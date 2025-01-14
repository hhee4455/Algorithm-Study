s = sorted(list(input()))
array = []
total = 0  

for char in s:
    if ord(char) >= ord("A"):
        array.append(char)
    else:
        total += int(char)

print(''.join(array) + str(total))
