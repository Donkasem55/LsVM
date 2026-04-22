import sys

while True:
    x = input(f"[hex {[i.split("\\") for i in sys.argv[1].split("/")][-1][-1]}]# ")
    if x == "q":
        break
    elif x[0] == "a":
        with open(sys.argv[1], "ab") as f:
            f.write("".join(x[1:]).encode("utf-8"))
    elif x[0] == "f":
        with open(sys.argv[1], "rb") as f:
            a = f.read()
        with open(sys.argv[1], "wb") as f:
            f.write("".join(x[1:]).encode("utf-8") + a)
    elif x[0] == "p":
        with open(sys.argv[1], "rb") as f:
            for i in f.read():
                print(str(i), end=" ")
            print()
    elif x[0] == "l":
        with open(sys.argv[1], "rb") as f:
            print(len(f.read()))
    elif x[0] == "d":
        with open(sys.argv[1], "rb") as f:
            a = f.read()
        with open(sys.argv[1], "wb") as f:
            f.write(a[1:])
    elif x[0] == "r":
        with open(sys.argv[1], "rb") as f:
            a = f.read()
        with open(sys.argv[1], "wb") as f:
            f.write(a[:-1])
    elif x[0] == "b":
        with open(sys.argv[1], "rb") as f:
            a = f.read()
        with open(sys.argv[1], "wb") as f:
            f.write(b"")
        with open(sys.argv[1], "ab") as f:
            for i in x.split(" ")[1:]:
                f.write(chr(int(i, 0)).encode("utf-8"))
            f.write(a)
    else:
        with open(sys.argv[1], "ab") as f:
            for i in x.split(" "):
                f.write(chr(int(i, 0)).encode("utf-8"))
