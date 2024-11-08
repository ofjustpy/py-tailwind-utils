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
from .style_tags import bg
from .style_tags import from_
from .style_tags import to_
from .style_tags import via_




def build_gradient_expr(from_color_idvexpr,
             to_color_idivexpr,
             via_color_idivexpr=None,
             *args,
             direction="bl"
             ):
    """
    for now only considering bg gradient;
    direction choices: t, r, b, l, tr, tl, br, bl, 
    
    """
    vias = []
    if args:
        vias = [gvia_/_ for _ in args]
        
    return [
        bg / "gradient-to-t",
        gfrom_ / from_color_idvexpr,
        gto_ / to_color_idivexpr,
        gvia_ / via_color_idivexpr,
        *vias
    ]

