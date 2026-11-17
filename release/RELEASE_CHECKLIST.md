# Release checklist

Everything in `release/` is generated and reproducible. What remains are
decisions that are **yours**, not defaults to be inherited.

---

## v1.1.0 DEPOSITED — 17 Nov 2026

**<https://zenodo.org/records/24306057>** — version DOI `10.5281/zenodo.24306057`

Verified after publication, not assumed: the version DOI resolves; **the concept DOI
`10.5281/zenodo.24290697` now resolves to this record** (`index: 1, is_last: true`),
which is the check that actually proves a new version went live; all five files present
with md5 matching the local copies; version 1.1.0, CC BY 4.0, ORCID, 10 keywords.

### TWO TITLE DEFECTS, ONE PERMANENT

**1. The published title was malformed at upload and has been corrected.** The new words
were *appended* to the old title rather than replacing it, giving
"…circularity and prediction-concordance labels and&nbsp;&nbsp;training-set-contamination
labels" — "labels" twice, with a double space. Metadata is editable after publication,
so this was fixed on the record.

**2. The DEPOSITED `CITATION.cff` carries the OLD title, and cannot be fixed.** The title
was updated in `.zenodo.json` and `release/DATA_DESCRIPTOR.md` but **not** in
`CITATION.cff` before upload, and deposited files are frozen. So a citation generated
from the deposited `CITATION.cff` gives v1.1.0's DOI and version with v1.0.0's title.

The repository copy is corrected, so v1.2.0 will be right. **This is recorded rather than
quietly fixed**, because the deposited file says otherwise and a reader comparing the two
deserves to know which is wrong. It is not worth a 1.1.1 deposit on its own; **if a 1.1.1
happens for another reason, this goes in it.**

### THE `v1.1.0` TAG IS NOT THE DEPOSIT — USE `deposited-v1.1.0`

The `v1.1.0` tag was cut *before* the frame fixes of 17 Nov, and **matches none of the
deposited files except `LICENSE`**. The tree that actually went to Zenodo is tagged
**`deposited-v1.1.0`** (commit `0746017`), whose five files reproduce the published md5s
exactly. The tag message carries those md5s.

`v1.1.0` is left where it is rather than moved: it is already published, and a moved tag
is worse than a wrong one. **Next time, tag after the final rebuild and immediately
before upload, and verify md5s against the record before tagging.**

**LESSON FOR NEXT TIME — the title lives in THREE places.** `.zenodo.json`, `CITATION.cff`
and `release/DATA_DESCRIPTOR.md`. Change it in all three *before* upload, and diff them
against each other; two of the three were right, which is exactly the case that passes a
casual look.

---

## v1.0.0 DEPOSITED — 16 Nov 2026

**<https://zenodo.org/records/24290698>**

| | |
|---|---|
| version DOI | `10.5281/zenodo.24290698` — cite this |
| concept DOI | `10.5281/zenodo.24290697` — latest version, use only if you mean that |
| licence | CC BY 4.0 |
| files | 5, byte sizes verified against the published record |

### `release/` NOW DIFFERS FROM WHAT WAS DEPOSITED, AND THAT IS CORRECT

`DATA_DESCRIPTOR.md` in this repository has been updated since publication to
carry the DOIs, which did not exist when it was uploaded. **The deposited files
are frozen and cannot be changed.** Zenodo lets you edit *metadata* after
publication, never files.

So do not try to reconcile them. **Any change to a deposited file requires a new
version** — bump `VERSION`, rebuild, tag, and deposit as v1.0.1 or v1.1.0, which
gets its own version DOI under the same concept DOI.

**What this means in practice:** small repo-side improvements to the descriptor
are free and should not trigger a new deposit. A new deposit is warranted when
the *data* change — a row added, a stratum resolved, an error corrected.

---

## SETTLED

### ~~2. Authorship~~ — done, and now complete

`CITATION.cff` and `.zenodo.json` carry:

- Bertrand Mercier des Rochettes
- ORCID `0000-0002-1145-1881`
- `contact@quantum-proteins.ai`

**Co-authors: none.** Settled by the author on 16 Nov 2026. It was asked and
answered rather than assumed, and the file now says so, so a later reader does
not mistake sole authorship for an unfinished field.

### ~~4. Where to deposit~~ — Zenodo

`.zenodo.json` is written and valid. Zenodo reads it automatically if you deposit
by linking a GitHub release; if you upload manually, it is still the record of
what the metadata should say.

### ~~1. Licence~~ — DECIDED 16 Nov 2026: CC BY 4.0

`LICENSE` now holds the **full, unmodified legal code**, fetched from
creativecommons.org — a licence is never paraphrased. `CITATION.cff` and
`.zenodo.json` already matched and were left alone.

The reasoning, recorded so it can be argued with later: the value of this
dataset is **curatorial**. The provenance, the circularity calls and the stratum
labels are the work. CC BY keeps attribution attached, which is what makes a
reader go back and check the reasoning. CC0 would maximise reuse but detach the
rows from the justification that makes them trustworthy.

**One limit is now stated in the descriptor**: several rows quote sentences from
papers under other licences, some closed — Navarro 2026 is Elsevier and reserves
text-and-data-mining rights. CC BY 4.0 covers *our curation*, not the quoted
material.

---

## STILL OPEN

### ~~3. Version number~~ — DROPPED 16 Nov 2026

`VERSION` in `scripts/build_release.py` is now `1.0.0`. The release was rebuilt,
the `-draft` artefacts deleted, and `CITATION.cff`, `.zenodo.json` and the
descriptor all follow it.

**What this means:** the files are deposit-ready. Nothing in the repository
deposits them.

### 5. What the release claims

The descriptor states the limitations plainly — 17 rows, a discordant stratum of
**4 documented rows** supporting a case series rather than a rate, 8 rows still
`PENDING`, rows that are not independent, and that insolubility is now reported
in control brains so these must not be called disease-specific aggregates.

**Do not soften that on the way to deposit.** If the dataset is published before
the benchmark, that honesty is what makes it citable.

---

## Deposit procedure

**Nothing in this repository deposits anything**, and nothing in it can.
Depositing is outward-facing and effectively irreversible: a Zenodo DOI is
permanent, and a published record can be superseded but not withdrawn cleanly.
**The deposit is the author's own action, from the author's own account.**

### v1.1.0 — PREPARED 17 Nov 2026, NOT YET DEPOSITED

Repo side is done: validator passes, `VERSION` is `1.1.0`, the release is rebuilt as
`aggregation_regions_v1.1.0.{json,csv}`, `CITATION.cff` and `.zenodo.json` are updated,
and the commit is tagged `v1.1.0` and pushed. **The v1.0.0 files are untouched** — and
`build_release.py` now refuses to rebuild a deposited version whose core fields have
changed, so a DOI cannot quietly stop describing what the script produces.

**What changed, and why it warrants a new version rather than a repo-side edit:** three
new core columns (`cpad_status`, `cpad_basis`, `cpad_checked`) recording the CPAD 2.0
training-set check. That is a *data* change by this file's own rule.

#### THE ROUTE IS MANUAL UPLOAD — correcting an error written here on 17 Nov 2026

An earlier draft of this section told you to publish a GitHub Release and said "the
Zenodo toggle is already on". **That was wrong.** v1.0.0 was deposited by **filling the
Zenodo form and uploading five files by hand** — that is why commit `8e4f104` verifies
*five file sizes* against the published record. The GitHub integration was never used
and the toggle is not known to be on. Keep the route the same as v1.0.0: a mixed history
is harder to audit than either route alone.

**Your action, from your own account:**

1. Open the published record <https://zenodo.org/records/24290698> and choose
   **"New version"**. This keeps the concept DOI `10.5281/zenodo.24290697` and mints a
   new version DOI. **Do not start a fresh upload** — that would create an unrelated
   record with no link to v1.0.0.
2. Zenodo copies the v1.0.0 files into the draft. **Delete all five**, then upload the
   five listed below. Deleting is safe: it affects the draft only, never the published
   v1.0.0, whose files are frozen.
3. Update **Version** to `1.1.0`, the **title** (it gained "and
   training-set-contamination labels"), the **description**, and **add two keywords**:
   `training set contamination` and `CPAD`. Authors, ORCID, affiliation and CC BY 4.0
   carry over and need checking, not retyping.

   > **`.zenodo.json` IS NOT READ ON THIS ROUTE.** It is the metadata file for the
   > GitHub integration, which is not in use here. Any keyword, title or description
   > change made there reaches Zenodo **only if you type it into the form**. The file is
   > still worth keeping in step, so that a later switch to the integration does not
   > silently publish stale metadata — but today it is documentation, not configuration.

   > **DO NOT PASTE THE DESCRIPTION MARKUP INTO THE FORM.** The field *stores* HTML —
   > the published v1.0.0 description contains `<p>`, `<ul>`, `<li>`, `<strong>`,
   > `<em>` and `&mdash;` — **but the form is a rich-text (WYSIWYG) editor**, so pasting
   > raw markup displays the tags as literal text, along with the `\n` escapes if the
   > text is copied out of the JSON string. Both failure modes were hit on 17 Nov 2026.
   >
   > **THE RELIABLE WAY — use the editor's source view.** The Description toolbar has a
   > **`<>`** button (right-hand end, beside undo/redo). Click it, select whatever is
   > already in the box and delete it, then paste the entire contents of
   > **`release/zenodo_description_v1.1.0.snippet.html`**, and leave source view. That
   > file is *only* the markup — no doctype, no `<html>`, no wrapper `<div>` — so there
   > is nothing to catch. Pasting into the **visual** editor instead is what produced
   > literal tags on 17 Nov 2026, twice.
   >
   > A second file, `release/zenodo_description_v1.1.0.html`, renders the same text in a
   > browser for copying as *rich* text, if the `<>` route is unavailable. Both are
   > generated from `.zenodo.json`; regenerate them if the description changes. **Neither
   > is uploaded.**
   >
   > **Check after pasting:** four bullets with bold headings, and no visible `<p>`,
   > `&mdash;` or `<div>`.
4. Publish, then **fill the new DOI into two files**: `CITATION.cff` (add the `doi:`
   key, deliberately absent with a comment saying so) and the Citation section of
   `release/DATA_DESCRIPTOR.md`, which currently gives the concept DOI and explains why.
   Commit that.

#### RESERVE THE DOI FIRST — the order matters, and an earlier draft of this file got it wrong

**Reserve → write the DOI into the files → upload → publish.** Not publish-then-patch.

An earlier draft of this section said to leave `doi:` out of `CITATION.cff` and fill it
in afterwards, on the reasoning that Zenodo mints the DOI at publication. **That is only
true if you do not reserve it.** Zenodo's *Reserve DOI* makes the number exist while the
draft is still unpublished — which is what v1.0.0 did, and why the **deposited** v1.0.0
`CITATION.cff` carries `doi: "10.5281/zenodo.24290698"` rather than an empty field.

Publish-then-patch cannot fix this, because **deposited files are frozen**: the DOI could
only ever reach the repository copy, leaving the deposited one silently inconsistent.
That is what happened to v1.0.0's `DATA_DESCRIPTOR.md`, which went up without the DOIs.
**For v1.1.0 both files carry it before upload.**

`10.5281/zenodo.24306057` is reserved for the v1.1.0 draft and is written into
`CITATION.cff` and `release/DATA_DESCRIPTOR.md`.

**THE CONDITION ON THAT NUMBER.** A reserved DOI belongs to one draft. **If that draft is
discarded rather than published, Zenodo reserves a different DOI next time and both files
must be updated.** As of 17 Nov 2026 it is reserved and NOT live — verified, not assumed:
doi.org returns *DOI Not Found*, the record page and API both 404, and the decisive check
is that the concept DOI `10.5281/zenodo.24290697` still resolves to v1.0.0 with
`is_last: true` at version index 0.

**The cheapest check that a version really published** is the concept DOI: if it still
resolves to the previous version, the new one is not live, whatever the form displayed.

#### The five files to upload

| file | what it is |
|---|---|
| `release/aggregation_regions_v1.1.0.json` | **authoritative** — all 17 rows, schema docs, per-row notes |
| `release/aggregation_regions_v1.1.0.csv` | core columns only |
| `release/DATA_DESCRIPTOR.md` | the descriptor a reader must read first |
| `LICENSE` | the full unmodified CC BY 4.0 legal code |
| `CITATION.cff` | citation metadata |

Same five as v1.0.0, with the data files at the new version. **`.zenodo.json` is not
uploaded** — it is metadata for the GitHub integration, not a dataset file, and this
route fills the form directly. **`RELEASE_CHECKLIST.md` is not uploaded either**: it is
addressed to the author, not to a reader of the dataset.

**This route deposits exactly those five files and nothing else** — not the repository,
not `PREREGISTRATION.md`, not `results/`. That is a decision, not an inheritance: the
DOI is for *the dataset*, and the analysis built on it is neither finished nor published.

### ~~Steps 1-4 for v1.0.0~~ — done 16 Nov 2026, deposited as above

### DO NOT PUT A DOI BACK INTO `.zenodo.json`

It was added there on 16 Nov 2026 and **removed the same day**. `.zenodo.json`
is read by the GitHub integration at *every* release, so it is a persistent
template; a DOI identifies *one version*. A version DOI left in that file means
a later v1.1.0 deposit carries v1.0.0's DOI, or is refused a new one — a fault
that surfaces months later, when the reason is forgotten.

**The DOI lives in `CITATION.cff`, in `release/DATA_DESCRIPTOR.md`, and in the
`notes` string.** Those describe one version. The rest of `.zenodo.json` does
not.

### Two DOIs, and they are not interchangeable

Zenodo mints a **concept DOI** that always resolves to the latest version, and a
**version DOI** for 1.0.0 specifically. **Put the VERSION DOI in the files.** The
concept DOI is for readers who want whatever is current, which is not what a
citation of this analysis means.

### After the DOI lands, it goes in three places

`CITATION.cff`, `.zenodo.json`, and the Citation section of
`release/DATA_DESCRIPTOR.md`, which currently tells readers to cite the version
and the repository **because no DOI exists yet**. That sentence stops being true
the moment one does.

## Before each rebuild

```
python3 scripts/validate_regions.py   # gate, must exit 0
python3 scripts/build_release.py
```

The validator is a gate, not a formality — it caught a retired field name
surviving in a row on its first run.

## Still open upstream (does not block the dataset)

- 8 of 17 rows are `stratum: PENDING` and need a predictor run, or a published
  one found by search.
- `PREREGISTRATION.md` §12 steps 4-5 (the freeze) are not done. **The dataset can
  be published without them; the benchmark cannot.**
