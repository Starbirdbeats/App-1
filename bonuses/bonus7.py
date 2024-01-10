filenames = ["1.doc", "2.report", "3.presentation"]

filenames = [f'{filename.replace(".", " - ")}.txt' for filename in filenames]

print(filenames)