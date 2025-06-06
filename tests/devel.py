from py_tailwind_utils import *

from addict_tracking_changes import Dict
from py_tailwind_utils.to_twsty_expr import encode_twstr

# print(tstr(noop/mr/4))

# test if dsearch

# ui_app_trmap = Dict(track_changes=True)
# ui_app_trmap.hello.alpha.beta = 5

# if list(dsearch(ui_app_trmap, "/hello/alpha/beta/gamma")):
#     print("path exists")
    
#print (list(dsearch(ui_app_trmap, "/hello")))

# ec = encode_twstr("hover:table-column-group")
# print (tstr(*ec))

# ================================ BUG ===============================
# BUG: get_color_value didn't address 500/50
# ec = encode_twstr("border-indigo-500/50")
# print (tstr(*ec))

# ================================ BUG ===============================
# ec = encode_twstr("group-hover:underline")
# ec = encode_twstr("group-hover:underline")
# ec = encode_twstr("group-hover:underline")
# print (tstr(*ec))

ec = encode_twstr("-space-x-px")
print(ec)
print (tstr(*ec))



