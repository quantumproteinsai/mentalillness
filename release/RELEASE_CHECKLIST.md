# Release checklist

Everything in `release/` is generated and reproducible. What remains are
decisions that are **yours**, not defaults to be inherited.

---

## BATCH CHANGES; DO NOT MINT A DOI PER EDIT — policy, 18 Nov 2026

**Three deposits were made in two days.** Each was justified on its own, but a dataset
whose version number moves faster than its content is harder to cite, not easier: a reader
choosing between four DOIs has to work out which difference mattered, and the answer is
usually "none that affects you".

**So: accumulate, then deposit.** The replacement for depositing on every edit is not
forgetting — it is `scripts/deposit_status.py`, which compares the working file against
the most recently deposited artefact and prints what has piled up:

```
python3 scripts/deposit_status.py
```

It imports `build_release.build()` rather than reimplementing the transform, so a status
report cannot disagree with what the builder would actually write. It reads only — no
files, no network.

**The test for whether a batch is ready is not a count.** It is:

> **Would a reader who found the DOI and not the repository be misled by what is missing?**

A corrected claim, a changed `stratum`, a new row, a retraction → **yes, deposit.** More
commentary on a row, a tightened caveat, a note that only matters to someone auditing the
project → **no, it waits.**

**Currently owed: nothing.** The batch that was accumulating became v1.5.0 on 20 Nov 2026.
Run `python3 scripts/deposit_status.py` to see what has piled up since.

---

## v1.5.0 PREPARED — awaiting a reserved DOI — **NOT YET UPLOADED**

**`preflight_deposit.py` refuses on exactly two checks, and they are the right two**: the
`DOI-RESERVE-PENDING` placeholder in `CITATION.cff` and in `release/DATA_DESCRIPTOR.md`
(**two** occurrences there). Everything else passes — title in all four places, version
strings, 27 regions claimed in three files and found in the artefact, all five previously
deposited versions byte-unchanged, snippet in step with `.zenodo.json`.

### THE REMAINING STEPS ARE YOURS, AT THE FORM

1. <https://zenodo.org/records/24342313> (v1.4.0) → **New version**
2. **Reserve DOI**, give me the number — it replaces `DOI-RESERVE-PENDING` in
   `CITATION.cff` (the `doi:` key) and `release/DATA_DESCRIPTOR.md` (**two** occurrences)
3. `python3 scripts/preflight_deposit.py` → must exit 0
4. Commit; tag `v1.5.0` **and** `deposited-v1.5.0` at the same commit
5. Delete the five copied files, upload the v1.5.0 five, set **Version** to `1.5.0`,
   **leave Additional Description empty**, paste
   `release/zenodo_description_v1.5.0.snippet.html` into the Description **source view**
6. Publish → verify the concept DOI resolves to the new record
7. **Verify the new VERSION DOI resolves too** — `curl -o /dev/null -w '%{http_code}'
   -I https://doi.org/10.5281/zenodo.<new>` must not be 404. **This step is new and v1.4.0
   is why**: the concept DOI check passed there while the version DOI never registered.
8. **Add `1.5.0` to `release/deposited.json` in the commit that records the deposit.**

### What changed, and why it warrants a version

**A residue range is corrected, and that alone decides it.** DISC1's deleted region is
**384-414**, not 384-415 — settled 19 Nov 2026 by the corresponding author from sequencing
of the actual plasmids. **Every deposited version, v1.0.0 through v1.4.0, carries the wrong
value.** By this file's own test — *would a reader who found the DOI and not the repository
be misled by what is missing?* — a wrong residue range is the strongest possible yes.

Also: **six new rows** (CHCHD10, CHCHD2, TAF15, Orb2, β2-microglobulin, SOD1 — 21 → 27),
**`power_eligible` and `power_limit` promoted to core columns** after being on every row and
documented nowhere, `power_limit` normalised from a two-shape field to an object, and the
undocumented `cpad_status` token `CPAD_PRESENT` normalised to `CPAD_MEMBER` on three rows.

**The confirmatory cell did not move: still 2 rows.** That is in the descriptor as a funnel
table, because six new rows moving it by zero is the most useful thing this release says.

---

## v1.4.0 DEPOSITED 18 Nov 2026 — PUBLISHED, BUT ITS VERSION DOI NEVER REGISTERED

**Version DOI `10.5281/zenodo.24342313` does not resolve, and as of 20 Nov 2026 it still
does not.** This section said "READY TO UPLOAD — NOT YET PUBLISHED" until 20 Nov, which was
stale: `release/deposited.json` had recorded the deposit on 18 Nov, in the same commit, as
step 7 requires. **Two files in this repository disagreed about whether a DOI had been
minted.**

### What is actually true, checked 20 Nov 2026

| check | result |
|---|---|
| `zenodo.org/api/records/24342313` | **200** — `state: done`, `status: published`, all five files present, `version: 1.4.0` |
| concept DOI `…24290697` → | **`zenodo.org/records/24342313`** — v1.4.0 *is* the current version |
| `doi.org/10.5281/zenodo.24342313` | **404** |
| `api.datacite.org/dois/10.5281/zenodo.24342313` | **404** |
| `doi.org/10.5281/zenodo.24339193` *(v1.3.0, control)* | **302 → record** |
| `api.datacite.org/dois/…24339193` *(control)* | **200** |

**The record is fine; the DOI registration is what failed.** And the control makes the
diagnosis decisive: **v1.3.0's DOI was minted 2 h 26 min earlier the same day**
(10:54:21 UTC against 13:20:37 UTC), from the same account by the same workflow, and it
registered correctly. So do v1.1.0, v1.2.0 and the concept DOI. **v1.4.0 is the only one
that failed**, which rules out an account-level or workflow-level cause.

**This cannot be fixed from this repository.** Registration is Zenodo's action.
`correspondence/2026-11-20_zenodo_support_request.md` is the request to send, carrying the
table above.

**What to do about citations meanwhile:** cite the **record URL**
<https://zenodo.org/records/24342313>, or the concept DOI. `CITATION.cff`,
`release/DATA_DESCRIPTOR.md` and `README.md` all now say so explicitly rather than listing
a DOI that 404s — which is how an external correspondent found this in the first place.

### The lesson, and it is already a step in the v1.5.0 procedure above

**The concept-DOI check was passed and the version DOI was never checked.** The procedure
said *"Publish → verify the concept DOI resolves to the new record"*, and that check is
sound — it is the cheapest proof that a new version really went live — but **it does not
test the version DOI**, which is the one that goes into a citation and the one that was
sent to an external correspondent. Step 7 of the v1.5.0 procedure now tests it explicitly.

### What v1.4.0 changed

**No rows added or removed. A new core column, `structure`**, on the seven rows whose
region is the ordered core of a deposited fibril — PDB entry, chain, modelled range,
method, resolution, helical parameters, every candidate considered and the rule that
chose. **Its absence is informative**: no deposited structure exists for that row, which
is true of every DISC1 and TRIOBP-1 row.

Also the glycinin row's correction from the Supporting Information, read 18 Nov — which
**overturned one of that row's own claims** (Val165–Asp172 belongs to an adjacent chain,
where the row had recorded an alternative conformation).

**That correction is the part that decides it.** By this file's own test — *would a reader
who found the DOI and not the repository be misled by what is missing?* — a corrected
claim is a yes. The `structure` column alone would also qualify, since the core-polarity
analysis published alongside cannot be reproduced without it.

---

## v1.3.0 DEPOSITED — DOI reserved 18 Nov 2026, published and verified

**Reserved version DOI: `10.5281/zenodo.24339193`**, written into `CITATION.cff` and
`release/DATA_DESCRIPTOR.md` before upload. **`preflight_deposit.py` exits 0.** Tagged
`v1.3.0` and `deposited-v1.3.0` at the same commit; the tag message carries the md5s.

**Verified reserved-but-not-live, with controls, 18 Nov 2026:**

| check | result |
|---|---|
| `doi.org/10.5281/zenodo.24339193` | **404** — reserved, unpublished |
| `api/records/24339193` | **404** |
| concept DOI `…24290697` | **200 → records/24337561** — still v1.2.0 |
| `doi.org/…24337561` *(control)* | 200 |

**The placeholder appeared twice, as predicted** — the instruction block that made it
three in v1.2.0 is gone, so the count the procedure states is now the count in the file.

### THE REMAINING STEPS ARE YOURS, AT THE FORM

1. <https://zenodo.org/records/24337561> (v1.2.0) → **New version**
2. Delete the five copied files; upload the v1.3.0 five
3. Set **Version** to `1.3.0`. Title, keywords, authors, licence carry over — check, do
   not retype. **Leave the Additional Description empty**: it is the field that carried
   "Version 1.0.0" forward through two deposits.
4. Paste `release/zenodo_description_v1.3.0.snippet.html` into the Description **source
   view** (`<>`), not the visual editor
5. Publish → verify `10.5281/zenodo.24290697` resolves to the new record
6. **Add `1.3.0` to `release/deposited.json` in the commit that records the deposit.**
   The step that has failed twice; numbered now rather than remembered.

### What changed, and why it is a new version

**No rows added or removed. Seven `stratum` labels changed**, under §7a: six
`PENDING → DISCORDANT`, one `PENDING → CONCORDANT`, assigned mechanically from the legacy
run. A new core column **`stratum_assignment`** records the rule, the legacy score, the
previous value, and `confirmatory_eligible`.

**The confirmatory count does not move: still 2.** Six of the eight eligible-looking rows
carry `confirmatory_eligible: false`, because the label was applied after the modern arm
had run. **That flag is the reason this is a data change worth a DOI** — a reader of
v1.2.0 sees seven rows as `PENDING`; a reader of v1.3.0 sees how they were resolved *and*
which resolutions were blind.

Two placement decisions, both arguable and both stated: `stratum_assignment` is **core**,
not per-row commentary, because a consumer who cannot see `confirmatory_eligible` cannot
reproduce the confirmatory set; and the top-level key explaining it is **dataset
documentation**, not a project note, for the same reason.

### THE SAME DEFECT RECURRED ONE DAY AFTER BEING WRITTEN UP

Yesterday's defect 2 was *`1.1.0` was never added to `DEPOSITED`*. It was fixed by adding
that one line. **On 18 Nov the guard failed again, identically, because `1.2.0` was not
added either** — and it overwrote the just-deposited v1.2.0 artefacts, which were restored
from git with their md5s re-verified against the published record (`459495c4…`,
`f7bc5079…`).

**Patching the instance is not fixing the defect.** The list lived as a Python literal
that someone had to remember to edit in the same breath as publishing. So it is now
**`release/deposited.json`**, read by `build_release.py` *and* `preflight_deposit.py`,
with the rule stated in the file: **add a version the moment it is published, in the
commit that records the deposit.**

---

## v1.2.0 DEPOSITED — 18 Nov 2026 — published, verified, and now superseded in the working tree

**Reserved version DOI: `10.5281/zenodo.24337561`**, written into `CITATION.cff` and
`release/DATA_DESCRIPTOR.md` **before** upload, which is the order this file requires.

**`python3 scripts/preflight_deposit.py` exits 0.** All 24 checks pass, and the tree is
tagged **`deposited-v1.2.0`** — cut after the final rebuild and immediately before
upload, which is the v1.1.0 lesson applied. The tag message carries the md5s.

**Verified, not assumed, on 18 Nov 2026 — the reserved DOI is NOT live, which is the
correct pre-upload state:**

| check | result |
|---|---|
| `doi.org/10.5281/zenodo.24337561` | **404** — reserved, unpublished |
| `zenodo.org/api/records/24337561` | **404** |
| concept DOI `…24290697` via the API | **302 → `/api/records/24306057`** — still v1.1.0 |
| `zenodo.org/records/24306057` *(control)* | 200 |
| `doi.org/10.5281/zenodo.24290697` *(control)* | 200 |

The controls are not decoration. A 404 from a broken network looks identical to a 404
from an absent record, so a check that expects absence is worthless without a parallel
check that expects presence — the same reasoning as the `raw.githubusercontent.com`
cache finding in `STATE.md`.

### A FOURTH DEPOSIT DEFECT, FOUND ON THE v1.2.0 DRAFT — and this one is live on v1.1.0

**The Additional Description field has said "Version 1.0.0. DOI 10.5281/zenodo.24290698"
since the first deposit, and "New version" copies it forward.** Checked against the API
on 18 Nov 2026, not assumed:

```
record 24290698 (v1.0.0): notes = "Version 1.0.0. DOI 10.5281/zenodo.24290698. ..."
record 24306057 (v1.1.0): notes = "Version 1.0.0. DOI 10.5281/zenodo.24290698. ..."
```

So **the published v1.1.0 record currently states that it is version 1.0.0 and carries
v1.0.0's DOI.** It arrived on the v1.2.0 draft the same way and was deleted there.

**DELETED RATHER THAN CORRECTED, deliberately.** Correcting it would create a fifth
copy of version-and-DOI to keep in step — after `CITATION.cff`, `DATA_DESCRIPTOR.md`,
the built artefact's `_dataset`, and the Version field — and this copy has already
drifted twice. Everything it said is in `DATA_DESCRIPTOR.md`, which is uploaded.

**FIX v1.1.0's RECORD TOO.** Zenodo metadata is editable after publication, unlike
files, so delete the Additional Description on record 24306057 as well. This is the
*repairable* half of the v1.1.0 title problem: the deposited `CITATION.cff` cannot be
fixed because files are frozen, but record metadata can.

**Why none of the gates caught it:** `preflight_deposit.py` reads the repository, and
this field exists only on Zenodo. A check cannot see a field it is not told about, and
the form carries state the repository never sees. **The version-DOI pair now lives in
one more place than this file had ever counted** — which is the same miscount as the
title living in four places rather than three.

### THE FIVE REMAINING STEPS ARE YOURS, AT THE ZENODO FORM

1. Open <https://zenodo.org/records/24306057> (v1.1.0) → **New version**. Not a fresh
   upload: that mints an unrelated record with no link to the concept DOI.
2. **Delete the five files Zenodo copied into the draft**, then upload the five listed
   under "The five files to upload" at v1.2.0. Deleting affects the draft only; the
   published v1.1.0 files are frozen and untouchable.
3. Set **Version** to `1.2.0`. Title, keywords, authors, ORCID and CC BY 4.0 carry over
   from 1.1.0 unchanged — check them, do not retype them.
4. Paste `release/zenodo_description_v1.2.0.snippet.html` into the Description field's
   **source view** (the `<>` button at the right-hand end of the toolbar). Not the
   visual editor: that renders the tags literally, which happened twice on 17 Nov 2026.
   After pasting, check for four bullets with bold headings and no visible `<p>` or
   `&mdash;`.
5. **Publish**, then verify with the concept DOI rather than the form:
   `10.5281/zenodo.24290697` must resolve to the new record with `is_last: true`.
   A form displaying a DOI is not a published record.

**If the draft is discarded rather than published**, Zenodo reserves a different number
next time, and `10.5281/zenodo.24337561` must be replaced in both files and the
`deposited-v1.2.0` tag re-cut.

**After publishing**, record the five published md5s here against the local ones in the
tag message, and verify the concept DOI — that is what closed out v1.0.0 and v1.1.0.

### What changed, and why it is a new version rather than a repo-side edit

**Four rows** — ANXA11 39-74, TMEM106B 120-254, glycinin G4 164-190 (the first
non-animal row), and a DISC1 interval split into the two sub-intervals its source
actually tested. 17 → 21 rows, 8 → 11 proteins. A row added is a *data* change by this
file's own rule.

Two top-level keys moved from `project_notes` into `dataset_documentation`: the
decoy-window rule (how to read `frame`) and the name-vs-accession limit of the CPAD
screen (how far to trust `CPAD_ABSENT`). Both qualify a column a consumer would
otherwise over-trust.

**The honest headline is a negative, and the description says so**: the dataset grew
from 17 rows to 21 and **the usable discordant stratum did not move off 2 rows**.

### THREE DEFECTS IN THE RELEASE MACHINERY, FOUND WHILE PREPARING THIS

**1. `build_release.py`'s freeze guard did not work, and overwrote the deposited
v1.1.0 files.** The guard compared the set of CORE FIELD NAMES in the working file
against the deposited artefact and refused only when a field had been *added*. Between
1.1.0 and 1.2.0 four **rows** were added and no field, so it passed, and a test run at
`VERSION = '1.1.0'` rewrote both deposited artefacts with 21 rows. **They were recovered
from git and their md5s re-verified against the ones in the `deposited-v1.1.0` tag
message** — `14df6109…` and `d0971d25…` — which is the only reason this is a near miss
and not a lost deposit. The guard now compares **the bytes it is about to write** against
the bytes on disk, which is the property actually wanted and does not require anyone to
predict which kind of change matters.

**2. `1.1.0` was never added to `DEPOSITED`.** The guard could not have protected it
even had it worked, because the dict the code reads did not know 1.1.0 was deposited —
the fact lived here and in `STATE.md` instead. Same shape as the three errors of earlier
that day: *a true statement stored somewhere that could not act on it.*

**3. The title lives in FOUR places, not the three this file said.** The fourth is the
hardcoded `_dataset.title` in `build_release.py`, which is why **the deposited v1.1.0
artefact also carries the pre-1.1.0 title** — not just `CITATION.cff` as recorded below.
"Change it in all three and diff them against each other" is precisely the check that
passes while the fourth stays stale. `preflight_deposit.py` now compares all four.

**The lesson generalises past this file**: every defect in the v1.0.0 and v1.1.0
deposits was caught by a human eye or not at all, and two were not. The checklist's
lessons are now executable — `scripts/preflight_deposit.py` — because a warning in prose
is not a constraint.

### Also new: the description staging files are generated now

`scripts/build_zenodo_description.py` builds both `release/zenodo_description_v*.html`
files from `.zenodo.json`. This file previously said "both are generated from
`.zenodo.json`; regenerate them if the description changes" — and **nothing generated
them**; they were made by hand for v1.1.0, so "regenerate" named a step no committed code
performed. Verified faithful by regenerating v1.1.0's snippet and diffing: it reproduces
byte-for-byte apart from the v1.2.0 wording changes.

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
python3 scripts/validate_regions.py          # gate, must exit 0
python3 scripts/build_release.py             # refuses to touch a deposited version
python3 scripts/build_zenodo_description.py  # only if the description changed
python3 scripts/preflight_deposit.py         # gate, must exit 0 BEFORE uploading
```

The validator is a gate, not a formality — it caught a retired field name
surviving in a row on its first run.

`preflight_deposit.py` is the other gate, and it exists because **the deposit's own
failures were never caught by a gate**: v1.0.0 went up without its DOIs and v1.1.0 went
up with a stale title, both recorded here afterwards as lessons for a reader. It checks
the DOI is reserved and written in, that all four copies of the title agree, that the
version and row count match everywhere they are claimed, that previously deposited
artefacts are byte-unchanged against `HEAD`, and that the description snippet is in step
with `.zenodo.json`. **It deposits nothing and cannot.**

## Still open upstream (does not block the dataset)

- 8 of 17 rows are `stratum: PENDING` and need a predictor run, or a published
  one found by search.
- `PREREGISTRATION.md` §12 steps 4-5 (the freeze) are not done. **The dataset can
  be published without them; the benchmark cannot.**
