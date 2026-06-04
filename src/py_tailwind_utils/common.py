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

import logging

import aenum
from addict_tracking_changes import Dict
from aenum import Enum

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def isTwTagType(twtag):
    #for some reason W instances has twtag.__bases__
    # while screen has twtag.__class__.bases__

    try:
        if TagBase in twtag.__bases__:
            return True
    except:
        pass
    
    try:
        if TagBase in twtag.__class__.__bases__:
            return True
    except:
        pass

    
    return False

def is_scalar(value):
    if isTwTagType(value):
        if value.elabel == "auto":
            return True
        else:
            return False
        
    return isinstance(value, (int, float, str, bool))

def is_scalar_copy(value):
    if isTwTagType(value):
        if value.elabel == "auto":
            return True
        else:
            return False
        
    return isinstance(value, (int, float, str, bool))

class _ColorBase:
    mycolor = None
    elabel = "color"
    tagstr = None
    
    @classmethod
    def __truediv__(cls, colorval: str):
        # we need the instance associated with the color
        return _IDivExpr(globals()[cls.mycolor], colorval)
        #return cls.evaluate(str(colorval))

    @classmethod
    def evaluate(cls, colorval: str):
        if colorval == None:
            return cls.mycolor
        
        if colorval == "":
            return cls.mycolor
        
        if colorval == "0":
            return cls.mycolor
        # we are nolonger auto filling color val from 5 to 500
        # if len(colorval) == 1 and colorval[-1] != "0":
        #     # letting go of the idea of using short form
        #     assert False
        #     #return f"{cls.mycolor}-{colorval}00"
        else:
            return f"{cls.mycolor}-{colorval}"
        pass

    @classmethod
    def keyvaleval(cls, colorval: str):
        return cls.evaluate(colorval)

    # @ classmethod
    # def __pow__(cls, colorval):
    #     print("In __pw")
    #     return f"{cls.mycolor}-{colorval}00"

    @classmethod
    def __repr__(cls):
        return f"{cls.mycolor}"

class _PresetBase:
    mypreset = None
    elabel = "preset"
    tagstr = None
    
    @classmethod
    def __truediv__(cls, presetval: str):
        return _IDivExpr(globals()[cls.mypreset], presetval)

    @classmethod
    def evaluate(cls, presetval: str):
        if presetval == None:
            return f"preset-{cls.mypreset[1:]}"
        
        if presetval == "":
            return  f"preset-{cls.mypreset[1:]}"
        
        if presetval == "0":
            return f"preset-{cls.mypreset[1:]}"
        else:
            return f"preset-{cls.mypreset[1:]}-{presetval}"
        pass

    @classmethod
    def keyvaleval(cls, presetval: str):
        return cls.evaluate(presetval)

    @classmethod
    def __repr__(cls):
        return f"{cls.mypreset}"

_skui_preset_list = ["pfilled",
                   "ptonal",
                   "poutlined",
                     "ptypo",
                   ]

for preset in _skui_preset_list:
    globals()[preset.capitalize()] = type(
        preset.capitalize(), (_PresetBase,), {"mypreset": preset, "tagstr": f"preset-{preset[1:]}-{{val}}"}
    )

    globals()[preset] = globals()[preset.capitalize()]()


    
_tw_color_list = [
    "slate",
    "gray",
    "zinc",
    "neutral",
    "stone",
    "red",
    "orange",
    "amber",
    "yellow",
    "lime",
    "green",
    "emerald",
    "teal",
    "cyan",
    "sky",
    "blue",
    "indigo",
    "violet",
    "purple",
    "fuchsia",
    "pink",
    "rose",
    "black",
    "white",
]

for color in _tw_color_list:
    globals()[color.capitalize()] = type(
        color.capitalize(), (_ColorBase,), {"mycolor": color, "tagstr": f"{color}-{{val}}"}
    )

    globals()[color] = globals()[color.capitalize()]()

def get_color_instance(colorname):
    assert colorname in _tw_color_list
    return globals()[colorname]


class _IDivExpr:
    def __init__(self,
                 numor,
                 denom=None,
                 modifier_chain=None):
        """
        numor: numerator 
        denom: can be a IDivExpr, or a tag, or a enum, or a scalar
        tagstr, elabel will come from numerator
        """

        self.numor =  numor
        self.denom = denom
        self.modifier_chain = modifier_chain

    def __truediv__(self, arg):
        # only top-most idiv expression can have modifier chain
        tt = _IDivExpr(self.denom,  arg, modifier_chain=None
                       )
        self.denom = tt
        return self

    def evaluate(self, val=None):
        """
        Resolves the expression tree by first evaluating the denominator (the value)
        and then applying it to the numerator (the prefix).
        """
        # 1. RESOLVE THE DENOMINATOR (The "Value" or "Sub-Expression")
        subval, is_denom_scalar = self._resolve_denominator(val)
        # 2. APPLY TO THE NUMERATOR (The "Prefix" or "Tag")
        return self._apply_to_numerator(subval, is_denom_scalar)

    def _resolve_denominator(self, val=None):
        """Internal helper to determine the value of the right-hand side."""
        d = self.denom
        
        # Case: Nested Expression
        if isinstance(d, _IDivExpr):
            return d.evaluate(val=val), False
            
        # Case: Enums
        if isinstance(d, (aenum.Enum, aenum.EnumType)):
            return d.value, False
            
        # Case: Colors or Presets
        if isinstance(d, (_ColorBase, _PresetBase)):
            return d.evaluate(val), False

        # Case: Tailwind Tag Types
        if isTwTagType(d):
            # Special case for "auto" labels
            
            if hasattr(d, "tagstr_s"):
                if val is None:
                    raise ValueError(f"Template tag {d} requires a value but got None")
                return d.tagstr_s.format(val=val), is_scalar(d)
            
            return d.evaluate(val=val), is_scalar(d)

        # Case: Scalars (Int, Str, etc.)
        if is_scalar_copy(d):
            return d, True

        raise ValueError(f"Unknown denominator type: {type(d)} for {d}")

    def _apply_to_numerator(self, subval, is_denom_scalar):
        """Internal helper to wrap the subval with the left-hand side prefix."""
        n = self.numor

        # Case: Nested Expression (Pass subval up the chain)
        if isinstance(n, _IDivExpr):
            return n.evaluate(val=subval)

        # Case: Colors
        if isinstance(n, _ColorBase):
            return n.evaluate(colorval=subval)

        # Case: Presets
        if isinstance(n, _PresetBase):
            return n.evaluate(presetval=subval)

        # Case: Tailwind Tag Types
        if isTwTagType(n):
            # If the value is a terminal scalar, use the template string directly
            if is_denom_scalar and hasattr(n, "tagstr_s"):
                return n.tagstr_s.format(val=subval)
            
            # Otherwise, delegate to the tag's internal evaluation
            return n.evaluate(val=subval)

        raise ValueError(f"Unknown numerator type: {type(n)} for {n}")

    
    

    # def evaluate(self, val=None):
    #     is_denom_scalar = False
    #     if isinstance(self.denom, _IDivExpr):
    #         subval = self.denom.evaluate(val = val)
    #     elif isinstance(self.denom, aenum.Enum) or isinstance(self.denom, aenum.EnumType):
    #         subval = self.denom.value
    #     elif isTwTagType(self.denom):
    #         if hasattr(self.denom, "tagstr_s"):
    #             if val != None: 
    #                 subval = self.denom.tagstr_s.format(val=val)
    #             else:
    #                 raise ValueError("None found at value ")
    #         else:
    #             subval =  self.denom.evaluate(val=val)

    #         # its m-auto and not mauto
    #         if self.denom.elabel == "auto":
    #             is_denom_scalar = True
    #     elif isinstance(self.denom, _ColorBase):
    #         subval =  self.denom.evaluate(colorval=val)
    #     elif isinstance(self.denom, _PresetBase):
    #         subval =  self.denom.evaluate(colorval=val)            

    #     else:
    #         if is_scalar(self.denom):
    #             is_denom_scalar = True
    #         else:
    #             raise ValueError("Unkonwn type denom: ", self.denom)
            
    #         subval = self.denom

        
    #     if isinstance(self.numor, _IDivExpr):
    #         return self.numor.evaluate(val=subval)
    #     elif isTwTagType(self.numor):
    #         if hasattr(self.numor, "tagstr_s"):
    #             if is_denom_scalar:
    #                 return self.numor.tagstr_s.format(val=subval)
    #             else:
    #                 return self.numor.evaluate(val=subval)
                
    #         else:
    #             return self.numor.evaluate(val=subval)
    #     elif isinstance(self.numor, _ColorBase):
    #         return self.numor.evaluate(colorval=subval)
    #     elif isinstance(self.numor, _PresetBase):
    #         return self.numor.evaluate(presetval=subval)
    #     else:
    #         raise ValueError("Unknow _IDivExpr.numor type")
            

    #     assert False

    # TODO: 
    def keyvaleval(self):
        """
        Returns a representation of the _IDivExpr for the JSON builder.
        - Simple case (pd/4): returns ("pd", "4")
        - Nested case (pd/sl/4): returns ("pd", ("sl", "4"))
        """
        # 1. Identify the 'key' (the numerator)
        # We strip any internal object wrappers to get the string tag
        assert not isinstance(self.numor, _IDivExpr), \
        f"Unexpected nested _IDivExpr in numor: {self.numor}. 4 clause expression not supported"
        
        key = self.numor.elabel

        # 2. Resolve the 'value' (the denominator)
        denom = self.denom

        if isinstance(denom, _IDivExpr):
            # Case: pd / (sl / 4)
            # Recursively call keyvaleval on the denominator
            # This returns the nested tuple: ("sl", "4")
            return (key, denom.keyvaleval())

        else:
            # Case: pd / 4
            # Just return the tag and the raw value
            return (key, denom)
    


class TagBase:
    tagstr = None
    tagops = None
    taghelp = None
    elabel = None  # the label that ends up in the style expression

    @classmethod
    def __truediv__(cls, denom):
        return  _IDivExpr(cls, denom, modifier_chain=[])


    @classmethod
    def evaluate(cls, val=None):
        # return border, e , etc. if value is not specified
        if val == None:
            return cls.stemval
        return cls.tagstr.format(val= str(val))


    @classmethod
    def keyvaleval(cls, val=None):
        raise ValueError


def tstr(*args, prefix=""):
    if len(args) > 0:
        if isinstance(args[0], list) or isinstance(args[0], tuple):
            raise ValueError("error in tstr argument passing")

    res = ""
    for arg in args:
        # every tailwind tag should have modifier chain eventually
        # we will no longer use db.f but noop/db.f everwhe
        modifier_prefix = ""
        if hasattr(arg, "modifier_chain"):
            if arg.modifier_chain:
                modifier_prefix = ":".join(arg.modifier_chain) + ":"

        if isinstance(arg, Enum) or isinstance(arg, aenum.EnumType):
            # don't allow usage of raw style_values
            # always use noop/<style-value>
            assert False
        else:
            
            evals = arg.evaluate()
            res += f"{modifier_prefix}{prefix}" + evals + " "
            
    return res


# def exact_match_idivexpr_recurse(aidiv_expr, bidiv_expr):
#     if isinstance(aidiv_expr.numor, _IDivExpr) and isinstance(bidiv_expr.numor, _IDivExpr):
#         if exact_match_idivexpr_recurse(aidiv_expr.numor, bidiv_expr.numor):
#             pass
#         else:
            
#             return False
#     else:
#         try:

#             if aidiv_expr.numor.elabel != bidiv_expr.numor.elabel:
#                 logger.debug("mismatch at IDiv:numor.elabel")
#                 return False
#             else:
#                 #logger.debug(f"passes IDiv:numor.elabel equality {aidiv_expr.numor.elabel} {bidiv_expr.numor.elabel}")
#                 pass
#         except:
#             logger.debug(f"Failed Test: aidiv_expr.numor and bidiv_expr.numor are of diff type {aidiv_expr.numor} {bidiv_expr.numor}")
#             assert False

#     if isinstance(aidiv_expr.denom, _IDivExpr) and isinstance(bidiv_expr.denom, _IDivExpr):

#         if exact_match_idivexpr_recurse(aidiv_expr.denom,
#                                           bidiv_expr.denom):
#             # check modifiers
#             pass
#         else:
#             return False

#     elif isinstance(aidiv_expr.denom, _IDivExpr):
#         return False

#     elif isinstance(bidiv_expr.denom, _IDivExpr):
#         return False
    
#     else:
#         # both denom are non _IDivExpr 
#         if aidiv_expr.denom == bidiv_expr.denom:
#             logger.debug(f"denom: LHS == RHS due to type equality: {aidiv_expr.denom} {bidiv_expr.denom}")
#             return True
#         else:
#             return False
    

#     return False

# def exact_match_idivexpr(aidiv_expr, bidiv_expr):
#     if isinstance(aidiv_expr.numor, _IDivExpr) and isinstance(bidiv_expr.numor, _IDivExpr):
#         if exact_match_idivexpr_recurse(aidiv_expr.numor, bidiv_expr.numor):
#             pass
#         else:
            
#             return False
#     else:
#         try:

#             if aidiv_expr.numor.elabel != bidiv_expr.numor.elabel:
#                 logger.debug("mismatch at IDiv:numor.elabel")
#                 return False
#             else:
#                 #print(f"passes IDiv:numor.elabel equality{aidiv_expr.numor.elabel} {bidiv_expr.numor.elabel}" )
#                 pass
            
#         except:
#             logger.debug(f"Failed Test: aidiv_expr.numor and bidiv_expr.numor are of diff type {aidiv_expr.numor}  {bidiv_expr.numor}")
#             assert False

#     if isinstance(aidiv_expr.denom, _IDivExpr) and isinstance(bidiv_expr.denom, _IDivExpr):

#         if exact_match_idivexpr_recurse(aidiv_expr.denom,
#                                           bidiv_expr.denom):
#             # check modifiers
#             pass
#         else:
#             #print ("NotSame: under recurse")
#             return False

#     elif isinstance(aidiv_expr.denom, _IDivExpr):
#         return False

#     elif isinstance(bidiv_expr.denom, _IDivExpr):
#         return False
    
#     else:
#         # both denom are non _IDivExpr 
#         if aidiv_expr.denom == bidiv_expr.denom:
#             logger.debug(f"denom: LHS == RHS due to type equality:   {aidiv_expr.denom}  {bidiv_expr.denom}")
#             pass
#         else:
#             logger.debug(f"infer not same: demon unequal: {aidiv_expr.denom} {bidiv_expr.denom}")
#             return False
    
#     if aidiv_expr.modifier_chain == bidiv_expr.modifier_chain:
#         logger.debug("Passes modifier_chain equality")
#         return True
#     else:
#         logger.debug("Failed modifier_chain equality")
#         return False

#     return False


def is_same_class_idivexpr_recurse(aidiv_expr, bidiv_expr):
    """
    check if two idiv expr is same
    """

    assert isinstance(aidiv_expr, _IDivExpr)
    assert isinstance(bidiv_expr, _IDivExpr)

    if isinstance(aidiv_expr.numor, _IDivExpr) and isinstance(bidiv_expr.numor, _IDivExpr):
        if is_same_class_idivexpr_recurse(aidiv_expr.numor, bidiv_expr.numor):
            pass
        else:
            
            return False
    else:
        try:

            if aidiv_expr.numor.elabel != bidiv_expr.numor.elabel:
                logger.debug("mismatch at IDiv:numor.elabel")
                return False
            else:
                logger.debug(f"passes IDiv:numor.elabel equality  {aidiv_expr.numor.elabel} {bidiv_expr.numor.elabel}")
        except:
            logger.debug(f"Failed Test: aidiv_expr.numor and bidiv_expr.numor are of diff type {aidiv_expr.numor} {bidiv_expr.numor}")
            return False

    

    
    if isinstance(aidiv_expr.denom, _IDivExpr) and isinstance(bidiv_expr.denom, _IDivExpr):

        if is_same_class_idivexpr_recurse(aidiv_expr.denom,
                                          bidiv_expr.denom):
            # check modifiers
            pass
        else:
            return False

    elif isinstance(aidiv_expr.denom, _IDivExpr):
        return False

    elif isinstance(bidiv_expr.denom, _IDivExpr):
        return False
    
    else:
        # both denom are non _IDivExpr 
        if type(aidiv_expr.denom) == type(bidiv_expr.denom):
            logger.debug(f"denom: LHS == RHS due to type equality: {aidiv_expr.denom} {bidiv_expr.denom}")
            pass
        else:
            return False
    
    return True



def is_same_class_idivexpr(aidiv_expr, bidiv_expr):
    """
    check if two idiv expr is same
    """
    try:
        if aidiv_expr.numor.elabel != bidiv_expr.numor.elabel:
            logger.debug("mismatch at toplevel:numor:TagBase level")
            return False
        else:
            logger.debug(f"passes IDiv:numor.elabel equality {aidiv_expr.numor.elabel} {bidiv_expr.numor.elabel}")

    except:
        logger.debug("in no-mans-land: numor doesn't have elabel")
        assert False
        pass
    


    if isinstance(aidiv_expr.denom, _IDivExpr) and isinstance(bidiv_expr.denom, _IDivExpr):

        if is_same_class_idivexpr_recurse(aidiv_expr.denom,
                                          bidiv_expr.denom):
            # check modifiers
            pass
        else:
            return False
    
    elif isinstance(aidiv_expr.denom, _IDivExpr):
        logger.debug("infered-unequal: _IDivExpr vs othter type1:  {aidiv_expr.denom}  {bidiv_expr.denom}")
        return False

    elif isinstance(bidiv_expr.denom, _IDivExpr):
        logger.debug("infered-unequal: type2")
        return False
    
    else:
        # both denom are non _IDivExpr 
        if type(aidiv_expr.denom) == type(bidiv_expr.denom):
            logger.debug(f"denom: LHS == RHS due to type equality:  {aidiv_expr.denom} {bidiv_expr.denom}")
            pass
        else:
            logger.debug(f"infered-unequal: type(denom) unequal  {aidiv_expr.denom} {bidiv_expr.denom}")
            return False
    


    if aidiv_expr.modifier_chain == bidiv_expr.modifier_chain:
        return True


    
    


    # finally compare the modifier chains
    if aidiv_expr.modifier_chain == bidiv_expr.modifier_chain:
        logger.debug("Passes modifier_chain equality")
        return True
    else:
        logger.debug("Failed modifier_chain equality")
        return False

    return False


def exact_match_idivexpr(a, b, check_modifiers=True):
    """
    Determines if two Tailwind expressions are structurally identical.
    
    :param a: First expression/tag
    :param b: Second expression/tag
    :param check_modifiers: If True, validates the modifier_chain (e.g., hover:)
    """
    # 1. Base Case: If they aren't the same type, they aren't a match
    if type(a) != type(b):
        logger.debug(f"Type mismatch: {type(a)} vs {type(b)}")
        return False

    # 2. Handle _IDivExpr recursion
    if isinstance(a, _IDivExpr):
        # Check Numerators (Deep Recurse)
        if not exact_match_idivexpr(a.numor, b.numor, check_modifiers=False):
            return False
            
        # Check Denominators (Deep Recurse)
        if not exact_match_idivexpr(a.denom, b.denom, check_modifiers=False):
            return False

        # 3. Top-level Modifier Check
        if check_modifiers:
            if a.modifier_chain != b.modifier_chain:
                logger.debug(f"Modifier mismatch: {a.modifier_chain} != {b.modifier_chain}")
                return False
        
        return True

    # 4. Handle Terminal Tags (Base types with .elabel)
    if hasattr(a, 'elabel') and hasattr(b, 'elabel'):
        if a.elabel == b.elabel:
            return True
        logger.debug(f"Label mismatch: {a.elabel} != {b.elabel}")
        return False

    # 5. Handle Scalars/Enums (Leaf nodes)
    return a == b

def remove_from_twtag_list(twsty_taglist, twsty_tag):
    if isinstance(twsty_tag, Enum) or isinstance(twsty_tag, aenum.EnumType):
        twsty_taglist.remove(twsty_tag)
        return

    remove_idx = None
    for idx, _twtag in enumerate(twsty_taglist):
        if isinstance(_twtag, Enum) or isinstance(_twtag, aenum.EnumType):

            continue

        if exact_match_idivexpr(twsty_tag, _twtag):
            remove_idx = idx

            break
        
        pass

    if remove_idx is None:
        return


    twsty_taglist.pop(remove_idx)


def add_to_twtag_list_internal(twsty_taglist, twsty_tag):
    """
    add the twsty_tag to taglist; override existing elabel.
    TODO: bg/green/100, bg/opacity/50
    """
    # doesn't support conc of style_values Enum type
    if isinstance(twsty_tag, Enum) or isinstance(
            twsty_tag, aenum.EnumType
        ):

        raise ValueError("Do not support raw StyleValues: only IDivExpr")


    if issubclass(type(twsty_tag), TagBase):
        raise ValueError("Do not support raw TagBase: only IDivExpr")



    
    override_pos = None


        
    for idx, _twtag in enumerate(twsty_taglist):

        # if both are twtags
        if issubclass(type(_twtag), TagBase):
            raise ValueError("Do not support raw TagBase: only IDivExpr")
        
        elif is_same_class_idivexpr(twsty_tag, _twtag):
            override_pos = idx
            break

        
        
    if override_pos is not None:
        twsty_taglist[override_pos] = twsty_tag

    else:
        twsty_taglist.append(twsty_tag)


def conc_twtags(*args):
    res = []
    orig_twstr = [tstr(_) for _ in args]
    
    for twsty_tag in args:
        add_to_twtag_list_internal(res, twsty_tag)

    res_twstr = [tstr(_) for _ in res]
    if len(orig_twstr) == len(res_twstr):
        pass
    else:
        logger.debug (f"Review conc: orig : == {orig_twstr}")
        logger.debug (f"Review conc: final  == {res_twstr}")
    
    
    return res
