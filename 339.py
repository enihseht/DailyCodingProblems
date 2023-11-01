import itertools


def test(array, k):
    array.sort()
    arr_rst = list(filter(lambda x: x < k, array))
    result = itertools.combinations(arr_rst, 3)
    for each in result:
        if sum(each) == k:
            print(each)
            return True
    return False


while True:
    k = input("Sum: >   ")
    try:
        k = int(k)
        break
    except ValueError:
        print("Invalid Input: Only Integers Are Accepted!")
        continue
arr = []
while True:
    n = input(">    ")
    if not n == "done":
        try:
            n = int(n)
            arr.append(n)
        except ValueError:
            print("Invalid Input: Only Integers Are Accepted!")
    else:
        break

print(test(arr, k))
