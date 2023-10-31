while True:
    n = input("n: ")
    try:
        n = int(n)
        i = 1
        while True:
            if bin(n).count("1") == bin(n + i).count("1"):
                print(n + i)
                break
            else:
                i += 1
        break
    except ValueError:
        print("n must be an integer")
