input_numbers = input("Enter numbers seperated by space: ")
num_list = input_numbers.split()
num_list = [int(num) for num in num_list]
max_n= max(num_list)
print(max_n)