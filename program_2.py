# Random Number File Writer
# Samuel Renneke, 3/26/2026
import random
def random_numbers():
    numbers = open("numbers.txt", "w")
    how_many = int(input("How many numbers do you want? (up to 1000) "))
    for i in range(how_many):
        random_number = random.randint(1, 500)
        if i == 0:
            numbers.write(str(random_number))
        else:
            numbers.write(f"\n {str(random_number)}")
    numbers.close()

random_numbers()
