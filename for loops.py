# distinguishing multiple exit points in loops

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    # else belongs to FOR loop; if NO BRAKE exists
    else:
        return -1
    return i


# multiple state variables: update state all at once

def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        print(x)
        x, y = y, x + y


if __name__ == "__main__":

    # print(find("laba diena", "a"))

    print(fibonacci(10))
