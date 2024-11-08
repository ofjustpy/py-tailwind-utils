# This file is part of project py-tailwind-utils
#
# Copyright (c) [2023] by Monallabs.in.
# This file is released under the MIT License.
#
# Author(s): Kabira K. (webworks.monallabs.in).
# MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys

from aenum import Enum

#################################################
# block	display: block;                         #
# inline-block	display: inline-block;          #
# inline	display: inline;                #
# flex	display: flex;                          #
# inline-flex	display: inline-flex;           #
# table                                         #
#################################################

###############################################################
# inline-table	display: inline-table;                        #
# table-caption	display: table-caption;                       #
# table-cell	display: table-cell;                          #
# table-column	display: table-column;                        #
# table-column-group	display: table-column-group;          #
# table-footer-group	display: table-footer-group;          #
# table-header-group	display: table-header-group;          #
# table-row-group	display: table-row-group;             #
# table-row	display: table-row;                           #
# flow-root	display: flow-root;                           #
# grid	display: grid;                                        #
# inline-grid	display: inline-grid;                         #
# contents	display: contents;                            #
# list-item	display: list-item;                           #
# hidden	display: none;                                #
###############################################################

#TODO: Floats


class DisplayBox(Enum):
    b = "block"
    bi = "inline-block"
    i = "inline"
    f = "flex"
    fi = "inline-flex"
    t = "table"
    it = "inline-table"
    tcaption = "table-caption"
    tcell = "table-cell"
    tc = "table-column"
    tcg = "table-column-group"
    tfg = "table-footer-group"
    thg = "table-header-group"  # Changed from hogg to thg
    trg = "table-row-group"
    tr = "table-row"  # Changed from ro to tr
    flowroot = "flow-root"
    g = "grid"
    ig = "inline-grid"
    contents = "contents"
    li = "list-item"
    h = "hidden"

# class DisplayBox(Enum):
#     b = "block"
#     bi = "inline-block"
#     i = "inline"
#     f = "flex"
#     fi = "inline-flex"
#     t = "table"
#     g = "grid"
#     # TBD: add more docs/display
#     pass


#BoxLayout = DisplayBox

# docs/float


class WrapAround(Enum):
    s = "float-start"
    e = "float-end"
    r = "float-right"
    l = "float-left"
    n = "float-none"


class ClearWrap(Enum):
    l = "clear-left"
    r = "clear-right"
    b = "clear-both"
    n = "clear-none"


# TBD: docs/isolation


# TBD: docs/overscroll-behaviour
class ObjectFit(Enum):
    cn = "object-contain"      # Scale to fit within container, preserving aspect ratio.
    cv = "object-cover"        # Fill container while preserving aspect ratio; may crop.
    f = "object-fill"          # Stretch to fill container, ignoring aspect ratio.
    n = "object-none"          # Keep original size, may overflow or leave space.
    sd = "object-scale-down"   # Scale down if larger than container, preserve aspect ratio.


    
# TODO: top, bottom permutation combination missing


class ObjectPosition(Enum):
    b = "object-bottom"
    c = "object-center"
    l = "object-left"
    lb = "object-left-bottom"
    lt = "object-left-top"
    r = "object-right"
    rb = "object-right-bottom"
    t = "object-top"


# class Visibility(Enum):
#     v = "visible"
#     nv = "invisible"

class FlexDirection(Enum):
    row = "flex-row"
    rrow = "flex-row-reverse"
    col = "flex-col"
    rcol = "flex-col-reverse"
    

class FlexWrap(Enum):
    w = "flex-wrap"
    rw = "flex-wrap-reverse"
    nw = "flex-nowrap"
    
class FlexResize(Enum):
    
    one = "flex-1"
    auto = "flex-auto"
    initial = "flex-initial"
    none = "flex-none"
    grow = "flex-grow"
    nogrow = "flex-grow-0"
    shrink = "flex-shrink"
    noshrink = "flex-shrink-0"


class JustifyContent(Enum):
    start = "justify-start"
    end = "justify-end"
    center = "justify-center"
    between = "justify-between"
    evenly = "justify-evenly"
    around = "justify-around"
    stretch = "justify-stretch"
    normal = "justify-normal"

class JustifyItems(Enum):
    start = "justify-items-start"
    end = "justify-items-end"
    center = "justify-items-center"
    stretch = "justify-items-stretch"


class JustifySelf(Enum):
    auto = "justify-self-auto"
    start = "justify-self-start"
    end = "justify-self-end"
    center = "justify-self-center"
    stretch = "justify-self-stretch"


class AlignSelf(Enum):
    auto = "self-auto"
    start = "self-start"
    end = "self-end"
    center = "self-center"
    stretch = "self-stretch"
    baseline = "self-baseline"
class AlignContent(Enum):
    start = "content-start"
    end = "content-end"
    center = "content-center"
    between = "content-between"
    evenly = "content-evenly"
    around = "content-around"
    normal = "content-normal"
    baseline = "content-baseline"
    stretch = "content-stretch"

class AlignItems(Enum):
    start = "items-start"
    end = "items-end"
    center = "items-center"
    stretch = "items-stretch"
    baseline = "items-baseline"


# TBD docs/align-self


class PlaceContent(Enum):
    start = "place-content-start"
    end = "place-content-end"
    center = "place-content-center"
    between = "place-content-between"
    evenly = "place-content-evenly"
    around = "place-content-around"
    stretch = "place-content-stretch"


class PlaceItems(Enum):
    start = "place-items-start"
    end = "place-items-end"
    center = "place-items-center"
    stretch = "place-items-stretch"


class PlaceSelf(Enum):
    auto = "place-self-auto"
    start = "place-self-start"
    end = "place-self-end"
    center = "place-self-center"
    stretch = "place-self-stretch"


class FontFamily(Enum):
    sans = "font-sans"
    serif = "font-serif"
    mono = "font-mono"
    pass


class FontStyle(Enum):
    i = "italic"
    ni = "not-italic"


class FontSmoothing(Enum):
    a = "antialiased"
    sa = "subpixel-antialiased"


class FontSize(Enum):
    xs = "text-xs"
    sm = "text-sm"
    _ = "text-base"
    lg = "text-lg"
    xl = "text-xl"
    xl2 = "text-2xl"
    xl3 = "text-3xl"
    xl4 = "text-4xl"
    xl5 = "text-5xl"
    xl6 = "text-6xl"
    # TBD ixl
    pass


# TDB docs/font-smoothing
# TBD docs/font-style


class FontWeight(Enum):
    thin = "font-thin"
    extralight = "font-extralight"
    light = "font-light"
    normal = "font-normal"
    medium = "font-medium"
    bold = "font-bold"
    extrabold = "font-extrabold"
    black = "font-black"
    semibold = "font-semibold"

    def __call__(self, *args):
        return self.value(*args)


# TBD: docs/font-variant-numeric


class LetterSpace(Enum):
    tighter = "tracking-tighter"
    tight = "tracking-tight"
    normal = "tracking-normal"
    wide = "tracking-wide"
    wider = "tracking-wider"
    widest = "tracking-widest"


class LineHeight(Enum):
    none = "leading-none"
    tight = "leading-tight"
    snug = "leading-snug"
    normal = "leading-normal"
    relaxed = "leading-relaxed"
    loose = "leading-loose"


class ListStylePosition(Enum):
    i = "list-inside"
    o = "list-outside"



class ListStyleType(Enum):
    none = "list-none"
    disc = "list-disc"
    decimal = "list-decimal"


class TextAlign(Enum):
    left = "text-left"
    center = "text-center"
    right = "text-right"
    justify = "text-justify"
    start = "text-start"
    end = "text-end"
    pass


# https://tailwindcss.com/docs/text-transform
class TextTransform(Enum):
    u = "uppercase"
    l = "lowercase"
    c = "capitalize"
    n = "normal-case"


class TextWrap(Enum):
    wrap = "text-wrap"
    nowrap = "text-nowrap"
    balance = "text-balance"
    pretty = "text-pretty"


class TextDecoration(Enum):
    underline = "underline"
    overline = "overline"
    linethrough = "line-through"
    nounderline = "no-underline"


class TextOverflow(Enum):
    truncate = "truncate"
    ellipsis = "text-ellipsis"
    clip = "text-clip"

    
        
class DecorationStyle(Enum):
    solid = "decoration-solid"
    dashed = "decoration-dashed"
    dotted = "decoration-dotted"
    double = "decoration-double"
    wavy = "decoration-wavy"
    
class VerticalAlign(Enum):
    baseline = "align-baseline"
    
    top = "align-top"
    middle = "align-middle"
    bottom = "align-bottom"
    texttop = "align-text-top"
    textbottom = "align-text-bottom"
    alignsub = "align-sub"
    alignsuper = "align-super"
    # few others left out

    pass


# TBD docs/text-decoratio
# TBD docs/text-transform
# TBD docs/text-overflow
# TBD docs/vertical-align
# TBD docs/whitespace
# TBD docs/wordbreak


class BackgroundAttachment(Enum):
    f = "bg-fixed"
    l = "bg-local"
    s = "bg-scroll"


# TBD docs/background-clip
# TBD docs/backgrond-origin
# TBD docs/backgrond-position
# TBD docs/backgrond-repeat
# TBD docs/backgrond-size
# TBD docs/backgrond-image
# TBD docs/gradient-color-stops


class BorderRadius(Enum):
    sm = "rounded-sm"
    md = "rounded-md"
    lg = "rounded-lg"
    full = "rounded-full"
    none = "rounded-none"
    _ = "rounded"
    xl = "rounded-xl"
    xl2 = "rounded-2xl"
    xl3 = "rounded-3xl"
    pass


class BorderStyle(Enum):
    solid = "border-solid"
    dashed = "border-dashed"
    dotted = "border-dotted"
    double = "border-double"
    none = "border-none"
    collapse = "border-collapse"  # for table
    separate = "border-separate"


class DivideStyle(Enum):
    solid = "divide-solid"
    dashed = "divide-dashed"
    dotted = "divide-dotted"
    double = "divide-double"
    none = "divide-none"
    
    
class OutlineStyle(Enum):
    none = "outline-none"
    #_ = "outline"
    dashed = "outline-dashed"
    dotted = "outline-dotted"
    double = "outline-double"
    hidden = "outline-hidden"


class BoxShadow(Enum):
    sm = "shadow-sm"
    _ = "shadow"
    md = "shadow-md"
    lg = "shadow-lg"
    xl = "shadow-xl"
    xl2 = "shadow-2xl"
    none = "shadow-none"
    inner = "shadow-inner"
    pass

class LineClamp(Enum):
    one = "line-clamp-1"
    two = "line-clamp-2"
    three = "line-clamp-3"
    four = "line-clamp-4"
    five = "line-clamp-5"
    six = "line-clamp-6"
    none = "line-clamp-none"
    

    
class Table(Enum):
    auto = "table-auto"
    fixed = "table-fixed"

class BreakInside(Enum):
    auto = "break-inside-auto"
    avoid = "break-inside-avoid"
    avoid_page = "break-inside-avoid-page"
    avoid_column = "break-inside-avoid-column"    

# class Transition(Enum):
#     none="transition-none"

# TBD:   docs/transition-timing-function, transition-delay, animation, transform, transform-origin, tranform-scale, transform-rotate, translate, skew,

# TBD: appreance
# TBD: cursor,


# class Outline(Enum):
#     n = "outline-none"
#     w = "outline-white"
#     b = "outline-black"


# TBD: user-select, fill-current, stroke, stroke-width, screen-readers, typography(proces),

# here--


# Layout
class BoxTopo(Enum):
    bd = "border"
    ring = "ring"
    outline = "outline"
    # container = "container"
    pass


class PlacementPosition(Enum):
    static = "static"
    fixed = "fixed"
    absolute = "absolute"
    relative = "relative"
    sticky = "sticky"
    pass

class LayoutVisibility(Enum):
    v = "visible"
    iv = "invisible"
    c = "collapse"
    
class BoxSizing(Enum):
    b = "box-border"
    c = "box-content"
    pass


class Prose(Enum):
    sm = "prose-sm"
    _ = "prose-base"
    lg = "prose-lg"
    xl = "prose-xl"
    xl2 = "prose-2xl"
    pass


class GridFlow(Enum):
    row = "grid-flow-row"
    col = "grid-flow-col"
    dense = "grid-flow-dense"
    rowd = "grid-flow-row-dense"
    cold = "grid-flow-col-dense"
    pass


class Whitespace(Enum):
    normal = "whitespace-normal"
    nowrap = "whitespace-nowrap"
    pre = "whitespace-pre"
    pre_line = "whitespace-pre-line"
    pre_wrap = "whitespace-pre-wrap"
    break_spaces = "whitespace-break-spaces"

class WordBreak(Enum):
    normal = "break-normal"
    words = 	"break-words" 
    all = "break-all"
    keep = "break-keep"

class GridAuto(Enum):
    cauto = "grid-cols-auto"
    cmin = "grid-cols-min"
    cmax = "grid-cols-max"
    cfr = "grid-cols-fr"
    rauto = "grid-rows-auto"
    rmin = "grid-ros-min"
    rmax = "grid-rows-max"
    rfr = "grid-rows-fr"

class Transition(Enum):
    none = "transition-none"
    all = "transition-all"
    default = "transition"
    colors = "transition-colors"
    opacity = "transition-opacity"
    shadow = "transition-shadow"
    transform = "transition-transform"

class ScreenReaders(Enum):
    only = "sr-only"
    notonly = "not-sr-only"

class Overflow(Enum):
    auto = "overflow-auto"
    hidden = "overflow-hidden"
    clip = "overflow-clip"
    visible = "overflow-visible"
    scroll = "overflow-scroll"

class OverflowX(Enum):
    auto = "overflow-x-auto"
    hidden = "overflow-x-hidden"
    clip = "overflow-x-clip"
    visible = "overflow-x-visible"
    scroll = "overflow-x-scroll"

class OverflowY(Enum):
    auto = "overflow-y-auto"
    hidden = "overflow-y-hidden"
    clip = "overflow-y-clip"
    visible = "overflow-y-visible"
    scroll = "overflow-y-scroll"        

class OverscrollBehaviour(Enum):
    auto = "overscroll-auto"
    contain = "overscroll-contain"
    none = "overscroll-none"
    y_auto = "overscroll-y-auto"
    y_contain = "overscroll-y-contain"
    y_none = "overscroll-y-none"
    x_auto = "overscroll-x-auto"
    x_contain = "overscroll-x-contain"
    x_none = "overscroll-x-none"

    
class PointerEvents(Enum):
    none = "pointer-events-none"
    auto = "pointer-events-auto"

class AspectRatio(Enum):
    auto = "aspect-auto"
    square = "aspect-square"
    video = "aspect-video"


class Cursor(Enum):
    auto = "cursor-auto"
    default = "cursor-default"
    pointer = "cursor-pointer"
    wait = "cursor-wait"
    text = "cursor-text"
    move = "cursor-move"
    help = "cursor-help"
    not_allowed = "cursor-not-allowed"
    none = "cursor-none"

class BackgroundRepeat(Enum):
    repeat = "bg-repeat"
    no_repeat = "bg-no-repeat"
    repeat_x = "bg-repeat-x"
    repeat_y = "bg-repeat-y"
    repeat_round = "bg-repeat-round"
    repeat_space = "bg-repeat-space"

class Animation(Enum):
    none = "animate-none"
    spin = "animate-spin"
    ping = "animate-ping"
    pulse = "animate-pulse"
    bounce = "animate-bounce"
    
current_module = sys.modules[__name__]
styValueDict = dict(
    [
        (name, cls)
        for name, cls in current_module.__dict__.items()
        if isinstance(cls, type) and name != "Enum"
    ]
)
# for varName in dir():
#     try:
#         res = getattr(current_module, varName)
#         styValueDict[varName] = res

#     except:

#         pass
