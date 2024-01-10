files = ["a.txt", "b.txt", "c.txt"]
for i in files:
    file = open(i, "r")
    print(file.read())
    file.close()