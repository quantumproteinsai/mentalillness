#!/usr/bin/env python3
"""AggrescanAI, run locally from pinned artefacts. PREREGISTRATION 5.2b / 12 step 6.

Faithful to aggrescanai.ipynb (sha256 1e1e4bc0433eb718673af34e9ce99d6771cd699840b44c40dd240836d494e7d6):
  ProtT5 per-residue embedding -> 5 CPAD90 MLPs -> soft-voting mean.

DELIBERATE DIFFERENCES FROM THE NOTEBOOK, each recorded because each could change a number:
  1. The notebook pulls weights from .../resolve/MAIN, a moving branch. We read from
     local copies downloaded at the PINNED revisions and checksummed.
  2. The notebook runs on Colab GPU. No GPU here, and prot_t5_xl_half is stored fp16,
     which CPU kernels do not support for these ops. We upcast to float32. That is an
     UPCAST -- it does not lose precision relative to the fp16 weights -- but it is a
     deviation and is recorded as one.
  3. Smoothing is NOT applied. In the notebook the moving average is display-only; the
     exported aggrescanai_score is the raw per-residue probability. PREREGISTRATION 5.3
     scores PLM tools per-residue, aggregated to 6-residue means, which we do downstream.

Usage: run_aggrescanai.py <out.csv> <id> <sequence>
"""
import hashlib
import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = ''

HERE = os.path.dirname(os.path.abspath(__file__))
# WHERE THE PINNED WEIGHTS LIVE. Made overridable 17 Nov 2026, same defect as the one
# fixed in score_rows.py: these resolved only against this script's own directory, where
# the multi-gigabyte artefacts are NOT committed and never will be, so the script could
# not be re-run from a clean checkout without silently failing on a missing path. The
# default is unchanged, so this alters no behaviour; AGGAI_HOME just names the directory
# holding protT5/ and aggai/. The revision pins and per-file SHA-256s below are what
# actually guarantee the weights are the right ones -- not their location.
_HOME = os.environ.get('AGGAI_HOME', HERE)
PROTT5 = os.path.join(_HOME, 'protT5')
MODELS = os.path.join(_HOME, 'aggai', 'models', 'homology_models')
PROTT5_REV = '94a6abc029ae13029317b140b7424e012bf8dfbf'
AGGAI_REV = '7aba68e65d620aa55b10f9550005efff3f3240e7'
AA = set('ACDEFGHIKLMNPQRSTVWY')


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def main(out_csv, ident, seq):
    seq = seq.strip().upper().replace(' ', '').replace('\n', '')
    bad = sorted(set(seq) - AA)
    if bad:
        raise SystemExit(f'non-standard residues in {ident}: {bad}')

    import numpy as np
    import torch
    from transformers import T5EncoderModel, T5Tokenizer
    from tensorflow.keras.models import load_model

    torch.set_grad_enabled(False)
    torch.set_num_threads(os.cpu_count() or 4)

    tok = T5Tokenizer.from_pretrained(PROTT5, do_lower_case=False, legacy=False)
    enc = T5EncoderModel.from_pretrained(PROTT5).float().eval()

    spaced = ' '.join(list(seq))
    ids = tok(spaced, add_special_tokens=True, return_tensors='pt')
    out = enc(input_ids=ids['input_ids'], attention_mask=ids['attention_mask'])
    emb = out.last_hidden_state[0, :-1].numpy()   # drop the trailing </s>, as the notebook does

    if emb.shape[0] != len(seq):
        raise SystemExit(
            f'EMBEDDING LENGTH MISMATCH for {ident}: got {emb.shape[0]} rows for a '
            f'{len(seq)}-residue sequence. Refusing to score a misaligned profile -- '
            f'an off-by-one here would shift every residue number in the result.')
    if emb.shape[1] != 1024:
        raise SystemExit(f'expected 1024-d embeddings, got {emb.shape[1]}')

    files = [os.path.join(MODELS, f'cpad_hotidp90_model_cv_{i}.h5') for i in range(1, 6)]
    models = [load_model(f, compile=False) for f in files]
    preds = np.stack([m.predict(emb, batch_size=32, verbose=0).reshape(-1) for m in models])
    score = preds.mean(axis=0)
    spread = preds.max(axis=0) - preds.min(axis=0)

    with open(out_csv, 'w') as fh:
        fh.write('# AggrescanAI local run, CPAD90 homology ensemble (soft-voting mean of 5)\n')
        fh.write(f'# id={ident} length={len(seq)}\n')
        fh.write(f'# prott5_revision={PROTT5_REV}\n')
        fh.write(f'# aggrescanai_weights_revision={AGGAI_REV}\n')
        fh.write(f'# notebook_sha256=1e1e4bc0433eb718673af34e9ce99d6771cd699840b44c40dd240836d494e7d6\n')
        for f in files:
            fh.write(f'# model {os.path.basename(f)} sha256={sha256(f)}\n')
        fh.write('# smoothing=NONE (raw per-residue probability; notebook smoothing is display-only)\n')
        fh.write('# precision=float32 upcast from fp16 weights (no GPU)\n')
        fh.write('position,residue,aggrescanai_score,ensemble_spread\n')
        for i, (a, s, d) in enumerate(zip(seq, score, spread), start=1):
            fh.write(f'{i},{a},{s:.6f},{d:.6f}\n')

    print(f'{ident}: {len(seq)} residues  '
          f'min={score.min():.4f} mean={score.mean():.4f} max={score.max():.4f}  '
          f'max_ensemble_spread={spread.max():.4f}')
    print(f'wrote {out_csv}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
