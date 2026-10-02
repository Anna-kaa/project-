with open('24.txt') as f:
    s = f.readline()

# Находим индексы всех букв 'A' в строке
pos = [i for i, char in enumerate(s) if char == 'A']

max_len = 0

# Нам нужно 4 буквы A, поэтому идем по индексам до len(pos) - 3
for i in range(len(pos) - 3):
    # Индексы четырех последовательных букв A
    i1, i2, i3, i4 = pos[i], pos[i+1], pos[i+2], pos[i+3]
    
    # Выделяем группы символов между буквами A
    sub1 = s[i1 + 1 : i2]
    sub2 = s[i2 + 1 : i3]
    sub3 = s[i3 + 1 : i4]
    
    # Проверяем, что группы одинаковы (условие "не содержат A" выполняется автоматически, 
    # так как мы берем символы строго между соседними A)
    if sub1 == sub2 == sub3:
        # Длина всей строки от первой A до последней A
        current_len = i4 - i1 + 1
        max_len = max(max_len, current_len)

print(max_len)
