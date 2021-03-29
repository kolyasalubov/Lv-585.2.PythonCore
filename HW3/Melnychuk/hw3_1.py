zen_python = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

#counting

count_of_better = zen_python.count("better")
count_of_never = zen_python.count("never")
count_of_is = zen_python.count("is")

print(f"\"better\" in text {count_of_better} times")
print(f"\"never\" in text {count_of_never} times")
print(f"\"is\" in text {count_of_is} times")

#capital letters

up_zen_python = zen_python.upper()
print(up_zen_python)

#replacing

replaced_zen_pyhon = zen_python.replace("i", "&")
print(replaced_zen_pyhon)