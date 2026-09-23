import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)

x = re.split(r"\s", txt, 1)
print(x)
