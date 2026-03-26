# Average Numbers
# Samuel Renneke, 3/26/2026
def sum_numbers_from_file():
    total = 0
    try:
        with open("numbers.txt", "r") as f:
            for line in f:
                try:
                    number = int(line.strip())
                    total += number
                except ValueError:
                    print(f"ValueError, skipping {line.strip()}.")
    except IOError:
        print("IOError, could not read the file.")

    print(total)

if __name__ == '__main__':
    sum_numbers_from_file()
