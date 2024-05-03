# bg_color = "bg-gray-100"
# text_color= "text-gray-700"
# twsty_tags = conc_twtags(*encode_twstr(f"group flex items-center justify-between rounded-lg {bg_color} px-4 py-2 {text_color}"), *twsty_tags)

# # a bug in encoding

from py_tailwind_utils import *

# case 1
# twsty_tags = [W/64, mr/st/"0.5"]
# res = conc_twtags(*twsty_tags)
# print(tstr(*res))

# # case 2: 
# twsty_tags=encode_twstr("bg-gray-300 peer-checked:bg-gray-300")

# t1 = twsty_tags[0]
# t2 = twsty_tags[1]
# res = conc_twtags(t1, t2)
# print(tstr(*res))


# case 3
# twsty_tags = [noop/peer, srs.only]
# twsty_tags=encode_twstr("peer sr-only")
# t1 = twsty_tags[0]
# t2 = twsty_tags[1]
# res = conc_twtags(t1, t2)
# print(tstr(*res))

#case 4

#twsty_tags = [boxtopo.bd, boxtopo.bd]
# twsty_tags=encode_twstr("border border")
# t1 = twsty_tags[0]
# t2 = twsty_tags[1]
# res = conc_twtags(t1, t2)
# print(tstr(*res))

#case 5
# twsty_tags = [bg/gray/100,  fc/gray/200]
# t1 = twsty_tags[0]
# t2 = twsty_tags[1]
# res = conc_twtags(t1, t2)
# print(tstr(*res))

# case 6
# twsty_tags = [W/screen/sm,  W/screen/md]
# t1 = twsty_tags[0]
# t2 = twsty_tags[1]
# res = conc_twtags(t1, t2)
# print(tstr(*res))


#case 7
print(tstr(twmax/W/screen/md))

# twsty_tags = [twmax/W/screen/md, twmax/W/screen/md]
# t1 = twsty_tags[0]
# t2 = twsty_tags[1]
# res = conc_twtags(t1, t2)
# print(tstr(*res))
