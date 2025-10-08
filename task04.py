file = open("input/numbers.txt")
numbers = file.read()
file.close()


numbers_list = [int(num) for num in numbers.split()]

progress = numbers_list

odd_num = list(filter(lambda a: a % 2 != 0, numbers_list))

file = open("output/output04.txt", "w")
file.write(f"Progress: {progress}\nOdd numbers: {odd_num}")
file.close()
