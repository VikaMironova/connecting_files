
open("общее.txt","w").write(open("1.txt","r").read() + open("2.txt","r").read())
count_1 = 0
count_2 = 0
list_1 = []
list_2 = []


print("1.txt")
with open('1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        count_1 += 1
        x = line[:-1]
        list_1.append(x)
        print(f"Строка номер {count_1} файла номер 1")
print(len(list_1))

print("2.txt")
with open('2.txt', 'r', encoding='utf-8') as file_1:
    for line_1 in file_1:
        count_2 += 1
        y = line_1[:-1]
        list_2.append(x)
        print(f"Строка номер {count_2} файла номер 2")
print(len(list_2))

if len(list_1) < len(list_2):
    res_1 = list_1 + list_2

if len(list_1) > len(list_2):
    res_2 = list_2 + list_1
