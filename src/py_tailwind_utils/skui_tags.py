import sys

from .common import TagBase, _ColorBase, _IDivExpr, _PresetBase
from .style_tags import noop
_skui_color_list = ["primary",
                   "secondary",
                   "tertiary",
                   "success",
                   "warning",
                   "surface",
                   "error"
                   ]

for color in _skui_color_list:
    globals()[color.capitalize()] = type(
        color.capitalize(), (_ColorBase,), {"mycolor": color, "tagstr": f"{color}-{{val}}"}
    )

    globals()[color] = globals()[color.capitalize()]()

#TODO:
#. disabled



from aenum import Enum


_skui_keywords_val = [
    "blockquote",
    "anchor",
    "pre",
    "code"
    "del",
    "ins",
    "mark",
    "badge",
    "btn",
    "card",
    "chip",
    "hr",
    "vr",
    "label",
    "input",
    "select",
    "placeholder"
    ]
for kw in _skui_keywords_val:
    globals()[f"_{kw}"] = type(
        f"_{kw}",
        (TagBase,),
        {"tagstr": kw, "tagops": [], "taghelp": kw, "elabel": kw, "stemval": kw},
    )

    globals()[kw] = globals()[f"_{kw}"]()

    


class _btn_icon(TagBase):
    tagstr = "btn-icon"
    tagops = []
    taghelp = "btn-icon"
    elabel = "btn_icon"
    stemval = "btn-icon"

btn_icon = _btn_icon()

class _btn_base(TagBase):
    tagstr = "btn-base"
    tagops = []
    taghelp = "btn-base"
    elabel = "btn_base"
    stemval = "btn-base"

btn_base = _btn_base()

class _btn_sm(TagBase):
    tagstr = "btn-sm"
    tagops = []
    taghelp = "btn-sm"
    elabel = "btn_sm"
    stemval = "btn-sm"

btn_sm = _btn_sm()

class _btn_lg(TagBase):
    tagstr = "btn-lg"
    tagops = []
    taghelp = "btn-lg"
    elabel = "btn_lg"
    stemval = "btn-lg"

btn_lg = _btn_lg()

class _btn_group(TagBase):
    tagstr = "btn-group"
    tagops = []
    taghelp = "btn-group"
    elabel = "btn_group"
    stemval = "btn-group"

btn_group = _btn_group()

class _badge_icon(TagBase):
    tagstr = "badge-icon"
    tagops = []
    taghelp = "badge-icon"
    elabel = "badge_icon"
    stemval = "badge-icon"

badge_icon = _badge_icon()

class _card_hover(TagBase):
    tagstr = "card-hover"
    tagops = []
    taghelp = "card-hover"
    elabel = "card_hover"
    stemval = "card-hover"

card_hover = _card_hover()

class _chip_icon(TagBase):
    tagstr = "chip-icon"
    tagops = []
    taghelp = "chip-icon"
    elabel = "chip_icon"
    stemval = "chip-icon"

chip_icon = _chip_icon()

class _label_text(TagBase):
    tagstr = "label-text"
    tagops = []
    taghelp = "label-text"
    elabel = "label_text"
    stemval = "label-text"

label_text = _label_text()

class _placeholder_circle(TagBase):
    tagstr = "placeholder-circle"
    tagops = []
    taghelp = "placeholder-circle"
    elabel = "placeholder_circle"
    stemval = "placeholder-circle"

placeholder_circle = _placeholder_circle()

class _animate_pulse(TagBase):
    tagstr = "animate-pulse"
    tagops = []
    taghelp = "animate-pulse"
    elabel = "animate_pulse"
    stemval = "animate-pulse"

animate_pulse = _animate_pulse()

class _table_wrap(TagBase):
    tagstr = "table-wrap"
    tagops = []
    taghelp = "table-wrap"
    elabel = "table_wrap"
    stemval = "table-wrap"

table_wrap = _table_wrap()

class _caption_bottom(TagBase):
    tagstr = "caption-bottom"
    tagops = []
    taghelp = "caption-bottom"
    elabel = "caption_bottom"
    stemval = "caption-bottom"

caption_bottom = _caption_bottom()



_skui_keywords_val = [
    "contrast",
    ]

for kw in _skui_keywords_val:
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
    
    

class FontSize(Enum):
    xs = "text-xs"
    sm = "text-sm"
    _ = "text-base"
    lg = "text-lg"
    xl = "text-xl"
    xl2 = "text2-2xl"
    xl3 = "text3-3xl"
    xl4 = "text4-4xl"
    xl5 = "text5-5xl"
    xl6 = "text6-6xl"
    xl7 = "text7-7xl"
    xl8 = "text8-8xl"
    xl9 = "text9-9xl"

    pass

class _FontSize:
    _sv_class = FontSize
    
    @property
    def xs(cls):
        return noop / cls._sv_class.xs

    @property
    def sm(cls):
        return noop / cls._sv_class.sm

    @property
    def base(cls):
        return noop / cls._sv_class.base

    @property
    def lg(cls):
        return noop / cls._sv_class.lg

    @property
    def xl(cls):
        return noop / cls._sv_class.xl

    @property
    def xl2(cls):
        return noop / cls._sv_class.xl2

    @property
    def xl3(cls):
        return noop / cls._sv_class.xl3

    @property
    def xl4(cls):
        return noop / cls._sv_class.xl4

    @property
    def xl5(cls):
        return noop / cls._sv_class.xl5

    @property
    def xl6(cls):
        return noop / cls._sv_class.xl6

    @property
    def xl7(cls):
        return noop / cls._sv_class.xl7

    @property
    def xl8(cls):
        return noop / cls._sv_class.xl8

    @property
    def xl9(cls):
        return noop / cls._sv_class.xl9

SkFontSize = _FontSize()    
# skeleton ui classes    
class Headings(Enum):
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"
    

class _Headings:
    _sv_class = Headings
    
    @property
    def h1(cls):
        return noop / cls._sv_class.h1

    @property
    def h2(cls):
        return noop / cls._sv_class.h2

    @property
    def h3(cls):
        return noop / cls._sv_class.h3

    @property
    def h4(cls):
        return noop / cls._sv_class.h4

    @property
    def h5(cls):
        return noop / cls._sv_class.h5

    @property
    def h6(cls):
        return noop / cls._sv_class.h6

Headings = _Headings()





# ============================== presets =============================


# _skui_preset_list = ["pfilled",
#                    "ptonal",
#                    "poutline",
#                    ]

# for preset in _skui_preset_list:
#     globals()[preset.capitalize()] = type(
#         preset.capitalize(), (_PresetBase,), {"mypreset": preset, "tagstr": f"{preset}-{{val}}"}
#     )

#     globals()[preset] = globals()[preset.capitalize()]()
#     print("globals = ", globals()[preset])
    
