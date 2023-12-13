"""
 from string to tailwind expression
"""
from .style_tags import styTagDict
from . import  style_values_noop as sv
from .common import tstr
from .modifiers import modify

from py_tailwind_utils import mr, st, sl, sb, sr, x, y, auto, pd, np, se, ss, px, noop
from .colors import _tw_color_list, get_color_instance

sv_map = {}
for en, eo in sv.styValueDict.items():
    # print (en, " ", eo)
    enum_class = eo._sv_class
    name = enum_class.__name__
    for _ in enum_class:
        sv_map[_.value] = getattr(eo, _.name)
        
        
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
st_map["me"] = mr/se
st_map["ms"] = mr/ss

st_map["pt"] = pd/st
st_map["pl"] = pd/sl
st_map["pb"] = pd/sb
st_map["pr"] = pd/sr
st_map["px"] = pd/x
st_map["py"] = pd/y
st_map["pe"] = pd/se
st_map["ps"] = pd/ss

#st_map["m"] = mr


def encode_tag(tag):
    if tag in st_map:
        return st_map[tag]
    if tag in ["auto", "px", "t", "b", "l", "r", "s", "e"]:
        return st_map[tag]

    if tag in _tw_color_list:
        return get_color_instance(tag)
    try:
        value = int(tag)
        if value != 50:
            cv = int(value/100)
            return cv
        else:
            return "50"
    except ValueError as e:
        pass
    try:
        value = float(tag)
        return value
    except:
        pass
    assert False
        
def encode_style_tag(the_meat, all_modifiers):

    # break modifiers from the utility class

    has_negative_prefix = False
    if the_meat[0] == "-":
        has_negative_prefix = True
        the_meat  =  the_meat[1:]
        
    meat_parts = the_meat.split("-")
    print (meat_parts, " ", len(meat_parts))
    restag = None
    if len(meat_parts) == 1:
        assert meat_parts[0] in st_map
        restag = st_map[meat_parts[0]]
        
        pass

    if len(meat_parts) == 2:
        assert meat_parts[0] in st_map
        if meat_parts[1] == "auto":
            restag = st_map[meat_parts[0]]/auto
        elif meat_parts[1] == "px":
            restag = st_map[meat_parts[0]]/px
        elif meat_parts[1] in [ "e"]:
            restag = st_map[meat_parts[0]]/st_map[meat_parts[1]]
            #TODO: need all the sl, sr, etc. here
        elif meat_parts[1] in _tw_color_list:
            restag = st_map[meat_parts[0]]/get_color_instance(meat_parts[1])
            
        else:
            try:
                value = float(meat_parts[1])
                restag = st_map[meat_parts[0]]/value
            except ValueError as e:
                # not what else can be w-6 etc
                assert False
                pass
    
    if len(meat_parts) == 3:
        assert meat_parts[0] in st_map
        if meat_parts[1] in _tw_color_list:
            try:
                if int(meat_parts[2]) != 50:
                    cv = int(int(meat_parts[2])/100)
                else:
                    #TODO: we need to think about how to handle 50 holistically
                    cv = "50"
                restag = st_map[meat_parts[0]]/get_color_instance(meat_parts[1])/cv
            except ValueError as e:
                assert False
                
        elif meat_parts[1] in st_map:
            if meat_parts[2] == "px":
                restag = st_map[meat_parts[0]]/st_map[meat_parts[1]]/px
            else:
                cv = float(meat_parts[2])
                restag = st_map[meat_parts[0]]/st_map[meat_parts[1]]/cv
        else:
            assert False
        
        pass

    if len(meat_parts) == 4:
        p0 = encode_tag(meat_parts[0])
        p1 = encode_tag(meat_parts[1])
        p2 = encode_tag(meat_parts[2])
        p3 = encode_tag(meat_parts[3])
        return p0/p1/p2/p3
        pass
    
    if has_negative_prefix:
        restag = np/restag
        
    tags = [restag]
    for mod in all_modifiers:
        tags = modify(*tags, modifier=mod)


    return tags[0]


def encode_twstr(twstr):
    tags = []
    for _ in twstr.split():
        if _ in ['[clip-path:_polygon(0_0,_0%_100%,_100%_50%)]']:
            continue
        
        stuff = _.split(":")
        all_modifiers = stuff[0:-1]
        the_meat = stuff[-1]
        
        if the_meat in sv_map:
            restag = sv_map[the_meat]
            tags = [restag]
            for mod in all_modifiers:
                tags = modify(*tags, modifier=mod)
        else:
            res = encode_style_tag(the_meat, all_modifiers)
            if res:
                tags.append(res)
    return tags
        
