"""
Status: not pursuing the idea of wrap/text wrap/line etc. 
"""
from .style_tags import (text)
from .common import TagBase, _IDivExpr


class _IDivExprShorted(_IDivExpr):
    def __truediv__(self, arg):
        assert False    

    def evaluate(self, val=None):
        assert self.numor == _Wrap
        assert self.denom == text
        
        assert val == None
        
        return "hello"
    

class _Wrap:
    tagstr = "wrap"
    tagops = []
    taghelp = "wrap"
    elabel = "wrap"
    stemval = "wrap"
    
    @classmethod
    def __truediv__(cls, denom):
        """
        note: we loose the wrap instance/object 
        """
        assert denom == text
        return _IDivExprShorted(cls, denom, modifier_chain=[])



wrap = _Wrap()
