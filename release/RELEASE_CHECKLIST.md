# Release checklist

Everything in `release/` is generated and reproducible. What remains are
decisions that are **yours**, not defaults to be inherited.

## 1. Licence

Not chosen. The usual choice for a dataset is **CC0** (public domain) or
**CC BY 4.0** (attribution required).

One thing to decide deliberately rather than by habit: several rows **quote
sentences** from papers under varying publisher licences. Quotation for
scholarly purposes is normal and is not what a dataset licence governs — but the
quotes are substantial in places, and a few come from papers that are not open
access. Worth a minute's thought before picking.

## 2. Authorship

`CITATION.cff` has your name and `TODO AUTHOR` markers for ORCID, affiliation,
co-authors and whether to publish an email. **I left contact details blank on
purpose** — publishing them is a decision, not a formality.

Also to settle: whether anyone else merits authorship on the dataset.

## 3. Version number

Currently `1.0.0-draft`, set in `scripts/build_release.py`. Drop `-draft` when
depositing. **Do not deposit while the string says draft.**

## 4. Where to deposit

Zenodo is the usual choice and mints a DOI. It also links to a GitHub release if
you want the code alongside. Alternatives: Figshare, Dryad, or a journal's data
descriptor track.

**This repository has no remote decided for public release** — `CLAUDE.md` notes
that whether to add one is the author's decision. Deposit is an outward-facing,
hard-to-reverse act; nothing here does it for you.

## 5. Decide what the release claims

The descriptor currently states the limitations plainly, including that the
discordant stratum holds **4 documented rows** and supports a case series rather
than a rate. **Do not soften that on the way to deposit.** If the dataset is
published before the benchmark, that honesty is the thing that makes it citable.

## 6. Before each rebuild

```
python3 scripts/validate_regions.py   # must exit 0
python3 scripts/build_release.py
```

The validator is a gate, not a formality — it caught a retired field name
surviving in a row on its first run.

## 7. Still open upstream

- 8 of 17 rows are `stratum: PENDING` and need a predictor run or a published one.
- `PREREGISTRATION.md` §12 steps 4-5 (freeze) are not done. The dataset can be
  published without them; the benchmark cannot.
