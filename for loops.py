# distinguishing multiple exit points in loops

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    # else belongs to FOR loop if NO BRAKE exists
    else:
        return -1
    return i


if __name__ == "__main__":

    print(find("laba diena", "a"))


