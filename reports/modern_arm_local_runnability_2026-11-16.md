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

### A circularity question — now CLOSED, and the answer is bad

> **Settled 16 Nov 2026 by reading Navarro et al. (2026) *J. Mol. Biol.* **438**:169643, version of record.** The inference below was correct and understated. See the end of this report.

#### The original filename inference, kept for the record

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


---

## CLOSED: AggrescanAI is CPAD-trained, and the exposure is wider than CPAD

**Navarro et al. (2026), *J. Mol. Biol.* **438**:169643 — full PDF opened [READ,
version of record].** This supersedes the filename inference above.

> "We used the Curated Protein Aggregation Database (CPAD) 2.0 … The training
> subset (80%) has 75,524 total residues, of which 2,167 correspond to APR+
> positions."

and the shipped model is named explicitly:

> "the final predictive model corresponds to the ensemble trained on the
> **CPAD90** dataset using optimized hyperparameters, from now on called
> AggrescanAI."

which matches the weight filenames `cpad_hotidp90_model_cv_{1..5}.h5` exactly.

**The important part is what CPAD90 is.** It is CPAD *together with homologous
sequences*, built by transferring annotations through the HoTIDP server using
OrthoInspector and OmaDB orthologues. **So checking that one of our proteins is
absent from CPAD is not sufficient** — an orthologue of a CPAD protein can carry
a transferred APR annotation into training. And the membership list is not
published: the entire data-availability statement is *"Data will be made
available on request."*

The authors say it themselves:

> "the predictor was trained on datasets that, even with augmentation, currently
> encompass a restricted subset of experimentally validated Aggregation-Prone
> Regions."

### A third kind of circularity

This project already separates two: **`circularity_status`** (was a predictor in
the *discovery* path) and **`stratum`** (do experiment and prediction *agree*).
This is neither. It is **training-set membership of the benchmark row**, and it
is recorded in `regions.json` as
`_AGGRESCANAI_HITS_ON_OUR_ROWS_ARE_NOT_EVIDENCE_OF_PREDICTION`.

It bites immediately. Navarro reports AggrescanAI recovering tau R3 306–336, tau
`275VQIINK280`, and α-synuclein APRs in the N-terminus and NAC domain — **three
regions that overlap rows in our dataset.** Tau and α-synuclein are among the
most heavily annotated proteins in CPAD. **A hit on a training protein is recall,
not prediction.**

## The paper contradicts one of our own rows, and both sides are right

Our `tau 275-280` row is `CONCORDANT`, on von Bergen 2000: PHF6 and PHF6* "are
the only two spots in the tau sequence where a β conformation is strongly
predicted". Navarro says of the same segment:

> "AggrescanAI also identifies an additional APR within the second repeat (R2,
> residues 275–305) that is **not detected by Aggrescan**. This segment includes
> the 275VQIINK280 motif."

**Both are true.** They are different predictors — a 2000-era β-propensity method
and AGGRESCAN 2007. So the same region is concordant for one tool and discordant
for another.

**`stratum` as defined cannot express that.** It attaches one label to a region,
in exactly the way a benchmark ignoring `construct` attaches one label to a
protein — the failure mode `CLAUDE.md` was written to prevent, reappearing one
column over. **No row value was changed on the strength of this**; the finding is
recorded as `_STRATUM_IS_A_PROPERTY_OF_A_PAIR_NOT_OF_A_REGION`. Making stratum a
(region, predictor) pair is a schema change and must be registered, not slipped
in before a freeze.

## Read the margin before spending anything

Figure 2, AUROC on the external AmyPro set:

| tool | AUROC |
|---|---|
| **AggrescanAI** | **0.69** |
| ANuPP | 0.60 |
| **AggreProt** | **0.60** |
| **AGGRESCAN** | **0.58** |
| Aggrescan3D | **0.51** |

**No confidence intervals are given for any of them.** The structure-aware tool is
indistinguishable from random. The gap between the best modern predictor and the
2007 legacy one is **0.69 vs 0.58, unbarred**, self-reported by the winning tool's
authors on a benchmark they built — and which they themselves call inadequate.

**CLAUDE.md rule 2 applies before any compute is spent.** A benchmark of ours
aiming to resolve differences of that size must argue its power first, on 4
discordant rows.

## A third independent call for exactly this dataset

> "These observations highlight the need for a more specific, **gold-standard
> reference set of APRs** to improve benchmarking across prediction tools."

That is now **three groups in print** — Thompson 2025 (CANYA), Planas-Iglesias
2024 (AggreProt), Navarro 2026 (AggrescanAI) — saying the standard APR benchmark
databases cannot support predictor comparison. Navarro's closing wish list asks
for "improved the experimental annotation of APRs at residue-level resolution,
which would reduce label ambiguity".

**`data/regions.json` is that object.** The data descriptor currently argues its
own necessity; it should cite these three instead.

## Licence

| artefact | licence |
|---|---|
| GitLab repository | **none — no LICENSE file** |
| HuggingFace weights | none, no model card |
| paper | Elsevier, **not** open access; "All rights are reserved, including those for text and data mining, AI training, and similar technologies" |
