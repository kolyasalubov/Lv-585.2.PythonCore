string = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

# 1-st task
a = "better"
b = "never"
c = "is"

count_a = string.count(a)
count_b = string.count(b)
count_c = string.count(c)
print("Count words:", count_a, count_b, count_c)

# 2-nd task
print("Upper string:", string.upper())

# 3-rd task
print("Replace task:", string.replace("i", "&"))
