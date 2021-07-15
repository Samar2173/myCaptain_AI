# list = list(map(int, input('Enter Integers seperated by ",": ').split(',')))
list1 = [12, -7, 5, 64, -14]
result = []
for i in list1:
    if i > 0:
        result.append(i)
print(f'Output: {result}')
