from collections import defaultdict

# create dict from keys
dictionary = dict.fromkeys(["one", "two", "three"])
# print(dictionary)

# --------

d = {"paulius": "black", "asta": "green", "tomas": "blue", "laura": "red"}
print(d)

# creatind dict from lists
names = ["paulius", "asta", "tomas", "laura"]
colors = ["black", "green", "blue", "red", "white", "green", "black"]

d1 = dict(zip(names, colors))
print(d1)

print(d == d1)

# looping over dict keys

for k in d:
    print(k)

for k in d.keys():
    if k.startswith("t"):
        print(k, d[k])

# looping over dict keys and values
# O() cheapest way:

for k, v in iter(d.items()):
    print(k, v)

# counting dict

c = {}
for color in colors:
    c[color] = c.get(color, 0) + 1
print(c)

# a better way
c = defaultdict(int)
print(c)
for color in colors:
    c[color] += 1
print(c)

# grouping with dict

c = defaultdict(list)
for name in names:
    key = len(name)
    c[key].append(name)
print(c)