import numpy as np


class Number:
    def __init__(self, indeces, prev, following):
        self.indeces = indeces
        self.prev = prev
        self.following = following


class List:
    def __init__(self, num):
        self.start = num
        self.end = self.start

    def add_number(self, indeces):
        self.end.following = Number(indeces, self.end, None)
        self.end = self.end.following


def find_indices(minimum, list_to_check, item_to_find):
    list_to_check = np.array(list_to_check)
    list_to_check = np.where(list_to_check == item_to_find)
    list_to_check = np.array(list_to_check)
    list_to_check = list_to_check[list_to_check > minimum]
    return list_to_check


def fix(list_to_fix, maximum):
    list_to_fix = np.array(list_to_fix)
    list_to_fix = list_to_fix[list_to_fix < maximum]
    return list_to_fix


main = input().split()
n = int(main[0])
m = int(main[1])
k = int(main[2])

bajtek = input().split()
bitek = input().split()

numbers = List(Number(find_indices(-1, bajtek, bitek[0]), None, None))
for i in range(1, m):
    numbers.add_number(find_indices(numbers.end.indeces[0], bajtek, bitek[i]))

number = numbers.end
number = number.prev
while number is not None:
    number.indeces = fix(number.indeces, number.following.indeces[-1])
    number = number.prev

for i in range(0, n):
    bajtek[i] = '0'
unique_list = []
number = numbers.start

while number is not None:
    for j in number.indeces:
        if j not in unique_list:
            unique_list.append(j)
    number = number.following

for i in unique_list:
    bajtek[i] = '1'

print(*bajtek, sep=" ")
