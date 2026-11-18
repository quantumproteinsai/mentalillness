#!/usr/bin/env python3
"""Generate the two Zenodo description helper files from .zenodo.json.

WHY THIS EXISTS. release/RELEASE_CHECKLIST.md says of these two files: "Both are
generated from .zenodo.json; regenerate them if the description changes." As of
17 Nov 2026 nothing generated them -- they were produced by hand for v1.1.0 and
there was no script to re-run, so "regenerate" was an instruction nobody could
follow. That is the same defect found three times the same day in the predictor
runners: an instruction naming a step that no committed code performs.

    python3 scripts/build_zenodo_description.py            # uses VERSION below
    python3 scripts/build_zenodo_description.py 1.2.0

WHAT THESE TWO FILES ARE FOR, and why there are two. The Zenodo description field
STORES HTML, but the upload form is a rich-text editor, so pasting raw markup into
the visual editor displays the tags as literal text. That failure was hit twice on
17 Nov 2026.

  *.snippet.html  -- markup ONLY: no doctype, no <html>, no wrapper element. This is
                     what you paste into the editor's SOURCE view (the `<>` button).
                     Nothing in it can be mistaken for page scaffolding.
  *.html          -- the same text wrapped in a viewable page, to open in a browser
                     and copy as RICH text if the source-view route is unavailable.

NEITHER FILE IS UPLOADED. They are staging aids for filling in the form.
"""
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.4.0'

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zenodo description v{v}</title>
<style>
  body{{font:16px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
       max-width:52em;margin:2rem auto;padding:0 1rem;color:#111;background:#fff}}
  .how{{background:#fff8e1;border:1px solid #e6c200;border-radius:6px;padding:.9rem 1.1rem;
       margin-bottom:1.6rem;font-size:14px}}
  .how code{{background:#fff;padding:1px 4px;border-radius:3px}}
  #desc{{border:1px solid #ccc;border-radius:6px;padding:1rem 1.2rem}}
  @media (prefers-color-scheme: dark){{
    body{{color:#e8e8e8;background:#121212}}
    .how{{background:#2a2408;border-color:#6b5a00}}
    .how code{{background:#1b1b1b}}
    #desc{{border-color:#444}}
  }}
</style></head><body>
<div class="how">
<strong>This page is a staging aid, not a file to upload.</strong> The preferred route is
to paste <code>release/zenodo_description_v{v}.snippet.html</code> into the Zenodo
Description field's <strong>source view</strong> (the <code>&lt;&gt;</code> button at the
right-hand end of the toolbar). Use this page only if that route is unavailable: select
the boxed text below, copy it as <em>rich</em> text, and paste into the visual editor.
Pasting raw markup into the visual editor renders the tags literally &mdash; that happened
twice on 17 Nov 2026. After pasting, check that the bullets have bold headings and that
no <code>&lt;p&gt;</code>, <code>&amp;mdash;</code> or <code>&lt;div&gt;</code> is visible.
</div>
<div id="desc">
{body}
</div>
</body></html>
"""


def main(version):
    meta = json.loads((ROOT / '.zenodo.json').read_text())
    desc = meta['description']

    # The description is a single line of concatenated block elements. Put each on
    # its own line so the snippet is reviewable in a diff, without altering it:
    # whitespace between block-level tags is not rendered.
    snippet = desc.replace('><p', '>\n<p').replace('><ul', '>\n<ul').replace('><li', '>\n<li')

    out = ROOT / 'release'
    sf = out / f'zenodo_description_v{version}.snippet.html'
    sf.write_text(snippet + '\n')

    hf = out / f'zenodo_description_v{version}.html'
    hf.write_text(PAGE.format(v=version, body=snippet))

    # A cheap guard against the failure this file exists to prevent: the snippet
    # must be markup only.
    for bad in ('<!doctype', '<html', '<body', '<head'):
        if bad in snippet.lower():
            raise SystemExit(f'SNIPPET CONTAINS PAGE SCAFFOLDING ({bad}) -- it must be '
                             f'markup only, or the source-view paste will be wrong.')

    print(f'wrote {sf.relative_to(ROOT)}  ({len(snippet)} chars of markup)')
    print(f'wrote {hf.relative_to(ROOT)}')
    print(f'  title in .zenodo.json: {meta["title"][:72]}...')
    print('  NEITHER FILE IS UPLOADED. Snippet -> source view; page -> rich-text fallback.')
    assert html.escape  # imported for the reader: nothing here escapes, by design
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else VERSION))
