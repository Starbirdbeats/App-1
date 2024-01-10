contents = ["words words words", "New Words, New Words, New Words", "Old Words, Old Words, Old Words"]
docs = ['one.txt', 'two.txt', 'three.txt']

directory = r'C:\Users\PistolPerks\Documents\Coding Practice\App 1\files'

for content, file in zip(contents, docs):
    file = open(fr'C:\Users\PistolPerks\Documents\Coding Practice\App 1\files/{file}', 'w')
    file.write(content)