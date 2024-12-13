# testing all combination of removal for page-style-editor

# ====================================================================
# single utility class like container
from py_tailwind_utils import *
to_remove = encode_twstr("container")

twarr = [noop/container, bg/green/100]
remove_from_twtag_list(twarr, to_remove[0])

print("no container = ", tstr(*twarr))

# ====================================================================
# utility class with value : e.g. pd/1
to_remove = encode_twstr("p-1")

twarr = [pd/1, bg/green/100]
remove_from_twtag_list(twarr, to_remove[0])

print("no pd/1 = ", tstr(*twarr))

# ====================================================================
# utility class/facet/value, e.g. bg/green/1, or mr/st/1
to_remove = encode_twstr("bg-green-100")

twarr = [pd/1, bg/green/100]
remove_from_twtag_list(twarr, to_remove[0])

print("no bg/green/100 = ", tstr(*twarr))

# ====================================================================
#style values e.g. flxw

to_remove = encode_twstr("flex-wrap")

print (tstr(*to_remove))
twarr = [flxw.w, pd/1, flxdir.col
         ]
remove_from_twtag_list(twarr, to_remove[0])

print("no flex-wrap = ", tstr(*twarr))

# ===================== is removal value agnostic ====================
# Removal is done on exact value
to_remove = encode_twstr("p-5")

print (tstr(*to_remove))
twarr = [flxw.w, pd/1, flxdir.col
         ]
remove_from_twtag_list(twarr, to_remove[0])

print("padding gone? = ", tstr(*twarr))

