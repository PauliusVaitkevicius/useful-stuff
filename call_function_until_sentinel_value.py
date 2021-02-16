from functools import partial

with open("test_text.txt", "r") as f:
    blocks = []
    while True:
        block = f.read(5)
        if block == "":
            break
        blocks.append(block)
    print(blocks)

# a better way:
with open("test_text.txt", "r") as f:
    blocks = []
    for block in iter(partial(f.read, 5), ""):
        blocks.append(block)
    print(blocks)
