temperatures = [10, 12, 14]

file = open("file.txt", "w")

for i in temperatures:
    file.writelines(f"{i}\n")

file.close()