import numpy as np

def find_indices(list_to_check, item_to_find):
    array = np.array(list_to_check)
    indices = np.where(array == item_to_find)[0]
    return list(indices)

# def is_bigger_present(list_to_check, item_to_check):
#     if item_to_check == None:
#         return None
#     for i in list_to_check:
#         if i>item_to_check:
#             return i
#     return None

def is_bigger_present(list_to_check, item_to_check, k, result, m):
    if k == m-1:
        for i in list_to_check[k]:
            if i > item_to_check:
                result.append(i)
                return i
    for i in list_to_check[k]:
        if i > item_to_check:
            if is_bigger_present(list_to_check, i, k+1, result, m):
                result.append(i)
                return i


# def func(list_to_check):
#     result = []
#     # for i in indeces[0]:
#     #     if is_bigger_present(indeces[3], is_bigger_present(indeces[2], is_bigger_present(indeces[1], i))):
#     #         result.append(i)
#     for i in range(0, len(list_to_check)):
#         for j in i:
#             if is_bigger_present(i+1, j)

main = input().split()
n = int(main[0])
m = int(main[1])
k = int(main[2])
unique_list = []

bajtek = input().split()
bitek = input().split()

indeces = []
for i in bitek:
    indeces.append(find_indices(bajtek, i))

result = []
if len(indeces) > 1:
    for i in indeces[0]:
        if is_bigger_present(indeces, i, 1, result, m) != None:
            result.append(i)
else:
    result = indeces[0]


for x in result:
    if x not in unique_list:
        unique_list.append(x)

final = []

for i in range(0, n):
    final.append(0)

for i in range(0, len(unique_list)):
    final[unique_list[i]] = 1

print(*final, sep=" ")