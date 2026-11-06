# -*- coding: utf-8 -*-
"""Cover the answers of a PDF with removable black box annotations.
MASK.pdf = the same document built with MASK=1 (answer areas painted pure red, identical layout).
usage: add_answer_boxes.py DOC.pdf MASK.pdf OUT.pdf"""
import sys
import numpy as np
import pypdf
import pypdfium2 as pdfium
from pypdf.annotations import Rectangle
from pypdf.generic import ArrayObject, FloatObject, NameObject, TextStringObject

DOC, MASK, OUT = sys.argv[1:4]
SC = 1.5  # render scale (108 dpi)
mask = pdfium.PdfDocument(MASK)
r = pypdf.PdfReader(DOC)
assert len(mask) == len(r.pages), "mask and document page counts differ"
w = pypdf.PdfWriter()
w.append(r)
total = 0
for pi in range(len(mask)):
    img = np.asarray(mask[pi].render(scale=SC).to_pil().convert("RGB")).astype(int)
    red = (img[:, :, 0] > 200) & (img[:, :, 1] < 90) & (img[:, :, 2] < 90)
    if not red.any():
        continue
    # runs per row, then union runs that touch vertically -> boxes
    parent, boxes, prev = {}, {}, []
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    nid = 0
    for y in range(red.shape[0]):
        row = red[y]
        if not row.any():
            prev = []
            continue
        d = np.diff(np.concatenate(([0], row.astype(int), [0])))
        starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
        cur = []
        for x0, x1 in zip(starts, ends):
            if x1 - x0 < 2:
                continue
            parent[nid] = nid
            boxes[nid] = [x0, y, x1, y + 1]
            for (px0, px1, pid) in prev:
                if px0 < x1 and x0 < px1:
                    a, b = find(pid), find(nid)
                    if a != b:
                        parent[b] = a
            cur.append((x0, x1, nid))
            nid += 1
        prev = cur
    merged = {}
    for k, (x0, y0, x1, y1) in boxes.items():
        root = find(k)
        m = merged.setdefault(root, [x0, y0, x1, y1])
        m[0], m[1], m[2], m[3] = min(m[0], x0), min(m[1], y0), max(m[2], x1), max(m[3], y1)
    H = float(r.pages[pi].mediabox.height)
    for x0, y0, x1, y1 in merged.values():
        if (x1 - x0) * (y1 - y0) < 20:
            continue
        rect = (x0 / SC - 0.6, H - y1 / SC - 0.6, x1 / SC + 0.6, H - y0 / SC + 0.6)
        a = Rectangle(rect=rect, interior_color="000000")
        a[NameObject("/C")] = ArrayObject([FloatObject(0), FloatObject(0), FloatObject(0)])
        a[NameObject("/T")] = TextStringObject("جواب")
        w.add_annotation(page_number=pi, annotation=a)
        total += 1
w.write(OUT)
print(total, "boxes ->", OUT)
