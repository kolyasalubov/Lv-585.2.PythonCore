def filter_words(st):
    st =" ".join(st.split())
    st_return = st[0].upper()+st[1:].lower()
    return st_return
