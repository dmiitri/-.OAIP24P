import os
import shutil
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

print("Файл data.txt создан и заполнен")
with open("data.txt", "r", encoding="utf-8") as file:
    print("\nСодержимое файла:")
    for line in file:
        print(line.strip())
with open("data.txt", "r", encoding="utf-8") as file:
    print("\nПозиция курсора в начале:", file.tell())
    file.readline()
    print("Позиция курсора после чтения строки:", file.tell())

    file.seek(0)
    print("Курсор возвращён в начало")
shutil.copy("data.txt", "data_copy.txt")
print("\nФайл скопирован в data_copy.txt")
if os.path.exists("data_copy.txt"):
    print("Копия файла существует")
os.remove("data.txt")
print("Оригинальный файл data.txt удалён")
