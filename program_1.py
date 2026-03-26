# Item Counter
# Samuel Renneke, 3/26/2026

def count_file_lines():
    file = open("names.txt", "r")
    names = file.readlines()
    print(len(names))
    file.close()

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
