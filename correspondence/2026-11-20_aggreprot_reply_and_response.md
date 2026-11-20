# AggreProt: their reply, and a draft response

**Status: REPLY RECEIVED 20 Nov 2026. RESPONSE SENT 20 Nov 2026** by the author, from
`contact@quantum-proteins.ai` to `joan.planas@mail.muni.cz`, cc `peta.kabourek@seznam.cz`
(the 'Petr' carried on their own reply). Sent substantially as drafted below. **Clock starts
now.** A silent inbox is not a blocker: AggreProt is already recorded UNAVAILABLE under §5.2b
and the confirmatory modern arm is AggrescanAI alone either way. Do not chase it.

---

## What they said — 20 Nov 2026, Joan Planas (`joan.planas@mail.muni.cz`)

Replying to `2026-11-16_aggreprot_weights_request.md`, to `contact@quantum-proteins.ai`,
copying Petr. Paraphrased, with the operative sentences verbatim:

- The GitHub distribution "lacks the models' weights, which are available to the scientific
  community upon request."
- **"Based on your provided background and research I did myself (<LinkedIn URL>), we cannot yet
  identify you as a member of the scientific community. Please provide us with an institutional
  email address and proof of your affiliation with a research-focused non-profit organisation."**
- **"In case this is not possible for you, please explain to us your situation and describe the
  use you intend for AggreProt. We expect that the use of AggreProt you make is not for
  commercial purposes."**
- Licensing, which answers a question that was outstanding: **the predictor and its weights are
  CC BY-NC-SA 4.0**; the **Zenodo repository** holds article/reproducibility data and is
  **CC BY 4.0**; the **web server is proprietary and may not be cloned outside their domains.**

### Why this is a reportable finding, independent of whether they say yes

The AggreProt paper's Code availability section states the weights are **"available to the
scientific community upon request."** The operational test for that membership turns out to be
**an institutional email address and affiliation with a research-focused non-profit.**

> **"Available upon request" and "available to anyone who asks" are not the same statement, and
> only the second is a reproducibility guarantee.** §5.2b already records AggreProt as
> **UNAVAILABLE, not as a failure**, on the stronger ground that the weights are not distributed
> at all. This exchange upgrades that from an unanswered email to **a stated policy with a
> documented eligibility test** — which is a sharper and fairer thing to report, and it is
> reportable whichever way they decide.

### What the weights could and could not be used for, if granted

**They cannot enter the confirmatory analysis, and this was registered before they were
refused.** §5.2b item 8, written 16 Nov and frozen 17 Nov: *"If they arrive after the freeze, it
is exploratory, reported separately, excluded from the confirmatory claim, with the date of
receipt stated."* **The freeze is 17 November 2026.** Anything arriving now is exploratory by a
rule fixed in advance, in a public dated commit.

So the ask is honest and modest, and saying so is the strongest thing in the letter: it is
verifiable, and it shows the request cannot buy an advantage.

---

## ⚠ THE PRE-SEND QUESTION — ANSWERED BY THE AUTHOR, 20 Nov 2026

**The letter went out stating the use is non-commercial. That is the author's representation,
made knowingly, and it now binds the project: AggreProt must not be used for any commercial
purpose, and if the surrounding activity ever becomes commercial the Loschmidt group must be
told before the tool is run again.** The original caveat is kept below unedited, because the
record should show what was asked and when, not only what was decided.

### The caveat as written before sending

**They wrote: "We expect that the use of AggreProt you make is not for commercial purposes."**

`quantum-proteins.ai` is a domain that can read as a company. **Whether this work is
non-commercial is a question of fact that only the author can answer, and it must be answered
accurately.** Misstating it to obtain licensed software would be worse than not having the
software — and AggreProt is already recorded as UNAVAILABLE, so the project loses nothing by
being unable to make the claim. If any part of the surrounding activity is commercial, say so
and let them decide; the draft below assumes it is not and must be edited if that is wrong.

---

## RESPONSE AS SENT — 20 Nov 2026

**From:** `contact@quantum-proteins.ai`
**To:** `joan.planas@mail.muni.cz`
**Cc:** `peta.kabourek@seznam.cz`
**Subject:** Re: AggreProt standalone — request for the model files (`nnap-data.zip`)

---

Dear Dr Planas,

Thank you for the clear answer, and particularly for setting out the three-way licensing split —
CC BY-NC-SA 4.0 for the predictor and weights, CC BY 4.0 for the Zenodo record, proprietary for
the web server. That resolves a discrepancy I could not settle from public sources, where the
repository `LICENSE`, the Zenodo record and bio.tools disagree with one another. I will cite the
licence as you state it regardless of how this request ends.

**On your question, plainly: I have no institutional affiliation and no institutional email
address.** I am an independent researcher and I would rather say so than present something that
does not hold up. Taking up your alternative, here is the situation and the intended use.

**The work.** It is a pre-registered benchmark of sequence-based aggregation predictors against
experimentally mapped aggregation-critical regions, chiefly in scaffold proteins associated with
chronic mental illness. The statistic, the decoy construction and the success threshold were
written down before any predictor was run, and the pre-registration is a public document with a
dated freeze commit. The validation set is deposited and citable:

- **Dataset:** https://doi.org/10.5281/zenodo.24394773 — 27 curated regions across 17 proteins,
  CC BY, with per-row provenance and a data descriptor.

I offer those in place of an institutional address because they are the part of the claim you can
actually check. They are dated, they are public, and they commit me in a way an email domain does
not.

**The intended use, stated narrowly.** I would run the standalone AggreProt locally, pinned to a
recorded version, over a fixed set of about thirty short sequence regions, and report its
per-region output alongside the other predictors. Nothing else. In particular:

- **AggreProt would enter as an exploratory arm only, not the confirmatory analysis.** My
  pre-registration fixed in advance that any predictor whose weights arrive after the freeze is
  reported separately and excluded from the confirmatory claim. The freeze was 17 November 2026,
  so that applies here. I mention it because it means this request cannot be used to strengthen a
  headline result, and you can verify the rule and its date rather than take my word for it.
- **The use is non-commercial**, and I accept the CC BY-NC-SA 4.0 terms and your terms of use.
- **I would not redistribute the weights**, publish them, mirror them, or include them in any
  repository or deposit — my own repository would record only the version string, the invocation
  and the outputs.
- **I would not clone or redeploy the web server**, and I have not done so.
- AggreProt and Planas-Iglesias et al. would be cited in full.

**What I can offer in return.** I am glad to put any of the above in writing in whatever form you
need, and to send you the draft and the AggreProt results before publication, so that you can see
how the tool is described and correct anything I have got wrong about it.

If you would still rather not release the weights to someone without an affiliation, I understand
that completely and there is no need to explain further. In that case I will record AggreProt as
unavailable for local, version-pinned execution and will say exactly that — not that it
underperformed, and not that it failed, because neither would be true and it would be unfair to
the tool. I would simply ask that you tell me so plainly, so that what I publish about its
availability is accurate.

With thanks for your time, and for taking the trouble to answer in detail,

Bertrand Mercier des Rochettes

---

## When a reply arrives

- **Granted** → record the date of receipt, run it as an exploratory arm under §5.2b item 8,
  amend §5.2b with the date, and keep the weights out of the repository and out of every deposit.
  `.gitignore` them by name first; `git add -A` has already swept licensed material in once.
- **Refused** → record the refusal and its stated grounds. `release/DATA_DESCRIPTOR.md` and §5.2b
  then say that the weights were requested on 16 Nov 2026 and declined on <date> for want of an
  institutional affiliation. **That is a stronger and more honest sentence than the one we have
  now**, and it is a fact about the tool's accessibility, not about its quality.
- **Either way** the confirmatory modern arm stays AggrescanAI alone, and §5.2b's narrowed claim
  — *a* PLM-based predictor, not *modern predictors* — stands unchanged.
