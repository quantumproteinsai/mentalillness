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

---

## Addendum: a second TANGO host, and why it also fails

The author supplied `http://biophysique.mnhn.fr/tango`, a deployment not
previously recorded anywhere in this project. **It is a real TANGO host and it is
also down.**

- It redirects to **`https://tango.mnhn.fr/`**, which resolves to Cloudflare
  addresses (`2606:4700::…`) — so the DNS and the CDN entry exist.
- It returns **HTTP 530 with Cloudflare error code 1016, "Origin DNS error"**:
  Cloudflare cannot resolve the backend. **Consistent across three retries over
  ~20 s, and on every path tried.**
- This is a server-side misconfiguration or a decommissioned origin. It is not
  transient, and it is not something a client can route around.

**The authors' own software page still points TANGO at the canonical host.**
`https://switchlab.org/software` lists TANGO as `http://tango.crg.es/` — the host
serving the "ERROR 404 … maintenance" page. So the canonical URL is the one the
authors endorse, and it is temporarily down; the MNHN deployment is a separate
instance whose origin is gone.

**Verdict unchanged: TANGO cannot be run today, at either host.** The MNHN URL is
recorded here so the next check tries both.

## Addendum: a shared outage, and a tool worth a look

**WALTZ and SolubiS both redirect to `error.kuleuven.be` and return 502.** That
is one institution's hosting failure taking down several SWITCH lab tools at
once, not three independent coincidences — worth knowing, because it means their
return is a single event rather than three.

LIMBO (`limbo.switchlab.org`) is **LIVE**, so switchlab.org hosting is not
uniformly down.

**`Cordax` (`https://cordax.switchlab.org`) is LIVE and was not on our radar.**
The authors describe it as *"a structure-based machine learning approach for
studying sequence determinants of amyloid propensity"* — i.e. a **modern,
ML-based** amyloid predictor from the group that wrote TANGO.

**This is a §5.2 question, and it is the author's to answer, not Claude's.**
§5.2 admits a tool to the *confirmatory* modern arm only if it is
version-pinnable and runs locally. Cordax is a web server, so on the face of it
it is **exploratory** under that rule — the same verdict ANuPP received in §12.1
decision 2. **Worth checking whether it ships code or weights before deciding**;
if it does, it is a serious modern-arm candidate from the most relevant group
possible.

---

## CORRECTION: `biophysique.mnhn.fr/tango` is a DIFFERENT TANGO

**My error, corrected the same day.** The addendum above treated that URL as "a
real TANGO host" whose origin had died. **It was never a host for our TANGO.**

`http://biophysique.mnhn.fr/tango` is the distribution page for:

> Ollion J, Cochennec J, Loll F, Escudé C, Boudier T (2013). **"TANGO: a generic
> tool for high-throughput 3D image analysis for studying nuclear
> organization."** *Bioinformatics* **29**(14):1840-1841.
> doi:10.1093/bioinformatics/btt276

**TANGO** there stands for **Tools for Analysis of Nuclear Genome
Organization** — an ImageJ plug-in and R package (`rtango`) for segmenting
fluorescence microscopy images, GPL v2. **It has nothing to do with protein
aggregation.**

Our TANGO is:

> Fernandez-Escamilla A-M, Rousseau F, Schymkowitz J, Serrano L (2004).
> "Prediction of sequence-dependent and mutational effects on the aggregation of
> peptides and proteins." *Nat Biotechnol* **22**:1302-1306.

**So the 530 I measured was an unrelated tool's download page being down**, and
the aggregation predictor's status is **unchanged**: it has **one** host,
`tango.crg.es`, serving a soft-404 maintenance page. `switchlab.org/software`
confirms the single host.

### What I did wrong, since the method is the point of this report

The body check I introduced in this very report is what should have caught it,
and it half did: `tango.mnhn.fr` returned 530, so **I never saw any content at
all** — and I nonetheless asserted the host "is a real TANGO host." **That was an
inference dressed as a verification.** A 530 tells you a server is unreachable;
it tells you *nothing* about what software the server would have served. The rule
the rest of this report states — verify content, not status — applies equally
when there is no content: **an unreachable host cannot be identified, only
named.**

### The collision is a live citation hazard, not just our mistake

Two tools called TANGO, both in bioinformatics, both with papers in
*Bioinformatics*-family journals, published nine years apart. **A reader or a
tool-chain can cite the wrong one.** Any mention of TANGO in this project's
outputs must carry the Fernandez-Escamilla 2004 citation, not the bare name.

---

## SECOND CORRECTION: TANGO is LIVE. The protocol matters.

**`https://tango.crg.es/` serves the real TANGO site** — `<title>Homepage |
Tango</title>`, a Drupal installation on the lab's own FoldX theme, 21,690 bytes.

**`http://tango.crg.es/` serves CRG's "ERROR 404 … maintenance" page instead.**
Same hostname, two different sites, no redirect between them. My sweep tested
`http://` because that is the URL recorded in §5.1, in Bradshaw 2014 and on
`switchlab.org/software` — and so I reported a live tool as down.

**Corrected status of the §5.1 legacy arm: TWO of four are usable.**

| tool | verdict |
|---|---|
| **TANGO** | **LIVE** at `https://tango.crg.es/` |
| **AGGRESCAN** | **LIVE** at `andromeda.uab.cat/bioinf/aggrescan/` |
| FoldAmyloid | DEAD — both hosts, **both protocols**, 000 |
| ProA | DEAD — redirects to a lab homepage on http, 000 on https |

**Every other tool was re-tested over HTTPS and nothing else changed:** WALTZ,
MetAmyl and SolubiS remain 502 (the shared KU Leuven outage), ZipperDB and
FoldAmyloid remain 000.

### The third form of the same lesson

This report now contains three versions of one mistake, each caught only after
being made:

1. **A status code is not reachability.** TANGO and ProA both returned 200 while
   serving a maintenance page and a homepage.
2. **An unreachable host cannot be identified, only named.** I called
   `tango.mnhn.fr` "a real TANGO host" having seen a 530 and no content — and it
   was a different tool entirely.
3. **`http` and `https` can serve different sites at one hostname.** Checking the
   protocol recorded in the literature is not the same as checking the tool.

**The general rule: fetch the body, over both protocols, and confirm the tool
names itself.** Anything less reports infrastructure, not availability.

### Consequence for the freeze

**§5.1 is corrected to show TANGO LIVE.** §5.1a — citing published legacy runs
rather than re-executing them — **still stands on its own merits**, and is now
the stronger choice rather than the forced one: the published runs were done on
contemporaneous servers by the groups that mapped the regions. With TANGO and
AGGRESCAN live, our own runs can corroborate those two arms directly.
