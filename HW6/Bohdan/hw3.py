user_str = input('Enter string\n>>>')


def calculate_included(st):
    """
    function that calculates the number of characters included in a given string

    :param st: user string
    :return: dict
    """
    st_set = set(user_str)
    dict_u = {}
    for i in st_set:
        dict_u.update({i: st.count(i)})
    return dict_u


print(calculate_included(user_str))

