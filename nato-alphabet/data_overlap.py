with open("./nato-alphabet/data/file1.txt") as first_file:
    first_data_portion = first_file.readlines()
    first_numbers = [int(n.strip()) for n in first_data_portion]

with open("./nato-alphabet/data/file2.txt") as second_file:
    second_data_portion = second_file.readlines()
    second_numbers = [int(n.strip()) for n in second_data_portion]

result = [n for n in first_numbers if (n in second_numbers)]
print(result)
