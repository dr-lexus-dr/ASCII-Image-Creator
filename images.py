import cv2
import os

#string = " `.,-':<>;+!*/?%&98#"
string = " 123456789"

coef = 255 / (len(string) - 1)

# Запрос имени файла у пользователя
filename = input("Введите имя файла (с расширением): ")

# Проверка существования файла
if not os.path.exists(filename):
    print(f"Файл '{filename}' не найден!")
    exit()

# Загрузка изображения
image = cv2.imread(filename)

# Проверка успешной загрузки
if image is None:
    print(f"Ошибка загрузки файла '{filename}'!")
    exit()

height, width, channels = image.shape

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

with open("ASCII_Art.txt", "a") as file:
    for x in range(0, width - 1, 8):
        s = ""
        for y in range(0, height - 1, 4):
            try:
                s += string[len(string) - int(gray_image[x, y] / coef) - 1]
                continue
            except IndexError:
                pass
        if len(s) != 0:
            file.write(s + "\n")

print(f"ASCII-арт успешно создан из файла '{filename}'!")