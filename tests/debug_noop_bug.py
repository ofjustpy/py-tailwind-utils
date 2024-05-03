from py_tailwind_utils import *

# t1 = mr/st/"0.5"
# t2 = noop/W/64

# print(tstr(t1), tstr(t2))
twsty_tags=encode_twstr("mt-0.5  w-64")
#print(tstr(twsty_tags[0]), tstr(twsty_tags[1]))
res = conc_twtags(twsty_tags[0], twsty_tags[1])
# print (res)
# res = conc_twtags(t1, t2)

# print(res)
