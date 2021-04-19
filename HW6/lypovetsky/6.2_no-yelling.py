# https: // www.codewars.com/kata/no-yelling
def filter_words(st):
    return " ".join(st.capitalize().split())


print(filter_words("HELLO    can YOU hear me"))
