n = int(input())
result = 0

hour_in_3 = 3600
hour_not_in_3 = 1575

count = 0
for minute in range(60):
    char_minute = list(str(minute))
    if '3' in char_minute:
        count += 60
    else:
        for second in range(60):
            char_second = list(str(second))
            if '3' in char_second:
                count += 1

for i in range(n+1):
    char_i = list(str(i))
    if '3' in char_i:
        result += hour_in_3
    else:
        result += hour_not_in_3

print(result)