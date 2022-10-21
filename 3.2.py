# fib_numbers = {0: 0, 1: 1}
#
#
# def calculate_fib(num):
#     global fib_numbers
#     if num in fib_numbers:
#         pass
#     else:
#         key2 = list(fib_numbers)[-1]
#         key = list(fib_numbers)[-2]
#         while fib_numbers[key2] < num:
#             key3 = key + key2
#             fib_numbers[key3] = key3
#             key, key2 = key2, key3
#         if num < fib_numbers[key2]:
#             return -1
#         key3 = key + key2
#         fib_numbers[key3] = key3
#         return key3
#
def calculate_fib(num):
    f1=1
    f2=1
    while f2<=num:
        f3=f1+f2
        f1,f2=f2,f3
    return[f1,f2]

str_numbers = input("введите вектора:")
numbers=str_numbers.split(' ')
for i in range(len(numbers)):
    x=int(numbers[i])
    f=calculate_fib(x)
    if x==f[0]:
        numbers[i]=str(f[1])

print(' '.join(numbers))

