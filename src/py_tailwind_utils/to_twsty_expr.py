"""
 from string to tailwind expression
"""
from .style_tags import styTagDict
from . import  style_values_noop as sv
from .common import tstr
from .modifiers import modify

from py_tailwind_utils import mr, st, sl, sb, sr, x, y, auto
sv_map = {}
for en, eo in sv.styValueDict.items():
    # print (en, " ", eo)
    enum_class = eo._sv_class
    name = enum_class.__name__
    for _ in enum_class:
        # print(_, " ", _.name, " ", _.value)
        sv_map[_.value] = _
        
# style tag mapping
st_map = {}
for tagname, tagC in styTagDict.items():
    tag_sm = tagC.__class__.__name__[1:]
    st_map[tagC.stemval] = tagC


st_map["mt"] = mr/st
st_map["ml"] = mr/sl
st_map["mb"] = mr/sb
st_map["mr"] = mr/sr
st_map["mx"] = mr/x
st_map["my"] = mr/y
#st_map["m"] = mr


def encode_style_tag(twstr):

    # break modifiers from the utility class
    stuff = twstr.split(":")
    all_modifiers = stuff[0:-1]
    the_meat = stuff[-1]

    meat_parts = the_meat.split("-")
    restag = None
    if len(meat_parts) == 1:
        assert meat_parts[0] in st_map
        restag = st_map[meat_parts[0]]
        
        pass

    if len(meat_parts) == 2:
        assert meat_parts[0] in st_map
        if meat_parts[1] == "auto":
            restag = st_map[meat_parts[0]]/auto
        else:
            try:
                value = int(meat_parts[1])
                restag = st_map[meat_parts[0]]/value
            except ValueError as e:
                # not what else can be w-6 etc
                assert False
                pass
    
    if len(meat_parts) == 3:
        assert False

    tags = [restag]
    for mod in all_modifiers:
        tags = modify(*tags, modifier=mod)

    return tags[0]


def encode_twstr(twstr):
    tags = []
    for _ in twstr.split():
        if _ in sv_map:
            tags.append(sv_map[_])
            pass
        else:
            encode_style_tag(_)
        
