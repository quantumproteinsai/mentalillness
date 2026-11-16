# Can the modern arm run locally? — 16 Nov 2026

**§5.2 admits a modern predictor only if it is version-pinnable *and* runs
locally.** This report tests both tools against that rule by fetching the actual
repositories, not the catalogue entries.

**Verdict: one passes, one fails, and neither is pinned as distributed.**

| | AggreProt | AggrescanAI |
|---|---|---|
| code public | yes, GitHub + Zenodo v1.0 | yes, GitLab |
| **trained weights public** | **NO** | yes, HuggingFace |
| runs locally | **NO — blocked on missing weights** | **yes, after porting out of Colab** |
| version-pinnable | by Zenodo v1.0 / commit | **no tags**; pin by commit + HF revision |
| pinned *as distributed* | n/a | **NO — fetches a moving branch head** |
| licence | **three conflicting statements** | **none stated anywhere** |

---

## AggreProt — cannot be run locally today

Source: `https://github.com/loschmidt/aggreprot-predictor` [READ],
Zenodo `10.5281/zenodo.19002542` v1.0, published 13 Mar 2026 [READ],
Planas-Iglesias et al., *Nucleic Acids Research* 2024, **52**:W159–W169 [READ,
version of record, CC BY 4.0].

The repository installs cleanly in principle — Python 3.8, `pip3 install
./aggreprot-predictor/`, and the documented invocation is:

```
aggreprot-predictor predict-sequential-batch --out-dir out sequences.fa
```

**But step 3 of the README cannot be performed.** It says:

> `unzip nnap-data.zip -d aggreprot-predictor/`

and **never says where `nnap-data.zip` comes from.** It is not in the
repository — the tree is 11 Python files, `setup.py`, `LICENSE`, `README.md` and
`.internal_commit.txt`, and nothing else. It is not in the Zenodo archive, which
is **22.9 kB in total** and therefore cannot contain neural-network weights. A
web search for the filename returns nothing [EMPTY].

Without it the package has no `nnap/data/Atomic.csv` and no
`nnap/data/models/sequential/`, which are exactly the files the README tells you
to verify before installing.

**The paper does not supply them either.** Its entire Data availability statement
is [READ]:

> "Aggreprot is freely available and accessible at
> https://loschmidt.chemi.muni.cz/aggreprot/."

That is a *server* availability statement. There is no code-availability and no
model-availability statement; the GitHub repository and the Zenodo release both
postdate the paper by ~2 years.

### The ProA trap, for the third time

Three guessed URLs for the weights archive were probed:

```
https://loschmidt.chemi.muni.cz/aggreprot/nnap-data.zip          200  0 bytes  text/html
https://loschmidt.chemi.muni.cz/aggreprot/data/nnap-data.zip     200  0 bytes  text/html
https://loschmidt.chemi.muni.cz/aggreprot/static/nnap-data.zip   200  0 bytes  text/html
```

**All three return HTTP 200.** All three are the single-page-application catch-all
serving `text/html`, not a zip. This is the same failure mode that made ProA and
TANGO look alive in a status-code sweep, and it is now the **third independent
instance** in this project. The rule stands and should be treated as settled:
*a status code is not reachability; only the content type and the body are.*

### What would unblock it

One email to the corresponding authors — addresses are printed in the paper —
asking for `nnap-data.zip` and its checksum. **Until that arrives, AggreProt is
not admissible under §5.2.** It is not "failing"; it is *unavailable*, and must
be recorded as such, exactly as ProA is.

### Licence: three sources, three answers

| source | states |
|---|---|
| repository `LICENSE` | **CC BY-NC-SA 4.0** (Attribution-NonCommercial-ShareAlike) |
| Zenodo record | **CC BY 4.0** |
| bio.tools entry | **Proprietary** |

The repository file is the one that governs the code. **`NC` is not a formality
for this project** — the author's affiliation is a commercial domain, and
`ShareAlike` propagates to adapted material. This needs a deliberate decision,
not an assumption, before any AggreProt output is published.

---

## AggrescanAI — runs locally, but is not pinned as shipped

Source: `https://gitlab.com/bioinformatics-fil/aggrescanai` [READ], public,
created 6 Jun 2025, last activity 23 Feb 2026, 51 commits, **0 tags**.
Navarro et al. (2026) *J. Mol. Biol.*, DOI 10.1016/j.jmb.2026.169643 — **NOT
READ, no PDF opened.**

**The entire repository is three files**: `README.md`, `aggrescanai.ipynb`,
`docs/aggrescanai_logo.png`. Notebook sha256
`1e1e4bc0433eb718673af34e9ce99d6771cd699840b44c40dd240836d494e7d6`.

### It is not really a Colab tool

The notebook was read cell by cell. Apart from `#@param` form annotations —
which are **comments**, inert outside Colab — it is ordinary Python: `requests`,
`pandas`, `torch`, `transformers`, `tensorflow.keras`, `numpy`, `plotly`.
**Nothing is Colab-specific.** Porting it to a local script is mechanical.

So the README's "no installation required" is a convenience claim, not a
constraint. **AggrescanAI satisfies §5.2's local-execution rule.**

### What it actually computes

1. ProtT5 (`Rostlab/prot_t5_xl_half_uniref50-enc`) embeds each residue as a
   1024-dim vector.
2. **Five** Keras models, `homology_models/cpad_hotidp90_model_cv_{1..5}.h5`,
   each predict a per-residue probability.
3. Soft-voting: the arithmetic mean across the five.
4. The displayed profile is additionally smoothed by a moving average.

### Two free parameters that must be pre-registered

**`window_size`.** The results cell exposes smoothing as a user-adjustable
slider, default `7`, range 1–25. **Changing it changes the profile**, so it is a
free parameter in exactly the sense §4 forbids leaving open. It must be fixed in
writing before any run. *The raw column `aggrescanai_score` is unsmoothed — if we
report the raw score and fix the threshold instead, this parameter disappears.
That is the cleaner choice and is recommended.*

**Edge behaviour.** The smoother is `np.convolve(..., mode='same')`, which
**zero-pads at the termini**. The first and last `window_size//2` residues are
therefore biased downward by construction, not by biology. At the default this
is 3 residues at each end. Any region near a terminus would be scored against a
padded window — another reason to prefer the raw column.

### It is not reproducible as written

The notebook fetches weights from
`https://huggingface.co/alvaro-2/aggrescanai/resolve/main` — **`main`, a moving
branch head** — and calls `from_pretrained(transformer_link)` for ProtT5 **with no
`revision=`**. Both resolve to whatever is current on the day it runs. A silent
upstream update would change our numbers with nothing in the output to show it.

**This is TANGO's missing version number again, and worse**, because TANGO's bytes
at least cannot change under us once downloaded.

Pins recorded today, to be passed explicitly:

| artefact | pin |
|---|---|
| AggrescanAI HF model repo | revision `7aba68e65d620aa55b10f9550005efff3f3240e7`, lastModified 2025-05-27 |
| notebook | sha256 `1e1e4bc0…`, GitLab `main` as of 16 Nov 2026 |
| ProtT5 | **not yet pinned** — resolve and record the HF revision before any run |

No model card, no licence, and no `config.json` on the HuggingFace repo. **No
`LICENSE` file exists in the GitLab repository.** Licence is therefore *unstated*,
not permissive-by-default.

### A circularity question that must be answered before it is run

The weight files are named **`cpad_hotidp90_model_cv_*`**.

`data/regions.json` already carries `_CPAD_CONTAMINATION_WARNING`, recording that
CANYA (Thompson 2025) found TANGO, CamSol and Aggrescan were *trained on sequences
within CPAD*. **If AggrescanAI is also CPAD-trained, that contamination extends
from the legacy arm into the modern arm** — which is the arm the whole project
exists to test.

**This is an inference from a filename and nothing more.** It is not READ, not a
snippet of any paper, and must not be written into `regions.json` or the
pre-registration until the JMB paper's Methods are opened. It is recorded here as
a question, with a named way to settle it.

*Note also that the notebook downloads **only** the five `homology_models`. The 33
`balanced_models/` in the same HuggingFace repo are unused by the published
notebook — so "AggrescanAI" means the CPAD-named ensemble specifically.*

---

## The AggreProt paper corroborates our own CPAD warning, independently

Unprompted, and from the opposite direction, the AggreProt authors make our
argument for us [READ, p. W160]:

> "two other curated databases, AmyPro and CPAD 2.0, compile protein sequences
> with annotated APRs based on the literature search and are widely used for
> predictor benchmarking. However, we and other groups have recently contested
> this relatively common practice by experimentally investigating the amyloid
> propensity of some of the sequences and revealed **many inaccuracies in the
> database labels**. As a result, comparing protein-level predictions of
> aggregation propensity between different algorithms based on these databases is
> **potentially biased, and their performance should always be validated by an
> experiment**."

**This is stronger than the claim our warning currently makes.** Ours is about
*train/test overlap*; theirs is about *the labels being wrong*. Two independent
groups — the CANYA authors and the AggreProt authors — have now said in print
that benchmarking on these databases is unsound.

**That is the published justification for `data/regions.json` existing at all**: a
small, hand-read, experiment-anchored set with per-row provenance is the stated
remedy to a problem the field has named twice. It belongs in the data descriptor,
which currently argues the case on its own authority.

Follow-up worth obtaining: **Cima et al. (2024), bioRxiv
`10.1101/2024.03.06.583680`** — reference 35, cited for the experimental
contesting of the labels. Marked in the paper as *"preprint: not peer reviewed."*

---

## Consequence for §5.2, which is the author's call

As of today the modern arm is **one tool, not two**. §5.2 can be satisfied by
AggrescanAI alone, or AggreProt can be reinstated by obtaining one missing file.

**A single-tool modern arm weakens the headline question**, which is about a
*generation* of predictors rather than one program. Before scoring anything, the
choice is: wait for the AggreProt weights, widen the modern arm to another
version-pinnable local tool, or register explicitly that the modern arm is one
tool and say so in the title.

**Nothing was run.** Executing either tool on a dataset protein before the freeze
would breach the pre-registration. Note in particular that AggrescanAI's own
example sequence is **UniProt P37840, α-synuclein — which is a row in
`data/regions.json`** — so even its demo cannot be used as a smoke test.
Use an unrelated sequence.
