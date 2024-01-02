
import os
print(__file__)

def read_write(m : str):
    with open(m, 'r+') as file:
        file.write("this gotta be the best to read && write")

        file.seek(0)

        content = file.read()
        print(content)
path = f'{os.getcwd()}/notes.txt'
# print(path)
read_write(path)
# read_write(__file__)