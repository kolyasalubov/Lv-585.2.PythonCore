# Записати в стрічку філософію Пайтона
zen_of_python = """Beautiful is better than ugly.
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

print(
    "Zen of Python:",
    zen_of_python,
    sep="\n"
)

# Знайти в заданій стрічці кількість
# входжень слів (better, never, is)
countBetter = zen_of_python.count("better")
countNever = zen_of_python.count("never")
countIs = zen_of_python.count("is")
print(
    "___\nThe count is:\n",
    countBetter, " 'better'\n",
    countNever, " 'never'\n",
    countIs, " 'is'\n",
    sep=""
)  # \n for visual purpuses in terminal

# Вивести весь текст у верхньому регістрі(всі великі літери)
print(
    "___\nTo uppercase:\n",
    zen_of_python.upper(),
    sep=""
)

# Замінити всі входження символу “і” на “&”
print(
    "___\nAll «i» → «&»:\n",
    zen_of_python.replace("i", "&"),
    sep=""
)
