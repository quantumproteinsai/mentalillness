# Zenodo support request: a published record whose version DOI never registered

**Status: DRAFT, NOT SENT.** Written by Claude for the author, 20 November 2026.

**Why this cannot be done from the repository.** DOI registration with DataCite is an
action Zenodo performs on publication. Nothing in this repository, and no unauthenticated
request, can make it happen. The deposit itself is correct and complete — the record is
published, holds all five files, and the concept DOI resolves to it. **Only the version
DOI's registration is missing.**

**Where to send it.** <https://zenodo.org/support>. Sign in first, so the request is linked
to the account that owns the record.

**Category: "Report bug or problem".** Checked against the live dropdown, 20 Nov 2026 --
there is no "Technical issue" option, which this file said until it was looked at. The
other plausible choices are worse: *General inquiry* invites a templated reply, and *Modify
files* is for changing the files on a published record, which is not what is being asked.
A DOI that was never registered at publication is a failure in their pipeline, so it is a
bug report.

**"Browser & OS" is a TOGGLE, not a text field** -- checked on the live form, 20 Nov 2026.
It attaches the browser and OS automatically ("Browser: Chrome 157, Operating System:
Windows") and nothing can be typed into it. **Leave it on and change nothing.** But say in
the BODY that the fault is server-side, because the attached browser string otherwise
invites support to chase a browser problem that does not exist: every check in this
request was made with `curl`, not a browser. That line is in the plain-text body below.

**"How can we help?" is a plain textarea.** Paste the plain-text version below, not the
markdown one -- tables written with pipes will arrive as unreadable pipe soup.

**What makes this request easy for them to act on, and worth keeping in the message.** The
same account published **v1.3.0 two hours and twenty-six minutes earlier the same day**,
by the same route, and **that DOI registered correctly**. That rules out an account-level
or workflow-level cause and points at a single failed registration call. Give them the
record id, the DOI, and both timestamps.

---

## The message

> **Subject: Published record 24342313 — version DOI 10.5281/zenodo.24342313 was never registered with DataCite**
>
> Hello,
>
> I have a published record whose version DOI does not resolve. I think the DataCite
> registration failed silently on publication, because everything on the Zenodo side looks
> correct.
>
> **Record:** <https://zenodo.org/records/24342313> — version 1.4.0 of "Experimentally
> mapped aggregation-critical protein regions", published 2026-11-18 at 13:20:37 UTC.
>
> **The DOI it displays:** `10.5281/zenodo.24342313`
>
> What I see:
>
> | check | result |
> |---|---|
> | `zenodo.org/api/records/24342313` | 200 — `state: done`, `status: published`, `submitted: true`, all five files present |
> | concept DOI `10.5281/zenodo.24290697` | resolves to `zenodo.org/records/24342313` — so this record *is* the current version |
> | `doi.org/10.5281/zenodo.24342313` | **404** |
> | `api.datacite.org/dois/10.5281/zenodo.24342313` | **404** |
> | `hdl.handle.net/api/handles/10.5281/zenodo.24342313` | **responseCode 100** (handle not found) |
>
> So the record is published and the concept DOI points at it, but the version DOI was
> never registered.
>
> **It looks like a one-off rather than something about my account.** The previous version
> of the same record, published the same day at 10:54:21 UTC — two and a half hours earlier,
> same workflow — registered correctly:
>
> | check | result |
> |---|---|
> | `doi.org/10.5281/zenodo.24339193` (v1.3.0) | 302 → record |
> | `api.datacite.org/dois/10.5281/zenodo.24339193` | 200 |
>
> `10.5281/zenodo.24290698` (v1.0.0), `10.5281/zenodo.24306057` (v1.1.0),
> `10.5281/zenodo.24337561` (v1.2.0) and the concept DOI all resolve too — 302 at doi.org
> and 200 at DataCite for every one of them. **v1.4.0 is the only one of the five version
> DOIs that does not.**
>
> Re-checked on 2026-11-20, two days after publication, in case registration was simply
> slow. It is unchanged.
>
> **Could you re-trigger the DataCite registration for `10.5281/zenodo.24342313`?** The
> DOI has been cited externally, so I would rather it were registered than replaced — but
> if minting that exact DOI is not possible, please tell me and I will state the record URL
> in its place.
>
> Thank you,
>
> Bertrand Mercier des Rochettes
> ORCID 0000-0002-1145-1881

---

## PASTE THIS ONE — plain text, for the form's textarea

**Subject:** Published record 24342313 — version DOI 10.5281/zenodo.24342313 was never registered with DataCite

```
Hello,

I have a published record whose version DOI does not resolve. I think the DataCite
registration failed silently on publication, because everything on the Zenodo side
looks correct.

Record:  https://zenodo.org/records/24342313
         "Experimentally mapped aggregation-critical protein regions", version 1.4.0,
         published 2026-11-18 at 13:20:37 UTC.
DOI it displays:  10.5281/zenodo.24342313

What I see:

  zenodo.org/api/records/24342313 ........... 200, state: done, status: published,
                                              submitted: true, all five files present
  concept DOI 10.5281/zenodo.24290697 ....... resolves to zenodo.org/records/24342313,
                                              so this record IS the current version
  doi.org/10.5281/zenodo.24342313 ........... 404
  api.datacite.org/dois/10.5281/zenodo.24342313 .... 404
  hdl.handle.net/api/handles/10.5281/zenodo.24342313 ... responseCode 100 (not found)

So the record is published and the concept DOI points at it, but the version DOI was
never registered.

This looks like a one-off rather than something about my account. The previous version
of the same record, published the SAME DAY at 10:54:21 UTC -- two and a half hours
earlier, same workflow -- registered correctly:

  doi.org/10.5281/zenodo.24339193 (v1.3.0) ......... 302 -> record
  api.datacite.org/dois/10.5281/zenodo.24339193 .... 200

10.5281/zenodo.24290698 (v1.0.0), 10.5281/zenodo.24306057 (v1.1.0),
10.5281/zenodo.24337561 (v1.2.0) and the concept DOI all resolve too -- 302 at doi.org
and 200 at DataCite for every one of them. v1.4.0 is the only one of the five version
DOIs that does not.

Re-checked on 2026-11-20, two days after publication, in case registration was simply
slow. Unchanged. Checked from two machines on two different networks (Linux and
Windows), with identical results, so it is not a local resolver or a cached response.
(The browser and OS this form attaches are not relevant: every check above was made
with curl, not a browser.)

Could you re-trigger the DataCite registration for 10.5281/zenodo.24342313? The DOI has
been cited externally, so I would rather it were registered than replaced -- but if
minting that exact DOI is not possible, please tell me and I will state the record URL
in its place.

Thank you,

Bertrand Mercier des Rochettes
ORCID 0000-0002-1145-1881
```

**Browser & OS:** a toggle. Leave it on; nothing can be typed there, and the body already
says the fault is server-side.

**Files:** nothing to attach. Everything above is checkable from the public API, which is
better evidence than a screenshot of it.

---

## Notes for the author before sending

- **Do not discard or re-publish the record while waiting.** The files of a published
  deposit are frozen and the DOI is already in print elsewhere; a new version does not
  repair a dead DOI, it only adds a live one beside it. v1.5.0 is being prepared anyway,
  which is the right way to move forward.
- **The timestamps are the load-bearing part.** They are what distinguishes "your account
  is misconfigured" from "one registration call failed". Both came from
  `zenodo.org/api/records/<id>` → `created`, so they are Zenodo's own values, not inferred.
- **Nothing in this message identifies anything beyond the public record** — record ids,
  DOIs, publication timestamps and an ORCID, all already public on Zenodo. No private
  detail is disclosed by sending it.
- **The three verbatim checks, if you want to re-run them yourself before sending.**
  Linux or macOS:

  ```sh
  curl -s -o /dev/null -w '%{http_code}\n' -I https://doi.org/10.5281/zenodo.24342313
  curl -s -o /dev/null -w '%{http_code}\n'    https://api.datacite.org/dois/10.5281/zenodo.24342313
  curl -s -o /dev/null -w '%{http_code}\n'    https://zenodo.org/api/records/24342313
  ```

  **On Windows PowerShell these three lines fail, and not for a reason about the DOI.**
  `curl` there is an alias for `Invoke-WebRequest`, which parses `-s` as `-SessionVariable`
  and refuses. Write `curl.exe` to reach the real curl Windows ships, and `NUL` for
  `/dev/null`:

  ```powershell
  curl.exe -s -o NUL -w '%{http_code}\n' -I https://doi.org/10.5281/zenodo.24342313
  curl.exe -s -o NUL -w '%{http_code}\n'    https://api.datacite.org/dois/10.5281/zenodo.24342313
  curl.exe -s -o NUL -w '%{http_code}\n'    https://zenodo.org/api/records/24342313
  ```

  Expected: **404**, **404**, **200**. A bare `302` on the first is the healthy answer for
  any *other* version's DOI — there is no `-L`, so curl does not follow the redirect, and
  302 means registered rather than failed.

  **If the first two ever return anything but 404, the problem has fixed itself and this
  message should not be sent.** Check before sending rather than after.

- **The checks were run twice, on two machines, and agree.** 20 Nov 2026 from Linux, and
  again the same day from Windows on a different network: 404, 404, 200 both times. Worth
  knowing before sending, because the one explanation a support desk will reach for first
  is a local resolver or cache, and two networks rule that out.
