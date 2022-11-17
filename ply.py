main = input().split()
n = int(main[0])
H = int(main[1])

main = input()
h = 0
c = 0
for i in main:
    if i == '(':
        if h < H:
            h += 1
        else:
            c += 1
            h -= 1
    else:
        if h > 0:
            h -= 1
        else:
            c += 1
            h += 1

print(c)
