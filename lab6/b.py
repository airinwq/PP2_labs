import os

#1
def l(path):
    items = os.listdir(path)
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    print("Directories:", dirs)
    print("Files:", files)
    print("All items:", items)
l("./")

#2
def check(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
check("./dir3.py")

#3
def test_path_details(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path doesnt exist")
test_path_details("./dir4.py")

#4
def count_l(file_path):
    counter = 0
    with open(file_path, 'r') as file:
        for line in file:
            counter += 1
    return counter
print("Num of lines:", count_l("./dir5.py"))

#5
def write(list_items, file_path):
    with open(file_path, mode='w') as file:
        for item in list_items:
            file.write(f"{item}\n")
write([1, 2, 3, 4, 5], './list_elements.txt')

#6
import string
def gen():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            pass
gen()

#7
import shutil
def copy_file(source_path, destination_path):
    shutil.copy(source_path, destination_path)

#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("error")