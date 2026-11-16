# Release checklist

Everything in `release/` is generated and reproducible. What remains are
decisions that are **yours**, not defaults to be inherited.

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

### Steps 1-4 are DONE as of 16 Nov 2026

Validator passes, `VERSION` is `1.0.0`, the release is rebuilt, and the commit
is tagged `v1.0.0` and pushed. What remains is on Zenodo and GitHub, not here.

### What remains

**Chosen route: link the GitHub repository to Zenodo.**

1. The repository must be **public** — Zenodo's GitHub page lists public
   repositories only.
2. zenodo.org -> GitHub -> authorise -> toggle the repository **On**. Use
   **Sync now** if it is not listed.
3. **Zenodo only archives releases created AFTER the toggle is on.** The
   `v1.0.0` tag already exists, so publish a GitHub *Release* from that existing
   tag once the toggle is on. No re-tagging is needed.
4. Zenodo reads `.zenodo.json` and mints the DOI.
5. Check the published record: title, sole creator with ORCID, licence CC BY
   4.0. **Metadata can be edited after publication; the files cannot.**

### KNOW WHAT THIS ROUTE DEPOSITS

**The GitHub integration archives the WHOLE REPOSITORY, not just `release/`.**
Zenodo has no ignore mechanism for it. So the DOI covers `research_notes/` --
which `CLAUDE.md` describes as machine-generated and unverified, under a
standing rule never to cite across that line -- along with `CLAUDE.md`,
`STATE.md` and `correspondence/`.

That is defensible, and publishing the pre-registration alongside the data is
arguably a virtue. **It should be a decision, not an inheritance.** The manual
upload route deposits exactly the four files in `release/` and nothing else.

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
