str_numbers=input("введите вектор:")
numbers = str_numbers.split(' ')
max_number=int(numbers[0])
for i in range(1,len(numbers)):
    if int(numbers[i])>max_number:
        max_number = int(numbers[i])
print(max_number)
# 6 64 89 222 13 62 5