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
import json
import os

from addict_tracking_changes import Dict
from .common import _IDivExpr, _ColorBase

# class _ColorBase:
#     mycolor = None
#     elabel = "color"
#     tagstr = None
    
#     @classmethod
#     def __truediv__(cls, colorval: str):
#         #return _IDivExpr(cls, colorval)
#         return cls.evaluate(str(colorval))

#     @classmethod
#     def evaluate(cls, colorval: str):
#         if colorval == None:
#             return cls.mycolor
        
#         if colorval == "":
#             return cls.mycolor
        
#         if colorval == "0":
#             return cls.mycolor
#         # we are nolonger auto filling color val from 5 to 500
#         # if len(colorval) == 1 and colorval[-1] != "0":
#         #     # letting go of the idea of using short form
#         #     assert False
#         #     #return f"{cls.mycolor}-{colorval}00"
#         else:
#             return f"{cls.mycolor}-{colorval}"
#         pass

#     @classmethod
#     def keyvaleval(cls, colorval: str):
#         return cls.evaluate(colorval)

#     # @ classmethod
#     # def __pow__(cls, colorval):
#     #     print("In __pw")
#     #     return f"{cls.mycolor}-{colorval}00"

#     @classmethod
#     def __repr__(cls):
#         return f"{cls.mycolor}"


slate = (
    gray
) = (
    zinc
) = (
    neutral
) = (
    stone
) = (
    red
) = (
    orange
) = (
    amber
) = (
    yellow
) = (
    lime
) = (
    green
) = (
    emerald
) = teal = cyan = sky = blue = indigo = violet = purple = fuchsia = pink = rose = None




onetonine = ["_", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]

with open(os.path.dirname(__file__) + "/palette-v2x.json", "r") as fh:
    _twccd = json.load(fh)

twcc2hex = Dict()
for cc in _twccd.keys():
    if cc not in ["black", "white"]:
        for i in range(1, 10):
            rn = onetonine[i]
            twcc2hex[cc][rn] = _twccd[cc][f"{i}00"]


def color2hex(twcc):
    basecolor, scale = twcc.split("-")
    if basecolor in _twccd.keys():
        if scale in _twccd[basecolor]:
            return _twccd[basecolor][scale]
        raise ValueError(f"{scale} not found in _twccd", _twccd[basecolor].keys())
    raise ValueError


