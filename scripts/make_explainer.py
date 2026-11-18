#!/usr/bin/env python3
"""Build the two illustrated explainers (English and French) as PDFs, plus the SVGs.

NO DEPENDENCIES, BY NECESSITY AND THEN BY CHOICE. No PDF or SVG library is installed in
this environment and installing one was not available, so this writes PDF directly: base-14
Helvetica with WinAnsi encoding, and figures as native PDF vector operators.

THE FIGURES HAVE ONE SOURCE. Each figure is a list of primitives in a y-down coordinate
box, rendered twice -- once to a real .svg file and once to PDF drawing operators. The two
therefore cannot drift, which is the only reason it is safe to say the .svg files are the
figures in the document rather than lookalikes.

    python3 scripts/make_explainer.py [outdir]     # default: docs/

Written for undergraduate readers: no assumed background beyond first-year biology and
the idea of a p-value.
"""
import os
import sys

# ----------------------------------------------------------------------------- palette
INK = (0.10, 0.10, 0.11)
MUTED = (0.42, 0.44, 0.48)
BLUE = (0.15, 0.39, 0.92)
BLUEL = (0.86, 0.91, 0.99)
WARM = (0.71, 0.33, 0.04)
WARML = (0.99, 0.93, 0.84)
RED = (0.73, 0.07, 0.11)
GREEN = (0.08, 0.50, 0.24)
GREY = (0.93, 0.93, 0.94)
WHITE = (1, 1, 1)

# ------------------------------------------------------------------- Helvetica metrics
_W = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667, "'": 191,
    '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333, '.': 278, '/': 278,
    ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015,
    '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556, '`': 333,
    '{': 334, '|': 260, '}': 334, '~': 584,
    'A': 667, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722,
    'I': 278, 'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778, 'P': 667,
    'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944, 'X': 667,
    'Y': 667, 'Z': 611,
    'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556, 'h': 556,
    'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833, 'n': 556, 'o': 556, 'p': 556,
    'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500,
    'y': 500, 'z': 500,
}
_WB = dict(_W)
_WB.update({
    'A': 722, 'B': 722, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'J': 556,
    'K': 722, 'L': 611, 'R': 722, 'S': 667, 'a': 556, 'b': 611, 'c': 556, 'd': 611,
    'e': 556, 'f': 333, 'g': 611, 'h': 611, 'i': 278, 'j': 278, 'k': 556, 'l': 278,
    'm': 889, 'n': 611, 'o': 611, 'p': 611, 'q': 611, 'r': 389, 's': 556, 't': 333,
    'u': 611, 'v': 556, 'w': 778, 'x': 556, 'y': 556, 'z': 500, "'": 238, ':': 333,
    ';': 333, '(': 333, ')': 333,
})
for _d in '0123456789':
    _W[_d] = 556
    _WB[_d] = 556
# Accented Latin-1 take their base letter's width; close enough for line breaking.
_FOLD = {'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a', 'ä': 'a',
         'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'û': 'u', 'ù': 'u', 'ü': 'u',
         'ç': 'c', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Ç': 'C', 'Î': 'I',
         'Ô': 'O', 'Û': 'U', '«': '"', '»': '"', '’': "'", '–': '-', '—': '-',
         '·': '.', '×': '+', '≈': '=', '≥': '=', '→': '-', '…': '.'}


def width(s, size, bold=False):
    t = _WB if bold else _W
    return sum(t.get(_FOLD.get(c, c), 556) for c in s) * size / 1000.0


def wrap(s, size, maxw, bold=False):
    out, line = [], ''
    for word in s.split():
        trial = word if not line else line + ' ' + word
        if width(trial, size, bold) <= maxw or not line:
            line = trial
        else:
            out.append(line)
            line = word
    if line:
        out.append(line)
    return out


# -------------------------------------------------------------------------- primitives
def rect(x, y, w, h, fill=None, stroke=None, lw=1, rx=0):
    return ('rect', x, y, w, h, fill, stroke, lw, rx)


def line(x1, y1, x2, y2, stroke=INK, lw=1, dash=None):
    return ('line', x1, y1, x2, y2, stroke, lw, dash)


def poly(pts, fill=None, stroke=INK, lw=1, close=False):
    return ('poly', pts, fill, stroke, lw, close)


def circ(cx, cy, r, fill=None, stroke=INK, lw=1):
    return ('circ', cx, cy, r, fill, stroke, lw)


def text(x, y, s, size=9, fill=INK, bold=False, anchor='start'):
    return ('text', x, y, s, size, fill, bold, anchor)


def arrow(x1, y1, x2, y2, stroke=INK, lw=1.4, head=5):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
    return [line(x1, y1, bx, by, stroke, lw),
            poly([(x2, y2),
                  (x2 - head * math.cos(a - 0.4), y2 - head * math.sin(a - 0.4)),
                  (x2 - head * math.cos(a + 0.4), y2 - head * math.sin(a + 0.4))],
                 fill=stroke, stroke=None, close=True)]


def flat(items):
    out = []
    for i in items:
        out.extend(i) if isinstance(i, list) else out.append(i)
    return out


# ------------------------------------------------------------------------- SVG writer
def _hex(c):
    return '#%02x%02x%02x' % tuple(int(round(v * 255)) for v in c)


def svg_of(fig, W, H):
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<svg xmlns="http://www.w3.org/2000/svg" width="%g" height="%g" '
         'viewBox="0 0 %g %g" font-family="Helvetica,Arial,sans-serif">' % (W, H, W, H)]
    for p in fig:
        k = p[0]
        if k == 'rect':
            _, x, y, w, h, fill, stroke, lw, rx = p
            o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" '
                     'stroke="%s" stroke-width="%g"/>'
                     % (x, y, w, h, rx, _hex(fill) if fill else 'none',
                        _hex(stroke) if stroke else 'none', lw))
        elif k == 'line':
            _, x1, y1, x2, y2, stroke, lw, dash = p
            d = ' stroke-dasharray="%s"' % dash if dash else ''
            o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" '
                     'stroke-width="%g"%s stroke-linecap="round"/>'
                     % (x1, y1, x2, y2, _hex(stroke), lw, d))
        elif k == 'poly':
            _, pts, fill, stroke, lw, close = p
            tag = 'polygon' if close else 'polyline'
            s = ' '.join('%g,%g' % q for q in pts)
            o.append('<%s points="%s" fill="%s" stroke="%s" stroke-width="%g" '
                     'stroke-linejoin="round" stroke-linecap="round"/>'
                     % (tag, s, _hex(fill) if fill else 'none',
                        _hex(stroke) if stroke else 'none', lw))
        elif k == 'circ':
            _, cx, cy, r, fill, stroke, lw = p
            o.append('<circle cx="%g" cy="%g" r="%g" fill="%s" stroke="%s" '
                     'stroke-width="%g"/>' % (cx, cy, r, _hex(fill) if fill else 'none',
                                              _hex(stroke) if stroke else 'none', lw))
        elif k == 'text':
            _, x, y, s, size, fill, bold, anchor = p
            a = {'start': 'start', 'middle': 'middle', 'end': 'end'}[anchor]
            esc = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            o.append('<text x="%g" y="%g" font-size="%g" fill="%s" text-anchor="%s"%s>%s'
                     '</text>' % (x, y, size, _hex(fill), a,
                                  ' font-weight="bold"' if bold else '', esc))
    o.append('</svg>')
    return '\n'.join(o)


# ------------------------------------------------------------------------- PDF writer
def esc(s):
    b = s.encode('cp1252', 'replace')
    return b.replace(b'\\', b'\\\\').replace(b'(', b'\\(').replace(b')', b'\\)')


class Page:
    def __init__(self):
        self.ops = []

    def _col(self, c, stroke):
        self.ops.append(b'%.3f %.3f %.3f %s' % (c[0], c[1], c[2], b'RG' if stroke else b'rg'))

    def text(self, x, y, s, size=10, fill=INK, bold=False):
        self._col(fill, False)
        f = b'/F2' if bold else b'/F1'
        self.ops.append(b'BT %s %.2f Tf 1 0 0 1 %.2f %.2f Tm (%s) Tj ET'
                        % (f, size, x, y, esc(s)))

    def figure(self, fig, x, ytop):
        """Draw a y-down figure box with its top-left at (x, ytop) in PDF space."""
        self.ops.append(b'q 1 0 0 -1 %.2f %.2f cm' % (x, ytop))
        for p in fig:
            k = p[0]
            if k == 'rect':
                _, rx_, ry, w, h, fill, stroke, lw, rr = p
                self.ops.append(b'%.2f w' % lw)
                if fill:
                    self._col(fill, False)
                if stroke:
                    self._col(stroke, True)
                self.ops.append(b'%.2f %.2f %.2f %.2f re' % (rx_, ry, w, h))
                self.ops.append(b'B' if (fill and stroke) else (b'f' if fill else b'S'))
            elif k == 'line':
                _, x1, y1, x2, y2, stroke, lw, dash = p
                self._col(stroke, True)
                self.ops.append(b'%.2f w 1 J' % lw)
                self.ops.append(b'[%s] 0 d' % (dash.replace(',', ' ').encode()
                                               if dash else b''))
                self.ops.append(b'%.2f %.2f m %.2f %.2f l S' % (x1, y1, x2, y2))
                self.ops.append(b'[] 0 d')
            elif k == 'poly':
                _, pts, fill, stroke, lw, close = p
                self.ops.append(b'%.2f w 1 j 1 J' % lw)
                if fill:
                    self._col(fill, False)
                if stroke:
                    self._col(stroke, True)
                self.ops.append(b'%.2f %.2f m' % pts[0])
                for q in pts[1:]:
                    self.ops.append(b'%.2f %.2f l' % q)
                if close:
                    self.ops.append(b'h')
                self.ops.append(b'B' if (fill and stroke) else (b'f' if fill else b'S'))
            elif k == 'circ':
                _, cx, cy, r, fill, stroke, lw = p
                k_ = 0.5523 * r
                self.ops.append(b'%.2f w' % lw)
                if fill:
                    self._col(fill, False)
                if stroke:
                    self._col(stroke, True)
                self.ops.append(b'%.2f %.2f m' % (cx + r, cy))
                self.ops.append(b'%.2f %.2f %.2f %.2f %.2f %.2f c'
                                % (cx + r, cy + k_, cx + k_, cy + r, cx, cy + r))
                self.ops.append(b'%.2f %.2f %.2f %.2f %.2f %.2f c'
                                % (cx - k_, cy + r, cx - r, cy + k_, cx - r, cy))
                self.ops.append(b'%.2f %.2f %.2f %.2f %.2f %.2f c'
                                % (cx - r, cy - k_, cx - k_, cy - r, cx, cy - r))
                self.ops.append(b'%.2f %.2f %.2f %.2f %.2f %.2f c'
                                % (cx + k_, cy - r, cx + r, cy - k_, cx + r, cy))
                self.ops.append(b'B' if (fill and stroke) else (b'f' if fill else b'S'))
            elif k == 'text':
                _, tx, ty, s, size, fill, bold, anchor = p
                w = width(s, size, bold)
                if anchor == 'middle':
                    tx -= w / 2
                elif anchor == 'end':
                    tx -= w
                self._col(fill, False)
                f = b'/F2' if bold else b'/F1'
                # 1 0 0 -1 re-flips the glyphs upright inside the y-down CTM.
                self.ops.append(b'BT %s %.2f Tf 1 0 0 -1 %.2f %.2f Tm (%s) Tj ET'
                                % (f, size, tx, ty, esc(s)))
        self.ops.append(b'Q')

    def stream(self):
        return b'\n'.join(self.ops)


def write_pdf(path, pages, title):
    objs = []

    def add(b):
        objs.append(b)
        return len(objs)

    font1 = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica '
                b'/Encoding /WinAnsiEncoding >>')
    font2 = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold '
                b'/Encoding /WinAnsiEncoding >>')
    # The /Pages object is written after the two fonts and the two objects per page,
    # but each page must reference it, so its id is predicted here and asserted below.
    pages_id = len(objs) + 2 * len(pages) + 1
    kids = []
    for p in pages:
        s = p.stream()
        sid = add(b'<< /Length %d >>\nstream\n' % len(s) + s + b'\nendstream')
        pid = add(b'<< /Type /Page /Parent %d 0 R /MediaBox [0 0 595.28 841.89] '
                  b'/Resources << /Font << /F1 %d 0 R /F2 %d 0 R >> >> /Contents %d 0 R >>'
                  % (pages_id, font1, font2, sid))
        kids.append(pid)
    pt = add(b'<< /Type /Pages /Count %d /Kids [%s] >>'
             % (len(kids), b' '.join(b'%d 0 R' % k for k in kids)))
    assert pt == pages_id, (pt, pages_id)
    info = add(b'<< /Title (%s) /Producer (illness project, scripts/make_explainer.py) >>'
               % esc(title))
    root = add(b'<< /Type /Catalog /Pages %d 0 R >>' % pt)

    out = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    offs = []
    for i, o in enumerate(objs, 1):
        offs.append(len(out))
        out += b'%d 0 obj\n' % i + o + b'\nendobj\n'
    xref = len(out)
    out += b'xref\n0 %d\n' % (len(objs) + 1)
    out += b'0000000000 65535 f \n'
    for off in offs:
        out += b'%010d 00000 n \n' % off
    out += (b'trailer\n<< /Size %d /Root %d 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n'
            % (len(objs) + 1, root, info, xref))
    open(path, 'wb').write(bytes(out))
    return len(out)


# ============================================================================ FIGURES
FW = 470.0   # figure width, matching the text column


def fig_fibril(L):
    H = 150
    f = []
    f.append(text(0, 12, L['f1t'], 10, INK, True))
    xs = [40, 205, 370]
    # (a) folded
    f.append(circ(xs[0], 80, 34, fill=BLUEL, stroke=BLUE, lw=1.2))
    pts = []
    import math
    for i in range(70):
        a = i / 70.0 * 6.0 * math.pi
        r = 5 + i * 0.33
        pts.append((xs[0] + r * math.cos(a) * 0.85, 80 + r * math.sin(a) * 0.75))
    f.append(poly(pts, stroke=BLUE, lw=1.3))
    f.append(text(xs[0], 132, L['f1a'], 8.5, MUTED, anchor='middle'))
    # (b) misfolded
    pts = [(xs[1] - 36 + i * 4.5, 80 + 20 * math.sin(i * 0.9) * (1 - i / 32.0))
           for i in range(17)]
    f.append(poly(pts, stroke=WARM, lw=1.6))
    f.append(text(xs[1], 132, L['f1b'], 8.5, MUTED, anchor='middle'))
    # (c) fibril: stacked strands
    for i in range(7):
        y = 56 + i * 8
        f.append(poly([(xs[2] - 34, y), (xs[2] + 22, y), (xs[2] + 30, y + 4),
                       (xs[2] + 22, y + 8)], fill=WARML, stroke=WARM, lw=1))
    f.append(text(xs[2], 132, L['f1c'], 8.5, MUTED, anchor='middle'))
    f.extend(arrow(xs[0] + 44, 80, xs[1] - 46, 80, MUTED))
    f.extend(arrow(xs[1] + 44, 80, xs[2] - 44, 80, MUTED))
    return f, FW, H


def fig_profile(L):
    H = 200
    import math
    f = [text(0, 12, L['f2t'], 10, INK, True)]
    x0, y0, w, h = 40, 40, 400, 110
    # the experimentally mapped region
    rx, rw = x0 + 0.58 * w, 0.14 * w
    f.append(rect(rx, y0, rw, h, fill=GREEN + (), stroke=None))
    f[-1] = rect(rx, y0, rw, h, fill=(0.88, 0.95, 0.90), stroke=None)
    f.append(line(x0, y0 + h, x0 + w, y0 + h, INK, 1))
    f.append(line(x0, y0, x0, y0 + h, INK, 1))
    pts = []
    for i in range(161):
        t = i / 160.0
        v = (0.46 + 0.30 * math.sin(t * 10.5) + 0.22 * math.sin(t * 27 + 1.1)
             + 0.14 * math.sin(t * 54 + 0.4))
        if 0.20 < t < 0.30:
            v += 0.55 * math.exp(-((t - 0.25) / 0.028) ** 2)
        if 0.58 < t < 0.72:
            v -= 0.18
        v = max(0.03, min(1.0, v))
        pts.append((x0 + t * w, y0 + h - v * (h - 10)))
    f.append(poly(pts, stroke=BLUE, lw=1.5))
    f.append(text(x0 - 6, y0 + 6, L['f2y1'], 7.5, MUTED, anchor='end'))
    f.append(text(x0 - 6, y0 + h, L['f2y0'], 7.5, MUTED, anchor='end'))
    f.append(text(x0 + w / 2, y0 + h + 16, L['f2x'], 8.5, MUTED, anchor='middle'))
    f.append(text(rx + rw / 2, y0 - 6, L['f2reg'], 8, GREEN, True, anchor='middle'))
    f.extend(arrow(x0 + 0.33 * w, y0 + 8, x0 + 0.26 * w, y0 + 22, RED, 1.2))
    f.append(text(x0 + 0.34 * w, y0 + 6, L['f2peak'], 8, RED, True))
    f.append(text(x0, y0 + h + 36, L['f2cap'], 8, MUTED))
    f.append(text(x0, y0 + h + 48, L['f2cap2'], 8, MUTED))
    return f, FW, H


def fig_circ(L):
    H = 175
    f = [text(0, 12, L['f3t'], 10, INK, True)]
    cols = [(0, BLUE, BLUEL, 'f3a', 'f3a1'), (158, WARM, WARML, 'f3b', 'f3b1'),
            (316, RED, (0.99, 0.90, 0.90), 'f3c', 'f3c1')]
    for dx, col, light, k1, k2 in cols:
        f.append(rect(dx, 26, 148, 120, fill=light, stroke=col, lw=1.2, rx=5))
        f.append(circ(dx + 20, 46, 7, fill=col, stroke=None))
        for i, ln in enumerate(wrap(L[k1], 9, 112, True)):
            f.append(text(dx + 34, 44 + i * 11, ln, 9, col, True))
        for i, ln in enumerate(wrap(L[k2], 8, 126)):
            f.append(text(dx + 11, 76 + i * 10.5, ln, 8, INK))
    return f, FW, H


def fig_stat(L):
    H = 190
    f = [text(0, 12, L['f4t'], 10, INK, True)]
    x0, y = 24, 44
    tw = 26
    for i in range(15):
        inside = 7 <= i <= 10
        f.append(rect(x0 + i * tw, y, tw - 2, 20,
                      fill=(0.88, 0.95, 0.90) if inside else GREY,
                      stroke=GREEN if inside else (0.75, 0.75, 0.78), lw=1))
    f.append(text(x0, y - 8, L['f4prot'], 8, MUTED))
    f.append(text(x0 + 7 * tw + 2 * tw, y + 34, L['f4reg'], 8, GREEN, True, anchor='middle'))
    f.extend(arrow(x0 + 9 * tw, y + 28, x0 + 9 * tw, y + 22, GREEN, 1.1, 4))
    # ranked scores
    yy = 96
    f.append(text(x0, yy - 6, L['f4rank'], 8.5, INK, True))
    vals = [0.95, 0.88, 0.81, 0.74, 0.70, 0.66, 0.61, 0.58, 0.52, 0.47, 0.43,
            0.36, 0.30, 0.22, 0.12]
    order = [2, 11, 0, 13, 4, 6, 9, 7, 1, 12, 3, 14, 5, 10, 8]
    for i, v in enumerate(vals):
        inside = 7 <= order[i] <= 10
        f.append(rect(x0 + i * tw, yy + 34 - v * 30, tw - 2, v * 30,
                      fill=GREEN if inside else (0.78, 0.80, 0.84), stroke=None))
    f.append(line(x0, yy + 34, x0 + 15 * tw - 2, yy + 34, INK, 1))
    f.append(text(x0, yy + 50, L['f4form'], 9, INK, True))
    for i, ln in enumerate(wrap(L['f4cap'], 8, FW - 10)):
        f.append(text(x0, yy + 64 + i * 10.5, ln, 8, MUTED))
    return f, FW, H


ROWS = [('TRIOBP-1 1-59', 0.9995, 0.0409), ('ANXA11 39-74', 0.4134, 0.3315),
        ('DISC1 748-769', 0.9227, 0.9955), ('DISC1 384-415', 0.3189, 0.4164),
        ('glycinin 164-190', 0.1645, 0.3884), ('TMEM106B 120-254', 0.7156, 0.9900),
        ('TRIOBP-1 333-340', 0.0388, 0.4240), ('TRIOBP-1 324-348', 0.1235, 0.9079),
        ('DISC1 691-836', 0.0812, 0.9994)]


def fig_results(L):
    H = 276
    f = [text(0, 12, L['f5t'], 10, INK, True)]
    x0, y0, h = 118, 34, 150
    bw, gap = 16, 38
    for i, (nm, tg, ag) in enumerate(ROWS):
        x = x0 + i * gap
        f.append(rect(x, y0 + h - tg * h, bw / 1.0 - 2, tg * h, fill=(0.62, 0.66, 0.72),
                      stroke=None))
        f.append(rect(x + bw - 1, y0 + h - ag * h, bw - 2, ag * h, fill=BLUE, stroke=None))
    f.append(line(x0 - 6, y0 + h, x0 + 9 * gap, y0 + h, INK, 1))
    f.append(line(x0 - 6, y0, x0 - 6, y0 + h, INK, 1))
    yb = y0 + h - 0.05 * h
    f.append(line(x0 - 6, yb, x0 + 9 * gap, yb, RED, 1.1, dash='3,2'))
    f.append(text(x0 + 9 * gap + 2, yb + 3, L['f5bar'], 7.5, RED, True))
    f.append(text(x0 - 10, y0 + 5, '1.0', 7.5, MUTED, anchor='end'))
    f.append(text(x0 - 10, y0 + h, '0', 7.5, MUTED, anchor='end'))
    f.append(text(x0 - 10, y0 + h / 2, L['f5y'], 8, MUTED, anchor='end'))
    for i, (nm, tg, ag) in enumerate(ROWS):
        x = x0 + i * gap + bw - 2
        f.append(text(x, y0 + h + 10, nm.split()[0], 6.6, MUTED, anchor='middle'))
        f.append(text(x, y0 + h + 18, nm.split()[1], 6.6, MUTED, anchor='middle'))
    ly = y0 + h + 34
    f.append(rect(x0, ly, 11, 9, fill=(0.62, 0.66, 0.72), stroke=None))
    f.append(text(x0 + 16, ly + 8, L['f5leg1'], 8.5, INK))
    f.append(rect(x0 + 150, ly, 11, 9, fill=BLUE, stroke=None))
    f.append(text(x0 + 166, ly + 8, L['f5leg2'], 8.5, INK))
    for i, ln in enumerate(wrap(L['f5cap'], 8, FW)):
        f.append(text(0, ly + 26 + i * 10.5, ln, 8, MUTED))
    return f, FW, H



POLAR = [('FUS', 0.675, 0.9582), ('TMEM106B', 0.577, 0.9900), ('LECT2', 0.526, 0.4054),
         ('glycinin', 0.480, 0.3884), ('hnRNPA1', 0.465, 0.4626), ('SAA', 0.462, 0.2124),
         ('ANXA11', 0.441, 0.3315)]


def fig_polarity(L):
    H = 250
    f = [text(0, 12, L['f6t'], 10, INK, True)]
    x0, y0, w, h = 86, 32, 300, 160
    f.append(rect(x0, y0, w, h, fill=(0.985, 0.985, 0.99), stroke=None))
    f.append(line(x0, y0 + h, x0 + w, y0 + h, INK, 1))
    f.append(line(x0, y0, x0, y0 + h, INK, 1))
    lo, hi = 0.42, 0.70
    def px(phi): return x0 + (phi - lo) / (hi - lo) * w
    def py(v): return y0 + h - v * h
    # the v = 0.05 recovery bar, for continuity with Figure 5
    f.append(line(x0, py(0.05), x0 + w, py(0.05), RED, 1, dash='3,2'))
    f.append(text(x0 + w + 3, py(0.05) + 3, 'v = 0.05', 7, RED, True))
    for nm, phi, v in POLAR:
        f.append(circ(px(phi), py(v), 4.2, fill=BLUE, stroke=WHITE, lw=1))
        f.append(text(px(phi), py(v) - 8, nm, 7, MUTED, anchor='middle'))
    f.append(text(x0 + w / 2, y0 + h + 17, L['f6x'], 8.5, MUTED, anchor='middle'))
    f.append(text(x0 - 8, y0 + 6, '1.0', 7.5, MUTED, anchor='end'))
    f.append(text(x0 - 8, y0 + h, '0', 7.5, MUTED, anchor='end'))
    for i, ln in enumerate(wrap(L['f6y'], 8, 74)):
        f.append(text(x0 - 12, y0 + h / 2 - 10 + i * 10, ln, 8, MUTED, anchor='end'))
    f.append(text(x0 + 6, y0 + 12, L['f6stat'], 9, GREEN, True))
    for i, ln in enumerate(wrap(L['f6cap'], 8, FW)):
        f.append(text(0, y0 + h + 34 + i * 10.5, ln, 8, MUTED))
    return f, FW, H

FIGS = [('fig1_aggregation', fig_fibril), ('fig2_predictor', fig_profile),
        ('fig3_circularity', fig_circ), ('fig4_statistic', fig_stat),
        ('fig5_results', fig_results), ('fig6_polarity', fig_polarity)]

# ============================================================================= LAYOUT
PW, PH = 595.28, 841.89
ML, MR, MT, MB = 62, 62, 64, 58
COLW = PW - ML - MR


def build(blocks, L, outpdf, title):
    pages, p = [], Page()
    y = PH - MT
    pageno = [1]

    def newpage():
        nonlocal p, y
        p.text(PW - MR, MB - 26, '%d' % pageno[0], 8, MUTED)
        pages.append(p)
        p = Page()
        pageno[0] += 1
        y = PH - MT

    for b in blocks:
        kind = b[0]
        if kind == 'title':
            for i, ln in enumerate(wrap(b[1], 21, COLW, True)):
                p.text(ML, y, ln, 21, INK, True)
                y -= 26
            y -= 4
            for ln in wrap(b[2], 10.5, COLW):
                p.text(ML, y, ln, 10.5, MUTED)
                y -= 14
            y -= 10
            p.figure([rect(0, 0, COLW, 2, fill=BLUE, stroke=None)], ML, y)
            y -= 18
        elif kind == 'h':
            if y < MB + 90:
                newpage()
            y -= 10
            for ln in wrap(b[1], 13, COLW, True):
                p.text(ML, y, ln, 13, BLUE, True)
                y -= 17
            y -= 4
        elif kind == 'p':
            lines = wrap(b[1], 10, COLW)
            if y - len(lines) * 14 < MB:
                newpage()
            for ln in lines:
                p.text(ML, y, ln, 10, INK)
                y -= 14
            y -= 7
        elif kind == 'b':
            for item in b[1]:
                lines = wrap(item, 10, COLW - 16)
                if y - len(lines) * 14 < MB:
                    newpage()
                p.figure([circ(3, 4, 2.2, fill=BLUE, stroke=None)], ML + 2, y + 7)
                for j, ln in enumerate(lines):
                    p.text(ML + 16, y, ln, 10, INK)
                    y -= 14
                y -= 3
            y -= 5
        elif kind == 'note':
            lines = wrap(b[1], 9.5, COLW - 26)
            hgt = len(lines) * 13 + 18
            if y - hgt < MB:
                newpage()
            p.figure([rect(0, 0, COLW, hgt, fill=(0.97, 0.97, 0.98), stroke=None, rx=4),
                      rect(0, 0, 3, hgt, fill=WARM, stroke=None)], ML, y + 4)
            yy = y - 8
            for ln in lines:
                p.text(ML + 14, yy, ln, 9.5, INK)
                yy -= 13
            y -= hgt + 12
        elif kind == 'fig':
            fig, w, h = b[1]
            if y - h - 10 < MB:
                newpage()
            p.figure(fig, ML, y)
            y -= h + 16
    p.text(PW - MR, MB - 26, '%d' % pageno[0], 8, MUTED)
    pages.append(p)
    return write_pdf(outpdf, pages, title)


# ============================================================================ CONTENT
def content(L, figs):
    return [
        ('title', L['title'], L['sub']),
        ('p', L['lead']),
        ('h', L['h1']),
        ('p', L['p1']), ('fig', figs[0]), ('p', L['p2']),
        ('h', L['h2']),
        ('p', L['p3']), ('fig', figs[1]), ('p', L['p4']),
        ('h', L['h3']),
        ('p', L['p5']), ('b', L['b1']), ('p', L['p6']),
        ('h', L['h4']),
        ('p', L['p7']), ('fig', figs[2]), ('p', L['p8']),
        ('note', L['n1']),
        ('h', L['h5']),
        ('p', L['p9']), ('fig', figs[3]), ('p', L['p10']), ('note', L['p10b']),
        ('h', L['h6']),
        ('p', L['p11']), ('fig', figs[4]), ('p', L['p12']), ('b', L['b2']),
        ('note', L['n2']),
        ('h', L['h7']),
        ('p', L['p13']), ('b', L['b3']),
        ('h', L['h8']),
        ('p', L['p14']), ('fig', figs[5]), ('p', L['p15']),
        ('note', L['n4']),
        ('note', L['n3']),
        ('h', L['h9']),
        ('b', L['gloss']),
    ]


EN = {
    'title': 'Can software find the sticky parts of a protein?',
    'sub': 'A benchmark of protein-aggregation predictors against regions that experiments '
           'have actually mapped. Written for undergraduates: no background assumed beyond '
           'first-year biology.',
    'lead': 'Some proteins clump together into long, ordered fibres. When this happens in '
            'the brain it is associated with disease. For decades, software has tried to '
            'predict which part of a protein sequence will do the clumping. This project '
            'asks a narrow, checkable question: when experiments have already mapped the '
            'region that matters, does the software find it?',
    'h1': '1. What is protein aggregation?',
    'p1': 'A protein is a chain of amino acids that normally folds into a specific shape. '
          'Sometimes it misfolds, exposing surfaces that are meant to be buried. Those '
          'surfaces stick to the same surfaces on other copies of the protein, and the '
          'copies stack into a fibril: a long, regular, highly stable fibre. Only part of '
          'the chain usually forms the rigid core of the fibril. That part is what we call '
          'the aggregation-critical region.',
    'f1t': 'Figure 1. From a working protein to a fibril',
    'f1a': 'folded and working',
    'f1b': 'misfolded, sticky surface exposed',
    'f1c': 'copies stack into a fibril',
    'p2': 'Two proteins drive this project: DISC1 and TRIOBP-1, both linked to '
          'schizophrenia. Experiments on them have narrowed the aggregation down to '
          'specific stretches of residues. Those experimental answers are what the '
          'software has to reproduce.',
    'h2': '2. What does a predictor actually do?',
    'p3': 'An aggregation predictor reads the amino-acid sequence and gives every position '
          'a score: how likely is this spot to drive aggregation? Older tools (roughly '
          '2004 to 2010) compute the score from physical chemistry, mostly how water-'
          'repelling the residues are and how well they would form a flat beta sheet. '
          'Newer tools learn the score from databases of known examples using machine '
          'learning. Either way the output is a curve along the sequence.',
    'f2t': 'Figure 2. What a predictor outputs, and how it can be wrong',
    'f2x': 'position along the protein sequence',
    'f2y1': 'high', 'f2y0': 'low',
    'f2reg': 'region the experiment mapped',
    'f2peak': "predictor's highest peak",
    'f2cap': 'Schematic, not real data. The predictor is not silent; it is confident about',
    'f2cap2': 'the wrong place. That is why "did it score the region highly?" is the wrong question.',
    'p4': 'The failure mode that matters is not a flat, silent prediction. It is a '
          'confident prediction in the wrong place. So the test cannot simply ask whether '
          'the mapped region got a high score. It has to ask whether the mapped region '
          'scored higher than the rest of the same protein.',
    'h3': '3. The question this project asks',
    'p5': 'Both of the papers that mapped these regions reported that the predictors of '
          'their day missed them. That is already published, and we do not re-establish '
          'it. The open question is about the current generation:',
    'b1': ['Do modern machine-learning predictors recover the experimentally mapped '
           'regions that the 2004-2010 generation missed?',
           'If they do not, what structural feature are they all missing?'],
    'p6': 'The second question is the interesting one, and it only becomes answerable if '
          'the first answer is no.',
    'h4': '4. The trap: three ways to fool yourself',
    'p7': 'Benchmarking predictors is unusually easy to get wrong, because the thing you '
          'are testing may have been involved in producing the answer you are testing it '
          'against. There are three distinct versions of this problem, and they are '
          'independent of one another.',
    'f3t': 'Figure 3. Three kinds of circularity, each tracked separately',
    'f3a': 'Discovery', 'f3a1': 'Was a predictor used to find the region in the first '
                                'place? If a predicted segment was deleted and the deletion '
                                'worked, that region cannot test that predictor.',
    'f3b': 'Agreement', 'f3b1': 'Do experiment and prediction already agree? Regions that '
                                'are easy to map are often the classic motifs predictors '
                                'were built to find. Those cannot separate good tools from bad.',
    'f3c': 'Training set', 'f3c1': 'Is the protein in the database the modern tool was '
                                   'trained on? If so, a hit may be memory rather than '
                                   'prediction.',
    'p8': 'Every row of our dataset carries a label for each of the three. Rows that fail '
          'one are kept and labelled, never silently deleted, because a reader must be able '
          'to see what was excluded and why.',
    'n1': 'A fourth column matters as much: which construct established the region. A '
          'region can be necessary in one protein fragment and dispensable in another, and '
          'both results can be correct. A benchmark that ignores this is scoring against a '
          'moving target.',
    'h5': '5. How we score an answer',
    'p9': 'We cut the whole protein into non-overlapping windows of six residues, score '
          'each window, and rank them. Then we ask: of all the windows in this protein, how '
          'well did the ones inside the experimentally mapped region do? If the region '
          'contains m windows and P is the chance that a randomly chosen window beats them, '
          'the score is v = 1 - P to the power m. A small v means the region stood out.',
    'f4t': 'Figure 4. Scoring a region against the rest of its own protein',
    'f4prot': 'the protein, cut into 6-residue windows',
    'f4reg': 'the mapped region',
    'f4rank': 'the same windows, sorted by predicted score',
    'f4form': 'v = 1 - P^m        small v = the region stood out',
    'f4cap': 'The green windows are inside the mapped region. If they sit at the left-hand '
             'end after sorting, the predictor found the region. Here they are scattered, '
             'so it did not.',
    'p10': 'The threshold was fixed in writing before any software was run: a region counts '
           'as recovered if v is below 0.05. Choosing that number afterwards, once the '
           'scores are visible, would produce a result that looks convincing and means '
           'nothing. Writing it down first, however, does not make it a good threshold -- '
           'see the note below.',
    'p10b': 'And on 18 November 2026 it turned out not to be one. Because v is built from a '
            'ranking, there is a smallest value it can possibly take, and that smallest '
            'value depends on how long the protein is and how long the region is. For 9 of '
            'our 23 scored regions that floor sits ABOVE 0.05, so a perfect predictor -- '
            'one that ranked the region top of the whole protein -- would still be scored '
            'as having failed. For those regions the threshold can never fire, and "the '
            'predictor missed it" is true before any software runs. This was arithmetic we '
            'could have done on day one, and we did not. It is recorded here rather than '
            'quietly repaired, because a reader deserves to know which of our numbers mean '
            'something.',
    'h6': '6. What we have found so far',
    'p11': 'Two tools have been run on every region we could score: TANGO, from the older '
           'generation, and AggrescanAI, a recent machine-learning tool. The bars below are '
           'real results, not illustrations.',
    'f5t': 'Figure 5. Both tools, nine regions. Lower is better.',
    'f5y': 'v (lower = found it)',
    'f5bar': 'v = 0.05',
    'f5leg1': 'TANGO (older generation)',
    'f5leg2': 'AggrescanAI (modern)',
    'f5cap': 'Only two bars in the whole chart fall below the dashed line. On seven of the '
             'nine regions the modern tool scores worse than the older one.',
    'p12': 'Read plainly:',
    'b2': ['Neither tool reliably recovers these regions.',
           'On 7 of 9 regions the modern tool does worse than the older one.',
           'The difference is not statistically significant: p = 0.10, which is not '
           'evidence that the older tool is better either.'],
    'n2': 'The honest summary is that nothing is established yet. The part of the dataset '
          'that can settle the question properly held just two regions for most of this '
          'work, and with two pairs the smallest p-value the test can possibly produce is '
          '0.25 -- no data could have passed the threshold. Three regions were added on 18 '
          'November 2026, taking it to five and giving a result of p = 0.38: still nothing, '
          'but for the first time a real test rather than an impossible one. Two of those '
          'three regions come from proteins so similar that they count as one measurement, '
          'and all three sit in the group whose threshold can never fire. That is a flaw in '
          'our own design, found by running it rather than by reading it, and it is '
          'recorded rather than quietly patched.',
    'h7': '7. Why we write the rules down first',
    'p13': 'The statistic, the threshold and the way regions are selected were all written '
           'down and committed before any predictor was run. This is called '
           'pre-registration, and it exists because of a simple human tendency: if you look '
           'at the results first and choose the test afterwards, you will choose the test '
           'that works. Doing it in this order has already cost us results we would have '
           'liked to keep:',
    'b3': ['Four defects in our own plan were found by executing it, including one where '
           'the answer changes depending on where you start cutting the windows.',
           'Several regions could have been moved into the main analysis late, which would '
           'have raised the sample size from 2 to 8 - but the rules say the labels must be '
           'fixed before the modern tool is run, and they were not, so those regions are '
           'reported separately.',
           'Applying that rule did not help our hypothesis in any case. It made the '
           'negative result stronger.'],
    'h8': '8. What happens next',
    'p14': 'The bottleneck is not the software; it is the number of independent, '
           'well-mapped regions that are clean on all three kinds of circularity. We need '
           'about five new proteins. Meanwhile one lead has been tested. A recent structure '
           'of a soy protein has a fibril core held together partly by water-ATTRACTING '
           'contacts rather than water-repelling ones. Every predictor here is built on '
           'water-repelling chemistry, so a water-attracting core is exactly the case they '
           'should fail on. We wrote down how to measure that, and the threshold for '
           'abandoning the measure, before computing anything.',
    'f6t': 'Figure 6. The polar-core result, on seven structurally solved proteins',
    'f6x': 'how polar the buried core is  (0 = all water-repelling, 1 = all water-attracting)',
    'f6y': 'v  (lower = the predictor found it)',
    'f6stat': 'rho = +0.82,  p = 0.017',
    'f6cap': 'Each point is one protein whose fibril structure has been solved, so its core '
             'can be measured rather than guessed. The more polar the core, the worse the '
             'predictor does. Real data; the statistic was fixed before it was computed.',
    'p15': 'The measure had to pass a test first: it was required to reproduce, from raw '
           'coordinates, a published classification of twelve other fibril structures - and '
           'we committed in advance to abandoning it if it did not. It passed. Then, across '
           'seven proteins, the more polar the core, the worse the modern predictor did '
           '(correlation +0.82, p = 0.017). That is the first prediction this project made '
           'in advance and then confirmed.',
    'n4': 'Two honest qualifications. The result is fragile: remove any one of four of the '
          'seven proteins and it slips just past the threshold. And it does not answer the '
          'main question, because the two proteins the project was built around have never '
          'had their fibrils solved, so they are not in this figure at all. There is also a '
          'sense in which the finding is half obvious - a tool that scores water-repelling '
          'chemistry will of course score water-attracting cores low. The half that is not '
          'obvious is that those cores drive real aggregation in the laboratory anyway. The '
          'tools are not wrong about chemistry; they are wrong about what nature does with '
          'it.',
    'h9': 'Glossary',
    'gloss': ['Residue - one amino acid within the protein chain.',
              'Fibril - the ordered, stacked fibre that aggregated protein forms.',
              'Aggregation-critical region - the stretch of sequence that experiments show '
              'drives the aggregation.',
              'Circularity - testing a tool using an answer that the tool itself helped to '
              'produce.',
              'Pre-registration - fixing the analysis in writing before seeing any results.',
              'v - our score for one region: small means the predictor ranked that region '
              'above the rest of the same protein.'],
    'n3': 'The dataset behind this document is published openly and has its own DOI, so '
          'anyone can check the rows, the labels and the reasoning for themselves. Each row '
          'records which paper it came from and whether someone actually opened that paper.',
}

FR = {
    'title': "Un logiciel peut-il trouver les régions collantes d'une protéine ?",
    'sub': "Une évaluation comparative des prédicteurs d'agrégation des protéines face aux "
           "régions réellement cartographiées par l'expérience. Écrit pour des étudiants de "
           "licence : aucun prérequis au-delà de la biologie de première année.",
    'lead': "Certaines protéines s'agglomèrent en longues fibres ordonnées. Lorsque cela se "
            "produit dans le cerveau, le phénomène est associé à la maladie. Depuis des "
            "décennies, des logiciels tentent de prédire quelle partie d'une séquence "
            "protéique provoquera cette agglomération. Ce projet pose une question étroite "
            "et vérifiable : lorsque l'expérience a déjà cartographié la région qui compte, "
            "le logiciel la retrouve-t-il ?",
    'h1': "1. Qu'est-ce que l'agrégation des protéines ?",
    'p1': "Une protéine est une chaîne d'acides aminés qui se replie normalement en une "
          "forme précise. Il arrive qu'elle se replie mal, exposant des surfaces qui "
          "devraient rester enfouies. Ces surfaces adhèrent aux mêmes surfaces d'autres "
          "copies de la protéine, et les copies s'empilent en une fibrille : une fibre "
          "longue, régulière et très stable. En général, seule une partie de la chaîne "
          "forme le coeur rigide de la fibrille. C'est ce que nous appelons la région "
          "critique pour l'agrégation.",
    'f1t': "Figure 1. D'une protéine fonctionnelle à une fibrille",
    'f1a': "repliée et fonctionnelle",
    'f1b': "mal repliée, surface collante exposée",
    'f1c': "les copies s'empilent en fibrille",
    'p2': "Deux protéines sont au coeur du projet : DISC1 et TRIOBP-1, toutes deux liées à "
          "la schizophrénie. Les expériences menées sur elles ont réduit l'agrégation à des "
          "segments précis de résidus. Ce sont ces réponses expérimentales que le logiciel "
          "doit reproduire.",
    'h2': "2. Que fait réellement un prédicteur ?",
    'p3': "Un prédicteur d'agrégation lit la séquence d'acides aminés et attribue à chaque "
          "position un score : quelle est la probabilité que cet endroit déclenche "
          "l'agrégation ? Les outils anciens (environ 2004 à 2010) calculent ce score à "
          "partir de la chimie physique, surtout le caractère hydrophobe des résidus et "
          "leur aptitude à former un feuillet bêta plat. Les outils récents apprennent le "
          "score à partir de bases de données d'exemples connus, par apprentissage "
          "automatique. Dans les deux cas, le résultat est une courbe le long de la séquence.",
    'f2t': "Figure 2. Ce que produit un prédicteur, et comment il peut se tromper",
    'f2x': "position le long de la séquence protéique",
    'f2y1': "élevé", 'f2y0': "faible",
    'f2reg': "région cartographiée",
    'f2peak': "pic le plus élevé du prédicteur",
    'f2cap': "Schéma, pas des données réelles. Le prédicteur n'est pas muet : il est sûr de lui,",
    'f2cap2': "mais au mauvais endroit. D'où l'inutilité de la question « a-t-il donné un score élevé ? »",
    'p4': "Le mode d'échec qui compte n'est pas une prédiction plate et silencieuse. C'est "
          "une prédiction assurée au mauvais endroit. Le test ne peut donc pas se contenter "
          "de demander si la région cartographiée a reçu un score élevé. Il doit demander "
          "si elle a obtenu un meilleur score que le reste de la même protéine.",
    'h3': "3. La question posée par ce projet",
    'p5': "Les deux articles qui ont cartographié ces régions signalent que les prédicteurs "
          "de leur époque les avaient manquées. C'est déjà publié, et nous ne le "
          "ré-établissons pas. La question ouverte concerne la génération actuelle :",
    'b1': ["Les prédicteurs modernes, fondés sur l'apprentissage automatique, retrouvent-ils "
           "les régions cartographiées que la génération 2004-2010 avait manquées ?",
           "Si ce n'est pas le cas, quelle caractéristique structurale leur échappe à tous ?"],
    'p6': "La seconde question est la plus intéressante, et elle ne devient abordable que "
          "si la réponse à la première est négative.",
    'h4': "4. Le piège : trois façons de se tromper soi-même",
    'p7': "Évaluer des prédicteurs est particulièrement facile à rater, car l'outil testé a "
          "parfois contribué à produire la réponse qui sert de référence. Ce problème "
          "existe sous trois formes distinctes et indépendantes.",
    'f3t': "Figure 3. Trois formes de circularité, suivies séparément",
    'f3a': "Découverte", 'f3a1': "Un prédicteur a-t-il servi à trouver la région ? Si un "
                                 "segment prédit a été supprimé et que la suppression a "
                                 "fonctionné, cette région ne peut pas tester ce prédicteur.",
    'f3b': "Accord", 'f3b1': "Expérience et prédiction concordent-elles déjà ? Les régions "
                             "faciles à cartographier sont souvent les motifs classiques que "
                             "les outils ont été conçus pour trouver.",
    'f3c': "Apprentissage", 'f3c1': "La protéine figure-t-elle dans la base ayant servi à "
                                    "entraîner l'outil moderne ? Si oui, un succès peut "
                                    "relever de la mémoire et non de la prédiction.",
    'p8': "Chaque ligne de notre jeu de données porte une étiquette pour chacune des trois. "
          "Les lignes qui échouent à l'un des critères sont conservées et étiquetées, jamais "
          "supprimées en silence : un lecteur doit pouvoir voir ce qui a été exclu et pourquoi.",
    'n1': "Une quatrième colonne compte tout autant : quelle construction a établi la "
          "région. Une région peut être nécessaire dans un fragment de protéine et "
          "dispensable dans un autre, et les deux résultats peuvent être exacts. Une "
          "évaluation qui ignore cela vise une cible mouvante.",
    'h5': "5. Comment nous notons une réponse",
    'p9': "Nous découpons la protéine entière en fenêtres de six résidus sans "
          "chevauchement, nous notons chaque fenêtre et nous les classons. Puis nous "
          "demandons : parmi toutes les fenêtres de cette protéine, comment se sont "
          "comportées celles situées dans la région cartographiée ? Si la région contient m "
          "fenêtres et que P est la probabilité qu'une fenêtre tirée au hasard les dépasse, "
          "le score vaut v = 1 - P puissance m. Un v faible signifie que la région s'est "
          "démarquée.",
    'f4t': "Figure 4. Noter une région face au reste de sa propre protéine",
    'f4prot': "la protéine, découpée en fenêtres de 6 résidus",
    'f4reg': "la région cartographiée",
    'f4rank': "les mêmes fenêtres, triées par score prédit",
    'f4form': "v = 1 - P^m        v faible = la région s'est démarquée",
    'f4cap': "Les fenêtres vertes sont dans la région cartographiée. Si elles se placent à "
             "gauche après le tri, le prédicteur a trouvé la région. Ici elles sont "
             "dispersées : il ne l'a pas trouvée.",
    'p10': "Le seuil a été fixé par écrit avant toute exécution de logiciel : une région "
           "est considérée comme retrouvée si v est inférieur à 0,05. Choisir ce nombre "
           "après coup, une fois les scores visibles, produirait un résultat convaincant en "
           "apparence et vide de sens. Mais l'écrire d'abord n'en fait pas pour autant un "
           "bon seuil — voir la note ci-dessous.",
    'p10b': "Et le 18 novembre 2026, il s'est avéré que ce n'en était pas un. Comme v est "
            "construit à partir d'un classement, il existe une valeur minimale qu'il peut "
            "atteindre, et cette valeur dépend de la longueur de la protéine et de celle de "
            "la région. Pour 9 de nos 23 régions notées, ce plancher se situe AU-DESSUS de "
            "0,05 : un prédicteur parfait — qui classerait la région en tête de toute la "
            "protéine — serait malgré tout compté comme ayant échoué. Pour ces régions, le "
            "seuil ne peut jamais se déclencher, et « le prédicteur l'a manquée » est vrai "
            "avant même qu'un logiciel ne s'exécute. C'était un calcul que nous aurions pu "
            "faire dès le premier jour, et nous ne l'avons pas fait. Il est consigné ici "
            "plutôt que réparé discrètement, car un lecteur mérite de savoir lesquels de nos "
            "chiffres ont un sens.",
    'h6': "6. Ce que nous avons trouvé jusqu'ici",
    'p11': "Deux outils ont été appliqués à toutes les régions que nous pouvions noter : "
           "TANGO, de l'ancienne génération, et AggrescanAI, un outil récent "
           "d'apprentissage automatique. Les barres ci-dessous sont des résultats réels, non "
           "des illustrations.",
    'f5t': "Figure 5. Deux outils, neuf régions. Plus bas vaut mieux.",
    'f5y': "v (plus bas = trouvée)",
    'f5bar': "v = 0,05",
    'f5leg1': "TANGO (ancienne génération)",
    'f5leg2': "AggrescanAI (moderne)",
    'f5cap': "Seules deux barres de tout le graphique passent sous la ligne pointillée. Sur "
             "sept des neuf régions, l'outil moderne fait moins bien que l'ancien.",
    'p12': "En clair :",
    'b2': ["Aucun des deux outils ne retrouve ces régions de manière fiable.",
           "Sur 7 des 9 régions, l'outil moderne fait moins bien que l'ancien.",
           "L'écart n'est pas statistiquement significatif : p = 0,10, ce qui ne prouve pas "
           "non plus que l'ancien outil soit meilleur."],
    'n2': "Le résumé honnête est que rien n'est encore établi. La partie du jeu de données "
          "capable de trancher proprement n'a contenu que deux régions pendant l'essentiel "
          "de ce travail, et avec deux paires la plus petite valeur de p que le test puisse "
          "produire est 0,25 : aucune donnée n'aurait pu franchir le seuil. Trois régions "
          "ont été ajoutées le 18 novembre 2026, la portant à cinq, pour un résultat de "
          "p = 0,38 : toujours rien, mais pour la première fois un vrai test plutôt qu'un "
          "test impossible. Deux de ces trois régions proviennent de protéines si "
          "semblables qu'elles comptent pour une seule mesure, et toutes trois appartiennent "
          "au groupe dont le seuil ne peut jamais se déclencher. C'est un défaut de notre "
          "propre protocole, découvert en l'exécutant plutôt qu'en le lisant, et il est "
          "consigné plutôt que corrigé discrètement.",
    'h7': "7. Pourquoi nous écrivons les règles d'abord",
    'p13': "La statistique, le seuil et le mode de sélection des régions ont tous été écrits "
           "et enregistrés avant toute exécution de prédicteur. Cela s'appelle le "
           "pré-enregistrement, et cela existe à cause d'une tendance humaine simple : si "
           "l'on regarde d'abord les résultats et que l'on choisit le test ensuite, on "
           "choisira le test qui fonctionne. Procéder dans cet ordre nous a déjà coûté des "
           "résultats que nous aurions aimé garder :",
    'b3': ["Quatre défauts de notre propre protocole ont été découverts en l'exécutant, dont "
           "un où la réponse change selon l'endroit où l'on commence à découper les fenêtres.",
           "Plusieurs régions auraient pu rejoindre tardivement l'analyse principale, ce qui "
           "aurait porté l'effectif de 2 à 8 ; mais les règles exigent que les étiquettes "
           "soient fixées avant l'exécution de l'outil moderne, ce qui n'a pas été fait. Ces "
           "régions sont donc rapportées séparément.",
           "De toute façon, appliquer cette règle n'a pas aidé notre hypothèse : le résultat "
           "négatif en est sorti renforcé."],
    'h8': "8. La suite",
    'p14': "Le goulot d'étranglement n'est pas le logiciel, mais le nombre de régions "
           "indépendantes, bien cartographiées et indemnes des trois formes de circularité. "
           "Il nous faut environ cinq nouvelles protéines. Entre-temps, une piste a été "
           "testée. Une structure récente d'une protéine de soja possède un coeur de "
           "fibrille maintenu en partie par des contacts HYDROPHILES plutôt qu'hydrophobes. "
           "Or tous les prédicteurs étudiés reposent sur la chimie hydrophobe : un coeur "
           "hydrophile est donc exactement le cas où ils devraient échouer. Nous avons écrit "
           "comment le mesurer, et à quelle condition abandonner la mesure, avant de "
           "calculer quoi que ce soit.",
    'f6t': "Figure 6. Le résultat sur la polarité, pour sept protéines dont la structure est résolue",
    'f6x': "polarité du coeur enfoui  (0 = tout hydrophobe, 1 = tout hydrophile)",
    'f6y': "v  (plus bas = le prédicteur l'a trouvée)",
    'f6stat': "rho = +0,82,  p = 0,017",
    'f6cap': "Chaque point est une protéine dont la structure de la fibrille est résolue : "
             "son coeur peut donc être mesuré et non supposé. Plus le coeur est polaire, "
             "moins le prédicteur réussit. Données réelles ; la statistique a été fixée "
             "avant d'être calculée.",
    'p15': "La mesure devait d'abord passer un test : reproduire, à partir des coordonnées "
           "brutes, une classification publiée de douze autres structures de fibrilles - et "
           "nous nous étions engagés d'avance à l'abandonner si elle échouait. Elle a réussi. "
           "Ensuite, sur sept protéines, plus le coeur est polaire, moins le prédicteur "
           "moderne réussit (corrélation +0,82, p = 0,017). C'est la première prédiction que "
           "ce projet ait formulée à l'avance puis confirmée.",
    'n4': "Deux réserves honnêtes. Le résultat est fragile : retirez n'importe laquelle de "
          "quatre des sept protéines et il repasse juste au-dessus du seuil. Et il ne répond "
          "pas à la question principale, car les deux protéines autour desquelles le projet "
          "a été construit n'ont jamais eu de fibrille résolue : elles ne figurent donc pas "
          "sur cette figure. Il y a aussi un sens où le résultat est à moitié évident : un "
          "outil qui évalue la chimie hydrophobe donnera bien sûr un score faible aux coeurs "
          "hydrophiles. La moitié qui ne l'est pas, c'est que ces coeurs provoquent malgré "
          "tout une agrégation réelle en laboratoire. Les outils ne se trompent pas sur la "
          "chimie ; ils se trompent sur ce que la nature en fait.",
    'h9': "Glossaire",
    'gloss': ["Résidu - un acide aminé au sein de la chaîne protéique.",
              "Fibrille - la fibre ordonnée et empilée que forme la protéine agrégée.",
              "Région critique pour l'agrégation - le segment de séquence dont l'expérience "
              "montre qu'il provoque l'agrégation.",
              "Circularité - tester un outil à l'aide d'une réponse que l'outil lui-même a "
              "contribué à produire.",
              "Pré-enregistrement - fixer l'analyse par écrit avant de voir le moindre "
              "résultat.",
              "v - notre score pour une région : faible signifie que le prédicteur a classé "
              "cette région au-dessus du reste de la même protéine."],
    'n3': "Le jeu de données à l'origine de ce document est publié en libre accès et possède "
          "son propre DOI : chacun peut vérifier les lignes, les étiquettes et les "
          "raisonnements. Chaque ligne indique de quel article elle provient et si quelqu'un "
          "a réellement ouvert cet article.",
}


def main(outdir='docs'):
    os.makedirs(outdir, exist_ok=True)
    written = []
    for tag, L in (('en', EN), ('fr', FR)):
        figs = []
        for name, fn in FIGS:
            fig, w, h = fn(L)
            figs.append((fig, w, h))
            sp = os.path.join(outdir, '%s_%s.svg' % (name, tag))
            open(sp, 'w').write(svg_of(fig, w, h))
            written.append(sp)
        pdf = os.path.join(outdir, 'explainer_%s.pdf' % tag)
        n = build(content(L, figs), L, pdf, L['title'])
        written.append('%s (%d bytes)' % (pdf, n))
    for w in written:
        print('wrote', w)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else 'docs'))
