with open("file.txt") as file:
    content = file.read().strip()
# for i in content:
    # print((f"{i} - {len(i)}").strip())
    # print(i, end = "")

print(len(content.replace(" ", "").replace("\n", "")))
