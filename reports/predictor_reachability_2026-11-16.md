# Predictor reachability, 16 Nov 2026

Checked for `PREREGISTRATION.md` §12 step 4. **Content-verified, not
status-code-checked** — see the warning below, which is the main finding.

| tool | arm | final URL after redirects | HTTP | body check | verdict |
|---|---|---|---|---|---|
| **TANGO** | §5.1 legacy | `tango.crg.es` | **200** | body is an **"ERROR 404 … maintenance"** page | **DOWN** |
| **AGGRESCAN** | §5.1 legacy | `andromeda.uab.cat/bioinf/aggrescan/` | 200 | names itself | **LIVE** |
| **FoldAmyloid** | §5.1 legacy | `antares.protres.ru`, `bioinfo.protres.ru` | **000** | — | **DEAD** (both hosts) |
| **ProA** | §5.1 legacy | **`mgm.ku.edu`** (lab homepage) | **200** | no mention of ProA | **DEAD** (silent redirect) |
| ANuPP | intermediate (§12.1 dec. 2) | `web.iitm.ac.in/bioinfo2/ANuPP/` | 200 | names itself | **LIVE** |
| AmylPred2 | not in either arm | `aias.biol.uoa.gr/AMYLPRED2/` | 200 | names itself | **LIVE** |
| PASTA 2.0 | not in either arm | `old.protein.bio.unipd.it/pasta2/` | 200 | names itself | **LIVE** |
| WALTZ | not in either arm | `waltz.switchlab.org` | **502** | — | **DOWN** (retried) |
| MetAmyl | not in either arm | `metamyl.genouest.org` | **502** | — | **DOWN** (retried) |
| ZipperDB | not in either arm | `services.mbi.ucla.edu/zipperdb/` | **000** | — | **DEAD** |

## The finding that matters more than the table

**A status code is not evidence a tool is reachable.** A naive
`curl -o /dev/null -w '%{http_code}'` sweep returned **200 for TANGO and 200 for
ProA**, and would have recorded both as available.

- **TANGO** serves a 404 page *under a 200 status* — the CRG IT team's
  maintenance notice.
- **ProA** returns 200 by *silently redirecting* to the lab's generic homepage.

**Three of the four legacy tools would have been misreported.** Only fetching the
body and looking for the tool's own name separates a live server from a
tombstone. Any future check in this project must verify content, record the final
URL after redirects, and retry 502s before calling them down.

## Consequence

**One of the four §5.1 legacy tools is usable today** (AGGRESCAN). That is worse
than §5.1 assumed on 15 Nov, and it is the strongest restatement of that
section's own rule that *a web form is not a reproducible tool*.

**It does not block the benchmark.** Every discordant row already carries a
*published* legacy run with the tools named — Bradshaw 2014, Murray 2017, Sharma
2023, Zaharija 2025 — so the legacy arm is cited rather than re-executed. See
the newly registered §5.1a. **What still has to run is the modern arm**, which is
the untested part and the entire point.

## Recheck before the freeze

TANGO's notice says *maintenance*, so it may return. Re-run this check
immediately before the §12 step 5 freeze commit and record the result, whichever
way it goes.
