def are_you_playing_banjo(name):
    if name[0] == "R":#
#         return(name + " plays banjo")
    elif name[0] == "r":
        return(name + " plays banjo")
    else:
        return(name + " does not play banjo")
    return are_you_playing_banjo(name)

# name = "lolik"
# print(name[0])
# if name[0] == "R" or "r":
#     print(name + " plays banjo")
# else:
#     print(name + " does not play banjo")
# # print(name + " plays banjo" if name[0] == "R" or "r" else name + " does not play banjo")
# print(name[0] == "t")
# чому не працює?
