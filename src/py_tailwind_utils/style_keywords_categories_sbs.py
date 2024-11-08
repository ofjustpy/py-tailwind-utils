
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
         
         StyT.offset,
         StyT.lh, # leading-{number|tight|snug|normal|relaxed|loose},
         StyT.indent # indent-{number}
         ],
    [

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
        StyV.ListStylePosition,
        StyV.ListStyleType,
        StyV.TextDecoration,
        StyV.TextOverflow,
        StyV.DecorationStyle,
        StyV.WrapAround,
        StyV.ClearWrap
        ]
     # as in text-decoration-inherit
    ]

#. TODO: Break After, Break Before Break Before, Box Decoration Break, Floats
#  Isolation,


flex_group_layout_tags = [[
    ],
                    [
                        StyV.JustifyContent,
                        StyV.AlignItems,
                        StyV.FlexDirection,
                        StyV.FlexWrap
                        ]


    ]
parent_child_layout_tags = [[
                             

    ],
                            [StyV.PlacementPosition,
                                ]


    ]

grid_tags = [[],
             [

                 StyV.PlaceContent,
                 StyV.PlaceItems,
                 StyV.AlignContent,
                 StyV.JustifyItems,
                 StyV.GridFlow,
                 StyV.GridAuto,
                 StyV.BorderStyle,
                 ]

    ]

# includes resizing, boxsizing, overflow, overscroll, visibility
self_flex_tags = [[
    ],
                                [
                                    StyV.FlexResize,
                                    StyV.BoxSizing,
                                    StyV.ObjectFit,
                                    StyV.ObjectPosition,
                                    StyV.Overflow,
                                    StyV.OverflowX,
                                    StyV.OverflowY,
                                    StyV.OverscrollBehaviour,
                                    StyV.LayoutVisibility
                                    
                                    ]


    ]

self_place_resize_grid_tags = [[
    ],
                                [
                                    StyV.JustifySelf,
                                    StyV.AlignSelf,
                                    StyV.PlaceSelf,
                                    
                                    ]


    ]


# layout_tags = [
#     [
#      StyT.container,
#      StyT.columns,
#      StyT.top,
#      StyT.left,
#      StyT.bottom,
#      StyT.right,
#      StyT.auto,
#      StyT.inset,
#      StyT.zo,
#      StyT.contain
#      ],
    
#     [
#     StyV.ObjectFit,
#     StyV.ObjectPosition,
#     StyV.Visibility,
#     StyV.BreakInside,
#     StyV.BoxSizing,
#     StyV.Overflow,
#     StyV.OverflowX,
#     StyV.OverflowY,
#         StyV.AspectRatio,
#         StyV.DisplayBox,
#         StyV.ClearWrap,
#         StyV.WrapAround,
#         StyV.LayoutVisibility
#         ]
#     ]

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
        StyV.DivideStyle,
        StyV.BoxShadow
        ]
    ]



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

            StyV.Table,
            StyV.DisplayBox
            
        ]
        ]

backgrounds_tags = [[],
                    [StyV.BackgroundAttachment
                     
                        ]


    ]





# TODO: image_filters_effects_transforms

# TODO: interactive_transitions

# Images Background
# Effects and filters Transforms
# interactivity


@ojr.ReactDomino
async def on_twValue_select(dbref, msg, to_ms):
    sty_value_class = getattr(StyV, dbref.key)
    sty_value_attr = getattr(sty_value_class, msg.value)
    return [("/tw_styValue_selected", (sty_value_class, sty_value_attr))]

async def on_twTag_click(dbref, msg, to_ms):
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
        comp_frame = oj.PD.Subsection(name, comp_box, section_depth=10)
        value_boxes.append(comp_frame)
        
    # removing tag_btns from display
    # there use is not particulary clear
    return oj.PC.Subsection(title,
                               oj.PC.StackG(num_cols=1, twsty_tags=[gap/x/12, gap/y/3, *variant(G/cols/2, rv="xl")],  childs=[*value_boxes]),
                               twsty_tags=[shadow.md, shadow/slate/200, pd/2, boxtopo.bd, bd/slate/100]
                               
                               )

    
almost_universal_panel = build_panel("Often used",
                                     almost_universal
                                     
                                     )
text_panel = build_panel("Text and Typography", text_tags[0], text_tags[1])

border_panel = build_panel("Border/Shadow", border_tags[0], border_tags[1])
flex_group_layout_panel = build_panel("Layout Group", flex_group_layout_tags[0], flex_group_layout_tags[1])

parent_child_layout_panel = build_panel("Layout Parent-Child", parent_child_layout_tags[0], parent_child_layout_tags[1])
grid_layout_panel = build_panel("Layout Grid",
                                grid_tags[0],
                                grid_tags[1]
                                )


self_flex_panel = build_panel("Layout/Resize Self: Flex",
                                      self_flex_tags[0],
                                      self_flex_tags[1],
                                      )

self_place_resize_grid_panel = build_panel("Layout/Resize Self: Grid",
                                      self_place_resize_grid_tags[0],
                                      self_place_resize_grid_tags[1],
                                      )

media_panel = build_panel("Media",
                                      self_place_resize_grid_tags[0],
                                      self_place_resize_grid_tags[1],
                                      )

dockbar = Dockbar ([text_panel,
                    border_panel,
                    flex_group_layout_panel,
                    parent_child_layout_panel,
                    self_flex_panel, 
                    grid_layout_panel,
                    self_place_resize_grid_panel
                    

                    ],
                   [#"Often used/Misc",
                       "Text and Typography",
                       "Border",
                       "Layout Group",
                       "Parent Child Layout",
                       "Place/Resize Self Flex",
                       "Layout Grid",
                       "Place/Resize Self Grid",
                    ],
                   undock_btn_sty = [
                       bdr.md,
                       boxtopo.bd,
                       
                       *variant(
                           bg / gray / 400,
                           fc / slate / 500,
                           bd / slate / 200,
                           boxtopo.bd,
                           bd/2,
                           bdr.md,
                           shadow.none,
                           rv="disabled",
                       )
                       ]
                   )

                   
