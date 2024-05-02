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
import os
import sys

import aenum
from addict_tracking_changes import Dict
from aenum import Enum
import pysnooper
from .colors import _ColorBase


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class _IDivExpr:
    def __init__(self, tagstr, elabel, arg2, link=None):
        print("calling _IDivExpr:init : tagstr=", tagstr, " elabel= ", elabel, " arg2 = ", arg2)
        self.tagstr = tagstr
        self.arg2 = arg2
        self.elabel = elabel
        self.link = link
        self.modifier_chain = []

    def __truediv__(self, arg):
        print ("calling _IDivExpr:__truediv__", self.tagstr,
               " ", self.arg2, " ", arg)
        tt = self.arg2/arg
        # tt = _IDivExpr(self,
        #                self.arg2.elabel,
        #                arg)
        self.link = tt
        return self



    def evaluate(self, val=""):
        if isinstance(self.tagstr, str) and isinstance(self.arg2, _IDivExpr):
            return self.tagstr.format(val=self.arg2.evaluate(val))
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, TagBase):
            return self.tagstr.evaluate(self.arg2.evaluate(val))
        if isinstance(self.tagstr, _IDivExpr) and (
            isinstance(self.arg2, int) or isinstance(self.arg2, str) or isinstance(self.arg2, float)
        ):
            return self.tagstr.evaluate(str(self.arg2))
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, _ColorBase):
            aval = self.arg2.__truediv__(val)
            return self.tagstr.evaluate(val=aval)
        if isinstance(self.tagstr, str) and (
            isinstance(self.arg2, TagBase) or isinstance(self.arg2, _ColorBase)
        ):
            
            ares = self.arg2.evaluate(val)
            # hardwired :( <-- sad day for humanity
            if tstr(self.arg2) == "auto":
                ares = "-" + ares
            
            if val == "":
                # Note: for utility like max which can be used
                # max/w/0 (see https://tailwindcss.com/docs/max-width) and
                # also as H/max
                # for H/max we need to remove leading dash (-)

                if ares[-1] == "-":
                    ares = ares[:-1]


            # this can introduce double ; need a more logicial strategy
            tmp = self.tagstr.format(val=ares)
            return tmp.replace("--", "-")

        if isinstance(self.tagstr, str) and (
            isinstance(self.arg2, int) or isinstance(self.arg2, str) or isinstance(self.arg2, float)
        ):
            # this can introduce double ; need a more logicial strategy
            tmp = self.tagstr.format(val="-" + str(self.arg2))
            return tmp.replace("--", "-")
        if isinstance(self.tagstr, str) and (
            isinstance(self.arg2, Enum) or isinstance(self.arg2, aenum.EnumType)
        ):
            if self.elabel == "noop":
                return self.arg2.value
            else:
                raise ValueError("Don't combine with Enum with tags other than noop")
        print(
            "evaluate: unkown case ", type(self.tagstr), " ", type(self.arg2), " ", val
        )
        print("evaluate: unkown case ", self.tagstr, " ", self.arg2, " ", val)
        raise ValueError

    def keyvaleval(self, val=""):
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, TagBase):
            return self.tagstr.evaluate(self.arg2.keyvaleval(val))
        if isinstance(self.tagstr, _IDivExpr) and (
            isinstance(self.arg2, int) or isinstance(self.arg2, str)
        ):
            return self.tagstr.keyvaleval(str(self.arg2))
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, _ColorBase):
            aval = self.arg2.__truediv__(val)
            return self.tagstr.evaluate(val=aval)
        if isinstance(self.tagstr, str) and isinstance(self.arg2, TagBase):
            return (self.elabel, self.arg2.keyvaleval(val))  # looks suspicious

        if isinstance(self.tagstr, str) and isinstance(self.arg2, _ColorBase):
            return (self.elabel, self.arg2.keyvaleval(val))  # looks suspicious

        if isinstance(self.tagstr, str) and (
            isinstance(self.arg2, int) or isinstance(self.arg2, str)
        ):
            return (self.elabel, self.arg2)

        if isinstance(self.tagstr, str) and (
            isinstance(self.arg2, Enum) or isinstance(self.arg2, aenum.EnumType)
        ):
            if self.elabel == "noop":
                return (self.arg2.__class__.__name__, self.arg2.name)

            else:
                raise ValueError("Don't combine with Enum with tags other than noop")

        print(
            "evaluate: unkown case ", type(self.tagstr), " ", type(self.arg2), " ", val
        )
        print("evaluate: unkown case ", self.tagstr, " ", self.arg2, " ", val)
        assert 0


class TagBase:
    tagstr = None
    tagops = None
    taghelp = None
    elabel = None  # the label that ends up in the style expression

    @classmethod
    def __truediv__(cls, valprefix):
        print ("calling TagBase:__truediv__")
        tt = _IDivExpr(cls.tagstr, cls.elabel, valprefix)
        return tt
        # if isinstance(valprefix, TagBase)or isinstance(valprefix, _ColorBase):
        #     return _IDivExpr(cls.tagstr, valprefix)
        # return _IDivExpr(cls, valprefix)

    @classmethod
    def evaluate(cls, val):
        if isinstance(cls.tagstr, str) and (
                isinstance(val, int) or isinstance(val, str) or isinstance(val, float)
        ):
            # whats going on here?
            # margin is marked as m{val}
            # however if you see mr/4 introduce
            # then it should be rendered as m-4
            tmp = cls.tagstr.format(val="-" + str(val))
            return tmp.replace("--", "-")

        return cls.tagstr.format(val=val)

    @classmethod
    def keyvaleval(cls, val=None):
        # fres = cls.tagstr.format(val=val)
        # key = cls.tagstr.replace("{val}", "")
        # key = key.replace("-", "")
        if val == None or val == "":
            return (cls.elabel, cls.elabel)
        else:
            return (cls.elabel, val)


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
            res += f"{modifier_prefix}{prefix}" + arg.value + " "
        if isinstance(arg, _IDivExpr):
            evals = arg.evaluate()
            if evals[-1] == "-":
                evals = evals[:-1]
            res += f"{modifier_prefix}{prefix}" + evals + " "
        if isinstance(arg, TagBase):
            res += f"{modifier_prefix}{prefix}" + arg.tagstr + " "
        if isinstance(arg, str):
            res += f"{prefix}" + arg + " "


    res = res.strip()

    return res
    
#@pysnooper.snoop()    
def is_same_class_idivexpr_recurse(aidiv_expr, bidiv_expr):
    """
    check if two idiv expr is same
    """
    if aidiv_expr.elabel != bidiv_expr.elabel:
        return False
    if isinstance(aidiv_expr.arg2,
                  _IDivExpr) and isinstance(
                      bidiv_expr.arg2,
                      _IDivExpr
                  ):
        return is_same_class_idivexpr_recurse(aidiv_expr.arg2,
                                      bidiv_expr.arg2
                                      )
            
    elif type(aidiv_expr.arg2) == type(bidiv_expr.arg2):
        # we only check for class equivalence
        # hence W/32 is same as W/64
        # therefore only type is checked and not the actual value
        return True

    return False

#@pysnooper.snoop()    
def is_same_class_idivexpr(aidiv_expr, bidiv_expr):
    """
    check if two idiv expr is same
    """
    if aidiv_expr.elabel != bidiv_expr.elabel:
        return False
    if isinstance(aidiv_expr.arg2,
                  _IDivExpr) and isinstance(
                      bidiv_expr.arg2,
                      _IDivExpr
                  ):
        if is_same_class_idivexpr_recurse(aidiv_expr.arg2,
                                      bidiv_expr.arg2
                                      ):
            pass
        else:
            return False
        
    elif type(aidiv_expr.arg2) == type(bidiv_expr.arg2):
        # we only check for class equivalence
        # hence W/32 is same as W/64
        # therefore only type is checked and not the actual value
        # the type expression also works for idiv expression
        # over enum types
        pass
    else:
        return False
    
    


    # finally compare the modifier chains
    if aidiv_expr.modifier_chain == bidiv_expr.modifier_chain:
            return True

    return False
    
def remove_from_twtag_list(twsty_taglist, twsty_tag):
    if isinstance(twsty_tag, Enum) or isinstance(twsty_tag, aenum.EnumType):
        twsty_taglist.remove(twsty_tag)
        return

    remove_idx = None
    for idx, _twtag in enumerate(twsty_taglist):
        if isinstance(_twtag, Enum) or isinstance(_twtag, aenum.EnumType):
            continue
        if twsty_tag.elabel == _twtag.elabel:
            if type(twsty_tag.tagstr) == type(_twtag.tagstr):
                if isinstance(twsty_tag.tagstr, _IDivExpr):
                    if twsty_tag.tagstr.elabel == _twtag.tagstr.elabel:
                        if twsty_tag.tagstr.arg2 == _twtag.tagstr.arg2:
                            remove_idx = idx
                            break
                        else:
                            # lets not raise ValueError if you are trying to remove bg/green/100 but bg/blue/100 is present
                            # raise ValueError(
                            #     "Item not found: unable to remove ", tstr(twsty_tag)
                            # )

                            continue
                elif isinstance(twsty_tag, TagBase):
                    remove_idx = idx
                    break
                else:
                    if twsty_tag.arg2 == _twtag.arg2:
                        remove_idx = idx
                        break

    if remove_idx is None:
        # raise KeyError("Item not found: unable to remove ", tstr(twsty_tag))
        logger.info("unable to remove  {tstr(twsty_tag)}: no tag found")
        return

    assert remove_idx is not None
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
        
        assert False
    
    # ========================== Scenario 1 ==========================
    # twsty_tag is noop/x where x is a style-value
    if twsty_tag.elabel == "noop":
        override_pos = None
        if isinstance(twsty_tag.arg2, Enum) or isinstance(
            twsty_tag.arg2, aenum.EnumType
        ):
            for idx, _twtag in enumerate(twsty_taglist):
                if _twtag.elabel == "noop":
                    if isinstance(_twtag.arg2, Enum) or isinstance(
                        _twtag.arg2, aenum.EnumType
                    ):
                        if _twtag.arg2.__class__ == twsty_tag.arg2.__class__:
                            override_pos = idx
                            break

            if override_pos is not None:
                twsty_taglist[override_pos] = twsty_tag
                return
            else:
                twsty_taglist.append(twsty_tag)
                return

            
    tagclass = twsty_tag.elabel
    override_pos = None
    for idx, _twtag in enumerate(twsty_taglist):
        # Enum types have already been handled
        if isinstance(_twtag, Enum) or isinstance(twsty_tag, aenum.EnumType):
            continue

        # now both twsty_tag and _twtag are IDiv expressions
        if is_same_class_idivexpr(twsty_tag, _twtag):
            override_pos = idx
            break
        


    if override_pos is not None:
        # Output too verbose
        # logger.debug(
        #     f"override {tstr(twsty_taglist[override_pos])} with  {tstr(twsty_tag)}"
        # )
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
        print ("Review conc: orig : == ", orig_twstr)
        print ("Review conc: final  == ", res_twstr)
    
    
    return res
