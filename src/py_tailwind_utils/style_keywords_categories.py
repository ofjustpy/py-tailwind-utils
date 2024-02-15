# TODO: current, transparent (border, divide, outline, rinnnnng, ring offset, text color, text decoration color, background color, gradient color stops,

# TODO: full

# TODO: placement of positioned elements: inset, start, x, y, top, end, left, right, bottom, auto, full, absolute, 

# TODO: group <-- usage unclear

#. double for text decoration

#. TODO: clip

#. TODO: ring : inset
#. se ss sss sse 
almost_universal = [none, inherit, none, auto, visible, invisble, collapse, double, max, min, offset, row, col, end, sb, sl, sr, st, ]

entities = [
    sv.BoxTopo
    ]
table = [
    sv.Table,
    BoxTop,
    collapse,
    
    ]
rarely_used = [
    peer, 
    ]

outline = [double,
           sv.Outline
           ]

background = [bg, scroll, repeat
    ]
overflow = [
    hidden, scroll, visible, 
    ]

modifiers = [
    first,
    last,
    placeholder
    ]

interactivity = [resize, sv.PointerEvents, sv.Cursor]

all= [
    "bd",
    
    ]

text = [
    text,
    underline,
    offset,
    sv.WrapAround,
    sv.ClearWrap,
    sv.FontFamily,
    sv.FontStyle,
    sv.FontSmoothing,
    sv.FontSize,
    sv.FontWeight,
    sv.LetterSpace,
    sv.LineHeight,
    sv.TextAlign,
    sv.TextTransform,
     # as in text-decoration-inherit
    ]

#. TODO: BackgroundAttachment
typography = [
    sv.VerticalAlign,
    sv.LineClamp,
    sv.Prose,
    sv.Whitespace
    ]
colors = [
    "bd"
    ]

effects = [opacity,
           sv.BoxShadow
           ]
# TODO: backdrop-opacity
border = [
    border,
    color,
    W,
    bdr,
    bds,
    hidden,
    double,
    sv.BorderRadius,
    sv.BorderStyle
    
    ]

#. TODO Transform: rotate, scale
divide = [
    divide,
    x,
    y,
    color,
    double,
    sv.DivideStyle
    
    
    
    ]


shadow = [
    shadow
    
    
    ]

width = [
    "bd", #border
    

    ]

others = [
    "priority",
    

    ]

gradient = [
    from,
    to,
    via
    ]

spacing = [
    twpx,
    mr, #margin
    space,
    x,
    y,
    np  # negative prefix
    
    
    
    ]


# TODO: Filters
layout = [  #in-use in style_keywords_categories_sbs
    visible,
    invisible,
    
    container,
    columns,
    top,
    left,
    bottom,
    right,
    sv.ObjectFit,
    sv.ObjectPosition,
    sv.Visibility,
    sv.BreakInside,
    sv.BoxSizing,
    sv.Overflow,
    sv.OverflowX,
    sv.OverflowY,
    sv.AspectRatio
    ]

#TODO: stroke
sizing = [W, H, full, min, max, size, screen, space]

# https://tailwindcss.com/docs/display
layout_display = [hidden,  sv.DisplayBox, ]

grid = [span, grow, rows, cols, gap,
        sv.GridFlow, GridAuto,
        ]

#. TODO: order 
flexbox = [grow, row, reverse, col, wrap, reverse, nowrap, shrink, basis,
           sv.FlexLayout,
           sv.JustifyContent,
           sv.JustifyItems,
           sv.JustifySelf,
           sv.AlignSelf,
           sv.AlignContent,
           sv.AlignItems,
           sv.PlaceContent,
           sv.PlaceItems,
           sv.PlaceSelf
           
           ]

animation = [duration, sv.Transition]

accessibility = [sv.ScreenReaders]
