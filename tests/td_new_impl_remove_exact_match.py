from py_tailwind_utils import *
from py_tailwind_utils.common import exact_match_idivexpr


# res = exact_match_idivexpr(db.f, db.fi)
# print (res)

# res = exact_match_idivexpr(db.f, noop/container)
# print (res)

# res = exact_match_idivexpr(noop/container, noop/container)
# print (res)

# res = exact_match_idivexpr(twmax/screen/md, hover(twmax/screen/md)[0])
# print (res)

taglist = [noop/invisible, db.f, noop/container]
remove_from_twtag_list(taglist, noop/invisible)

print(taglist)



