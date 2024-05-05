
from .style_tags import styTagDict
from . import style_tags as StyT
from . import style_values as StyV

from ofjustpy_components.htmlcomponents import Dockbar
import ofjustpy as oj
from py_tailwind_utils import *
import ofjustpy_react as ojr
#color
# TODO: table

# TODO: modifiers

almost_universal = [StyT.none, StyT.inherit, StyT.auto, StyT.double, StyT.max, StyT.min, StyT.offset, StyT.row,
                    StyT.col, StyT.start, StyT.end, StyT.sb, StyT.sl, StyT.sr, StyT.st ,   StyT.x, 
     StyT.y,                  ]


# TODO: Font Variant Numeric
# TODO: list-image-none
# TODO: Text Decoration
# TODO: Text Underline Offset
# TODO: Text Overflow
# TODO: Word Break
# TODO: Hyphens
# TODO: Content
text_tags = [
    [    StyT.text,
    StyT.underline,
    StyT.offset,
         StyT.lh, # leading-{number|tight|snug|normal|relaxed|loose},
         StyT.indent # indent-{number}
         ],
    [
        StyV.WrapAround,
        StyV.FontFamily,
        StyV.FontStyle,
        StyV.FontSmoothing,
        StyV.FontSize,
        StyV.FontWeight,
        StyV.LetterSpace,
        StyV.LineHeight,
        StyV.TextAlign,
        StyV.TextTransform,
        StyV.TextWrap,
        StyV.VerticalAlign,
        StyV.LineClamp,
        StyV.Prose,
        StyV.Whitespace,
        StyV.ListItems
        ]
     # as in text-decoration-inherit
    ]

#. TODO: Break After, Break Before Break Before, Box Decoration Break, Floats
#  Isolation, 
layout_tags = [
    [StyT.visible,
     StyT.invisible,
     StyT.container,
     StyT.columns,
     StyT.top,
     StyT.left,
     StyT.bottom,
     StyT.right,
     StyT.auto,
     StyT.inset,
     StyT.zo,
     StyT.contain
     ],
    
    [
    StyV.ObjectFit,
    StyV.ObjectPosition,
    StyV.Visibility,
    StyV.BreakInside,
    StyV.BoxSizing,
    StyV.Overflow,
    StyV.OverflowX,
    StyV.OverflowY,
        StyV.AspectRatio,
        StyV.DisplayBox,
        StyV.ClearWrap,
        ]
    ]

border_tags = [
    [StyT.bd,
     StyT.x,
     StyT.y,
     StyT.st,
     StyT.se,
     StyT.ss,
     StyT.sr,
     StyT.sb,
     StyT.sl,
     StyT.ring,
     StyT.offset,
     StyT.inset,
     StyT.divide,
     ],
    [
    
        StyV.BorderRadius,
        StyV.BorderStyle,
        StyV.OutlineStyle,
        StyV.DivideStyle
        ]
    ]

# order
flexbox_tags = [[StyT.grow, StyT.row, StyT.reverse,
            StyT.col,  StyT.reverse, StyT.shrink, StyT.basis, StyT.grow, StyT.shrink],
           
           [StyV.FlexLayout,
           StyV.JustifyContent,
           StyV.JustifyItems,
           StyV.JustifySelf,
           StyV.AlignSelf,
           StyV.AlignContent,
           StyV.AlignItems,
           StyV.PlaceContent,
           StyV.PlaceItems,
           StyV.PlaceSelf
            ]
           
           ]
spacing_sizing_tags = [[
    StyT.twpx,
    StyT.mr, #margin
    StyT.space,
    StyT.x,
    StyT.y,
    StyT.np,  # negative prefix
    StyT.W,   # space-{full, screen, svw, lvw, dvw, max, min, fit, screen}
    StyT.H,
    StyT.full,
    StyT.size, # size-{number|fraction|px|full|min|max|fit}
    StyT.screen,
    StyT.pd,
    StyT.reverse ],
                  []
    ]

# TODO:  Caption Side
grid_tables_tags = [[StyT.span,
         StyT.grow,
         StyT.rows, # grid-rows-{number}
         StyT.cols,
         StyT.G, # grid-cols-{number}
         StyT.gap, # gap-{number|px}, gap-{x|y}-{number}
         StyT.col, # col-span-{number}
         StyT.row, # row-span-{number}
                     StyT.spacing,
                     StyT.bd,
                     
         ],
        [
            StyV.GridFlow,
            StyV.GridAuto,
            StyV.BorderStyle,
            StyV.Table,
            StyV.DisplayBox
            
        ]
        ]

# TODO: image_filters_effects_transforms

# TODO: interactive_transitions

# Images Background
# Effects and filters Transforms
# interactivity


@ojr.ReactDomino
def on_twValue_select(dbref, msg, to_ms):
    sty_value_class = getattr(StyV, dbref.key)
    sty_value_attr = getattr(sty_value_class, msg.value)
    return "/tw_styValue_selected", (sty_value_class, sty_value_attr)

def on_twTag_click(dbref, msg, to_ms):
    assert False

def build_panel(title, tags, values= []):
    """
    tags: style tags
    values: style values
    """
    tag_btns = [
        oj.AD.Button(key = tagC.__class__.__name__[1:],
                     childs = [oj.PC.Span(text=tagC.taghelp, twsty_tags=[fz.sm, fw.medium, pd/x/2, pd/y/3])],
                     value = tagC.elabel,
                     twsty_tags = [boxtopo.bd, bdr.lg, bd/slate/700, bg/slate/200],
                     on_click = on_twTag_click
                     )     for tagC in tags]
    

    value_boxes = []
    for attrClass in values:
        enum_class = attrClass
        name = enum_class.__name__
        banner_text = name
        comp_box= oj.AD.Select(key=name,
                               childs = [oj.PC.Option(text = _.value ,
                                                      value=_.name
                                                      )
                                         for _ in enum_class
                                         ],
                               on_change= on_twValue_select,
                               twsty_tags=[boxtopo.bd, bdr.lg, bd/slate/700, bg/slate/200, pd/x/3, pd/y/2]
                               )
        
        value_boxes.append(comp_box)
        
    
    return oj.PC.Subsubsection(title,
                               oj.PC.StackG(num_cols=1, twsty_tags=[gap/x/12, gap/y/3, *variant(G/cols/2, rv="xl")],  childs=[*tag_btns, *value_boxes]),
                               twsty_tags=[shadow.md, shadow/slate/200, pd/2, boxtopo.bd, bd/slate/100]
                               
                               )

    
almost_universal_panel = build_panel("Often used",
                                     almost_universal
                                     
                                     )
text_panel = build_panel("Text and Typography", text_tags[0], text_tags[1])

border_panel = build_panel("Border", border_tags[0], border_tags[1])

layout_panel = build_panel("Layout", layout_tags[0], layout_tags[1])

flexbox_panel = build_panel("Flexbox", flexbox_tags[0], flexbox_tags[1])

spacing_sizing_panel = build_panel("Sizing and Spacing", spacing_sizing_tags[0], spacing_sizing_tags[1])

grid_tables_panel = build_panel("Grid and Tables", grid_tables_tags[0], grid_tables_tags[1])

dockbar = Dockbar ([almost_universal_panel,
                    text_panel,
                    border_panel,
                    layout_panel,
                    flexbox_panel,
                    spacing_sizing_panel,
                    grid_tables_panel
                    ],
                   ["Often used/Misc",
                    "Text and Typography",
                    "Border",
                    "Layout",
                    "Flexbox",
                    "Sizing and Spacing",
                    "Grid and Tables"
                    ]
                   )

                   
