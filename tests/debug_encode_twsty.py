from py_tailwind_utils import *

# case 1: use to not work
# twsty_tags = np/start/twpx
# print (tstr(twsty_tags))

# ================================ end ===============================

# # case 2:

# twsty_tags = twmax/W/screen/"md"
# print(tstr(twsty_tags))

# enc_twsty_tags = encode_twstr("max-w-screen-md")

# print (tstr(*enc_twsty_tags))
# fix: changed screen to screen-{val}

# ====================================================================

# case 3

# twsty_tags = bg/gradient/to_/sr
# print(tstr(twsty_tags))
# enc_twsty_tags = encode_twstr("bg-transparent bg-gradient-to-r")
# print(tstr(*enc_twsty_tags))

# brute force fix
# ====================================================================

# # case 4
# enc_twsty_tags = encode_twstr("hover:via-gray-100/50")
# print(tstr(*enc_twsty_tags))

#fix: use 100/50 instead of 100/5
# ====================================================================


# case 5

# twsty_tags = underline/offset/5
# #print(tstr(twsty_tags))
# enc_twsty_tags = encode_twstr("underline-offset-5")
# X = enc_twsty_tags[0]
# print (type(X))
# # print (X.arg2)
# # print (X.arg2.elabel)
# # print (X.arg2.arg2)
# # print (X.arg2.)
# print(tstr(X))

# #fix: underline was defined in 2 places : one with val and another without it.



#case 6
# twsty_tags = top/auto
# print (tstr(twsty_tags))
#twsty_tags = "group-open:top-auto"

# fix. preprocess self.tagstr.format to remove -- with -
# ================================ end ===============================


#case 6: text-gray-900/75
# twsty_tags = fc/gray/"900/75"
# print (tstr(twsty_tags))

#fixed by code modification: if len(colorval) == 1 and colorval[-1] != "0":

# case 7
# bg-clip-text
