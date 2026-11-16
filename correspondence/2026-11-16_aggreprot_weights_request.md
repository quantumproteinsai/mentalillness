# Draft email: request for the AggreProt model files

**Status: SENT, 16 Nov 2026**, by the author, with the first author copied.
Awaiting reply. The text below is the record of what was asked.

**Clock starts now.** If nothing arrives, this is not a dead end: see *When a
reply arrives* at the foot of this file. AggreProt is recorded as UNAVAILABLE,
which is a reportable finding about the tool's reproducibility, not a gap in
our work. Do not let a silent inbox hold up the freeze.

**To:** `davidbednar1208@gmail.com`, `jan.martinovic@vsb.cz`
*(both printed as corresponding authors in Planas-Iglesias et al., NAR 2024,
52:W159–W169)*

**Cc (optional):** Joan Planas-Iglesias — no address is printed in the paper; he
is reachable through Loschmidt Laboratories if you want the first author copied.

**Subject:** AggreProt standalone — request for the model files (`nnap-data.zip`)

---

Dear Dr Bednar and Dr Martinovic,

I am benchmarking sequence-based aggregation predictors against a small set of
experimentally mapped aggregation-critical regions, and I would like to include
AggreProt. I want to run it locally and pinned to a fixed version, rather than
through the web server, so that the run is reproducible by anyone who reads the
work.

The code at `github.com/loschmidt/aggreprot-predictor` installs cleanly, and the
README is clear. The one step I cannot complete is:

> `unzip nnap-data.zip -d aggreprot-predictor/`

I have not been able to find `nnap-data.zip`. It is not in the repository, and
the Zenodo release (10.5281/zenodo.19002542) is 22.9 kB in total, so it cannot
contain the trained networks. Without it there is no `nnap/data/Atomic.csv` and
no `nnap/data/models/sequential/`.

Could you point me to the archive, or send it? A checksum alongside it would be
very helpful — I record predictors by checksum where a version string is not
available, so that a later reader can confirm which exact model produced a
number.

Two smaller questions, if you have a moment:

1. **Licence.** The repository `LICENSE` is CC BY-NC-SA 4.0, the Zenodo record
   says CC BY 4.0, and the bio.tools entry says "Proprietary". I would like to
   cite the terms correctly — which governs the predictor and its model files?
2. **Defaults.** Is there a record of the web server's default parameters? I
   would like a local run to be comparable with results reported from the
   server.

May I add that your Introduction states the problem that prompted this work
better than I have managed to — that benchmarking on the curated APR databases
is "potentially biased, and their performance should always be validated by an
experiment". The dataset I am assembling is an attempt at a small, fully
hand-read alternative, and I would be glad to share it with you when it is
deposited.

Thank you for making the predictor available, and for any help with the model
files.

With best regards,

Bertrand Mercier des Rochettes
ORCID 0000-0002-1145-1881
contact@quantum-proteins.ai

---

## When a reply arrives

If the archive is supplied:

```
python3 scripts/record_predictor_provenance.py AggreProt /path/to/<a model file>
```

and record the archive's own SHA-256 plus the licence answer in
`data/predictor_provenance.json`, under
`_MODERN_ARM_STATUS_2026-11-16 → AggreProt`, which currently reads
`NOT ADMISSIBLE TODAY -- cannot be run locally.`

If no reply arrives, **AggreProt stays recorded as unavailable, not as a
failure** — the same treatment ProA receives. That is a finding about the tool's
reproducibility, and it is reportable as one. §5.2 is then satisfied by
AggrescanAI alone, and the modern arm must be described in the title as one
tool.
