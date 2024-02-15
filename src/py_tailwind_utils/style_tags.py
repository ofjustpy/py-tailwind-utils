import sys

from .common import TagBase


class _boxshadow(TagBase):
    tagstr = "shadow-{val}"
    tagops = []
    taghelp = "shadow"
    elabel = "boxshadow"
    stemval = "shadow"

boxshadow = _boxshadow()


# support bd/None to simply output borderTo
class _bd(TagBase):
    tagstr = "border-{val}"
    tagops = []
    taghelp = "border value"
    elabel = "bd"
    stemval = "border"


bd = _bd()

class _priority(TagBase):
    tagstr = "!{val}"
    tagops = []
    taghelp = "priority"
    elabel = "priority"
    stemval = "!"


priority = _priority()


class _from(TagBase):
    tagstr = "from-{val}"
    tagops = []
    taghelp = "gradient from color"
    elabel = "from"
    stemval = "from"


from_ = _from()


class _to(TagBase):
    tagstr = "to-{val}"
    tagops = []
    taghelp = "gradient to color"
    elabel = "to"
    stemval = "to"


to_ = _to()


class _via(TagBase):
    tagstr = "via-{val}"
    tagops = []
    taghelp = "gradient via color"
    elabel = "via"
    stemval = "via"


via_ = _via()


class _twpx(TagBase):
    tagstr = "px"
    tagops = []
    taghelp = "px"
    elabel = "px"
    stemval = "px"


twpx = _twpx()


class _cc(TagBase):
    tagstr = ""
    tagops = []
    taghelp = "comment out"
    elabel = "cc"
    stemval = None


cc = _cc()


_tw_keywords = [
    "container",
    "inherit",
    "current",
    "transparent",
    "first",
    "full",
    "screen",
    "hidden",
    "last",
    "none",
    "scroll",
    "span",
    "text",
    "visible",
    "auto",
    "group",
    "double",
    "clip",
    "invisible",
    "absolute",
    "grow",
    "peer",
    "contain",
    "reverse",
    "spacing"
    
]

for kw in _tw_keywords:
    globals()[f"_{kw}"] = type(
        f"_{kw}",
        (TagBase,),
        {"tagstr": kw, "tagops": [], "taghelp": kw, "elabel": kw, "stemval": kw},
    )

    globals()[kw] = globals()[f"_{kw}"]()


_tw_keywords_val = [
    "bg",
    "x",
    "y",
    "duration",
    "inset",
    "max",
    "min",
    "offset",
    "opacity",
    "order",
    "ring",
    "row",
    "rows",
    "col",
    "cols",
    "space",
    "span",
    "stroke",
    "gap",
    "outline",
    "underline",
    "divide",
    "rotate",
    "shrink",
    "translate",
    "gradient",
    "to",
    "rounded",
    "scale",
    "basis",
    "columns",
    "grayscale",
    "size",
    "indent"
    
]
for kw in _tw_keywords_val:
    globals()[f"_{kw}"] = type(
        f"_{kw}",
        (TagBase,),
        {
            "tagstr": f"{kw}-{{val}}",
            "tagops": [],
            "taghelp": kw,
            "elabel": kw,
            "stemval": kw,
        },
    )

    globals()[kw] = globals()[f"_{kw}"]()


class _end(TagBase):
    tagstr = "end{val}"
    tagops = []
    taghelp = "end"
    elabel = "end"
    stemval = "end"


end = _end()

class _ul(TagBase):
    tagstr = "underline"
    tagops = []
    taghelp = "underline"
    elabel = "underline"
    stemval = "underline"


ul = _ul()


class _fc(TagBase):
    tagstr = "text-{val}"
    tagops = []
    taghelp = "font color"
    elabel = "fc"
    stemval = "text"


fc = _fc()


class _G(TagBase):
    tagstr = "grid-{val}"
    tagops = []
    taghelp = "grid"
    elabel = "G"
    stemval = "grid"


G = _G()


class _H(TagBase):
    tagstr = "h-{val}"
    tagops = ["screen"]
    taghelp = "height"
    elabel = "H"
    stemval = "h"


H = _H()
# TODO: limit H to its domain


class _lh(TagBase):
    tagstr = "leading-{val}"
    tagops = []
    taghelp = "lineheight"
    elabel = "lh"
    stemval = "leading"


lh = _lh()


class _mr(TagBase):
    tagstr = "m{val}"
    tagops = {}
    taghelp = "margin"
    elabel = "mr"
    stemval = "m"


mr = _mr()


# class _ovf(TagBase):
#     tagstr = "overflow-{val}"
#     tagops = []
#     taghelp = "overflow"
#     elabel = "ovf"
#     stemval = "overflow"


# ovf = _ovf()


class _pd(TagBase):
    tagstr = "p{val}"
    tagops = {}
    taghelp = "padding"
    elabel = "pd"
    stemval = "p"


pd = _pd()


class _ph(TagBase):
    tagstr = "placeholder-{val}"
    tagops = []
    taghelp = "placeholder"
    elabel = "ph"
    stemval = "placeholder"


ph = _ph()


class _resize(TagBase):
    tagstr = "resize-{val}"
    tagops = []
    taghelp = "resize"
    elabel = "resize"
    stemval = "resize"


resize = _resize()


class _sb(TagBase):
    tagstr = "b-{val}"
    tagops = []
    taghelp = "rounded border: side bottom"
    elabel = "sb"
    stemval = "b"


sb = _sb()


class _sl(TagBase):
    tagstr = "l-{val}"
    tagops = []
    taghelp = "rounded border: side left"
    elabel = "sl"
    stemval = "l"


sl = _sl()


class _sr(TagBase):
    tagstr = "r-{val}"
    tagops = []
    taghelp = "rounded border: side right"
    elabel = "sr"
    stemval = "r"


sr = _sr()


class _st(TagBase):
    tagstr = "t-{val}"
    tagops = []
    taghelp = "rounded border: side top"
    elabel = "st"
    stemval = "t"


st = _st()


class _ss(TagBase):
    "side start based on text direction"
    tagstr = "s-{val}"
    tagops = []
    taghelp = "RTL: side start"
    elabel = "ss"
    stemval = "s"


ss = _ss()

class _se(TagBase):
    "side start based on text direction"
    tagstr = "e-{val}"
    tagops = []
    taghelp = "RTL:side end"
    elabel = "se"
    stemval = "e"


se = _se()

class _sss(TagBase):
    "side start based on text direction"
    tagstr = "ss-{val}"
    tagops = []
    taghelp = "rounded border: top-start"
    elabel = "sss"
    stemval = "ss"


sss = _sss()


class _sse(TagBase):
    "side start based on text direction"
    tagstr = "se-{val}"
    tagops = []
    taghelp = "rounded border: top-end "
    elabel = "sse"
    stemval = "se"


sse = _sse()


class _ses(TagBase):
    "side start based on text direction"
    tagstr = "es-{val}"
    tagops = []
    taghelp = "rounded border: bottom-start"
    elabel = "ses"
    stemval = "es"


ses = _ses()


class _see(TagBase):
    "side start based on text direction"
    tagstr = "ee-{val}"
    tagops = []
    taghelp = "rounded border: bottom-end"
    elabel = "see"
    stemval = "ee"


see = _see()




class _ctl(TagBase):
    tagstr = "tl-{val}"
    tagops = []
    taghelp = "ctl"
    elabel = "top-left"
    stemval = "tl"

ctl = _ctl()

class _ctr(TagBase):
    tagstr = "tr-{val}"
    tagops = []
    taghelp = "rounded border: top-right"
    elabel = "top-right"
    stemval = "tr"

ctr = _ctr()    
class _cbl(TagBase):
    tagstr = "bl-{val}"
    tagops = []
    taghelp = "rounded border: bottom-left"
    elabel = "cbl"
    stemval = "bl"

cbl = _cbl()

class _cbr(TagBase):
    tagstr = "br-{val}"
    tagops = []
    taghelp = "rounded border: bottom right"
    elabel = "cbr"
    stemval = "br"

cbr = _cbr()

class _np(TagBase):
    "negative prefix for margins"
    tagstr = "-{val}"
    tagops = []
    taghelp = "negative prefix"
    elabel = "np"
    stemval = "-"


np = _np()


class _top(TagBase):
    tagstr = "top-{val}"
    tagops = []
    taghelp = "top"
    elabel = "top"
    stemval = "top"


top = _top()


class _right(TagBase):
    tagstr = "right-{val}"
    tagops = []
    taghelp = "right"
    elabel = "right"
    stemval = "right"


right = _right()


class _bottom(TagBase):
    tagstr = "bottom-{val}"
    tagops = []
    taghelp = "bottom"
    elabel = "bottom"
    stemval = "bottom"


bottom = _bottom()


class _left(TagBase):
    tagstr = "left-{val}"
    tagops = []
    taghelp = "left"
    elabel = "left"
    stemval = "left"


left = _left()


class _inset(TagBase):
    tagstr = "inset-{val}"
    tagops = []
    taghelp = "inset"
    elabel = "inset"
    stemval = "inset"


inset = _inset()


class _start(TagBase):
    tagstr = "start{val}"
    tagops = []
    taghelp = "start"
    elabel = "start"
    stemval = "start"


start = _start()


class _W(TagBase):
    tagstr = "w-{val}"
    tagops = []
    taghelp = "element width"
    elabel = "W"
    stemval = "w"


W = _W()


class _zo(TagBase):
    tagstr = "z-{val}"
    tagops = []
    taghelp = "z-order"
    elabel = "zo"
    stemval = "z"


zo = _zo()


class _noop(TagBase):
    tagstr = "{val}"
    tagops = []
    taghelp = "noop"
    elabel = "noop"
    stemval = ""


noop = _noop()


# current_module = sys.modules[__name__]
# styTagDict = {}
# for varName in dir():
#     try:
#         res = getattr(current_module, varName)
#         styTagDict[varName] = res

current_module = sys.modules[__name__]
styTagDict = dict(
    [
        (name, cls)
        for name, cls in current_module.__dict__.items()
        if isinstance(cls, TagBase)
    ]
)
