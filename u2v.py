#!/bin/env python3.11

import os, sys


MAX_24 = 16777215


os.system(("clear", "cls")[os.name ==  "nt"])


def detect_encoding_and_encode(sym, prev=None):
    if prev is not None:
        try:
            _sym, coding = sym.encode(prev), prev
            assert len(_sym) == 1
            return _sym, coding
        except:
            pass
    for cp in range(1, 65535):
        coding = f"cp{cp}"
        if coding == "cp0":
            coding = "ascii"
        try:
            _sym, coding = sym.encode(coding), coding
            assert len(_sym) == 1
            return _sym, coding
        except:
            continue
    else:
        print(f"Unsupported symbol: {repr(sym)}, fallback to unicode! and zero enpand up to 32 bits")
        _sym = sym.encode("utf-8")
        _sym = b"\x00"*(4-len(_sym)) + _sym
        _sym = b"\xff\xff\xff\xff" + _sym
        return _sym, (prev if prev is not None else "ascii")


with open("utf8.txt", "rt") as f:
    src = f.read()

dst = b""

latest = "ascii"

for _sym in src:
    sym, coding = detect_encoding_and_encode(_sym, latest)
    print(repr(_sym), latest, coding, ("switch" if coding != latest else "stay"), sym, sep="\t")
    if coding != latest:
        latest = coding
        dst += b"\xff"
        if coding == "ascii":
            dst += "\x00"*3
        else:
            dst += int(coding[2:]).to_bytes(3)
    dst += sym


with open("vute.txt", "wb") as f:
    f.write(dst)
