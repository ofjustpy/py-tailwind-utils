"""
 from string to tailwind expression
"""
from .style_tags import styTagDict
from . import  style_values_noop as sv
from .common import tstr
from .modifiers import modify

from py_tailwind_utils import mr, st, sl, sb, sr, x, y, auto, pd, np, se, ss,  noop, twpx, priority
from .colors import _tw_color_list, get_color_instance
import pysnooper

sv_map = {}
for en, eo in sv.styValueDict.items():
    enum_class = eo._sv_class
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


def color_value_decoder(tag, terminal=True):
    try:
        value = int(tag)
        if value != 50:
            cv = int(value/100)
            return cv
        else:
            return "50"
    except ValueError as e:
        # assume tag is a string
        # as in "500/50"
        return tag


def encode_tag(tag, terminal=False):
    if terminal:
        if tag == "px":
            return twpx, None
        
    if tag in st_map:
        return st_map[tag], None
    if tag in ["auto", "px", "t", "b", "l", "r", "s", "e"]:
        return st_map[tag], None

    if tag in _tw_color_list:
        return get_color_instance(tag), color_value_decoder
    try:
        value = int(tag)
        return value, None
    except:
        pass
     
    try:
        value = float(tag)
        return value, None
    except:
        pass

    print ("DEBUG-LOG ; assuming tag is string = ", tag)
    return tag, None


def encode_style_tag(the_meat, all_modifiers):

    # break modifiers from the utility class

    has_negative_prefix = False
    has_priority_prefix = False
    if the_meat[0] == "!":
        has_priority_prefix = True
        the_meat  =  the_meat[1:]
        
    if the_meat[0] == "-":
        has_negative_prefix = True
        the_meat  =  the_meat[1:]



    if has_priority_prefix and has_negative_prefix:
        print ("Can't handle  priority with negativ")
        assert False
        
        
    meat_parts = the_meat.split("-")
    restag = None
    if len(meat_parts) == 1:
        assert meat_parts[0] in st_map
        restag, value_decoder = encode_tag(meat_parts[0])
        pass

    if len(meat_parts) == 2:
        assert meat_parts[0] in st_map
        p0, value_decoder = encode_tag(meat_parts[0])
        if value_decoder:
            p1 = value_decoder(meat_parts[1], terminal=True)
        else:
            p1, value_decoder = encode_tag(meat_parts[1], terminal=True)
        restag = p0/p1
    
    if len(meat_parts) == 3:
        assert meat_parts[0] in st_map
        p0, value_decoder = encode_tag(meat_parts[0])
        assert value_decoder == None
        p1, value_decoder = encode_tag(meat_parts[1])
        if value_decoder:
            p2 = value_decoder(meat_parts[2], terminal=True)
        else:
            p2, value_decoder = encode_tag(meat_parts[2], terminal=True)
        restag = p0/p1/p2

    if len(meat_parts) == 4:
        p0, value_decoder = encode_tag(meat_parts[0])
        assert value_decoder == None
        p1, value_decoder = encode_tag(meat_parts[1])
        assert value_decoder == None
        
        p2, value_decoder = encode_tag(meat_parts[2])
        if value_decoder:
            p3 = value_decoder(meat_parts[3], terminal=True)
        else:
            p3, value_decoder = encode_tag(meat_parts[3], terminal=True)
        restag =  p0/p1/p2/p3

    
    if has_negative_prefix:
        restag = np/restag

    if has_priority_prefix:
        restag = priority/restag
        
    tags = [noop/restag]
    for mod in reversed(all_modifiers):
        tags = modify(*tags, modifier=mod)
        

    return tags[0]

def check_same_tstr(atstr, btstr):
    """
    check if two tailwind directives have excatly the same constructs
    """

    atags = atstr.split()
    btags = btstr.split()
    for atag in atags:
        assert atag in btags

    for btag in btags:
        assert btag in atags

    return True
        
        
def encode_twstr(twstr):
    tags = []
    for _ in twstr.split():
        if _ in ['[clip-path:_polygon(0_0,_0%_100%,_100%_50%)]',
                 'transition-[grid-template-columns]',
                 '[-moz-appearance:_textfield]',
                 '[&::-webkit-inner-spin-button]:m-0',
                 '[&::-webkit-inner-spin-button]:appearance-none',
                 '[&::-webkit-outer-spin-button]:m-0',
                 '[&::-webkit-outer-spin-button]:appearance-none',
                 '[text-align:_inherit]',
                 '[&_summary::-webkit-details-marker]:hidden',
                 '[&_summary::-webkit-details-marker]:hidden',
                 '[-webkit-tap-highlight-color:_transparent]'
                 'swiper-prev-button', # marketing/announcments/ 8-dark.html
                 ]:
            print ("cannot handle set 1: ",_)
            assert False
        if 'swiper' in _:
            continue
        # if "/" in _:
        #     print(f"DEBUG:error-/:  skipping  {_} because of /")
        #     continue
        if 'animate-background' in _:
            print(f"DEBUG:error-animate:  skipping  {_} because of animate-background")
            assert False

        if 'transform' in _:
            print(f"DEBUG:error-transform:  skipping  {_} because of transform")
            assert False
        if "[" in _:
            print(f"DEBUG:error-[]:  skipping  {_} because of [")
            assert False
        stuff = _.split(":")
        all_modifiers = stuff[0:-1]
        the_meat = stuff[-1]
        
        if the_meat in sv_map:
            restag = sv_map[the_meat]
            # no need for noop -- already present in sv_map
            #restag = noop/restag # so simple -- but creates massive bugs noop/noop/style-vale will create big problems
            
            res = [noop/restag]

            for mod in reversed(all_modifiers):
                res = modify(*res, modifier=mod)
            assert len(res) == 1
            
            tags.append(res[0])
        else:
            res = encode_style_tag(the_meat, all_modifiers)
            if res:
                tags.append(res)

        
    decoded = tstr(*tags)
    # make sure the decoded is same as encoded
    check_same_tstr(twstr, decoded)
    return tags
        
