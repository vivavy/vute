# VCP - Variable Code Pages

VCP is a variable code page, that is a set of code points that can be used to
encode a text in a way that is more efficient than using a single code page.

## How it works

To use codes out of ASCII range, you must select your code page first. You can
select a code page by using the special symbol negative-one, in python:

```python
b"\xff"  # <- this is a byte with value 255, or -1 in byte range
```

next you need to put 24-bit code page number in big-endian format, for example:

```python
b"\xff\x00\x03\x62"  # <- this is a VCP selector for cp866
```

Now, you can use any code point from this code page, for example `b"\x9A"` is `Ъ` in cp866.

also you can store a VCP in _stack_ and use it later, for example:

```python
(
    b"\xff\x00\x03\x62"  # <- this is a VCP selector for cp866
    b"\x9A"              # <- symbol `Ъ` in cp866
    b"\xfe"              # <- push VCP to stack
    b"\xff\x00\x00\x00"  # <- this is a VCP selector for ASCII
    b"\x20"              # <- space in ASCII
    b"\xfd"              # <- pop VCP from stack
    b"\x9A"              # <- symbol `Ъ` in cp866
)
```

IT can be useful if if most of your text is in one code page, and you need to
encode some text parts in another code page, for example, if you writes a russian text
in cp1251, and you need to paste some english parts in ASCII.

## All* symbols in VUTE is 1-character long and encoding has backward compatibility with cpXXXX

* Exception are symbols that cannot be encoded using CP range, they are fallbacks to UTF-8 with zero-expanding up to 24 bits (but first byte must be zero)

VUTE is a text encoding that uses only one character to represent a code point, so it is very compact.
Also it uses already defined code pages, so if sofware doesn't support VUTE - the most of text will not be corrupted.
As VUTE uses 24 bits to represent a code page number, you can use a really huge range of symbols (to be correct, it is 4\`294\`967\`296, not bad, really?).
