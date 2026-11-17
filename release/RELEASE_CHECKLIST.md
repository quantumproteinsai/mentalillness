# Release checklist

Everything in `release/` is generated and reproducible. What remains are
decisions that are **yours**, not defaults to be inherited.

---

## DEPOSITED — 16 Nov 2026

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
3. Update **Version** to `1.1.0` and the **title** (it gained
   "and training-set-contamination labels"). Everything else — authors, ORCID,
   affiliation, CC BY 4.0, keywords — carries over and should be checked, not retyped.
4. Publish, then **fill the new DOI into two files**: `CITATION.cff` (add the `doi:`
   key, deliberately absent with a comment saying so) and the Citation section of
   `release/DATA_DESCRIPTOR.md`, which currently gives the concept DOI and explains why.
   Commit that.

#### A DOI IS RESERVED BUT NOT PUBLISHED — as of 17 Nov 2026

`10.5281/zenodo.24306057` is reserved on a **draft that has not been saved or
published**. Verified, not assumed: doi.org returns *DOI Not Found*, the record page and
the API both 404, and — the decisive check — the concept DOI `10.5281/zenodo.24290697`
still resolves to v1.0.0 with `is_last: true` at version index 0. **No v1.1.0 exists.**

**It is deliberately NOT written into `CITATION.cff` or `release/DATA_DESCRIPTOR.md`.**
Those are permanent, citable files, and a reserved DOI is not a published one. A
reserved DOI also lives only as long as its draft: discard the draft and that number is
gone, and a later "New version" reserves a different one.

**Verify before writing a DOI into anything.** The cheapest check is the concept DOI —
if it still resolves to the previous version, the new one is not published, whatever the
form displayed.

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
