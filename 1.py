"""Задание #1
Обработать любое изображение: Нарисовать горизонтальную линию по центру, повернуть на 75°, уменьшить мастшаб на 90%, написать текст в произвольном месте"""
import cv2
import numpy as np
def show_img(img, window_name="Image"):
    """Функция для отображения изображения"""
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Загружаем изображение
img = cv2.imread("Tosha.png")
# Проверяем, загрузилось ли изображение
if img is None:
    exit()
# Получаем размеры изображения
H, W = img.shape[:2]
print(f"Размер изображения: {W}x{H}")
# Создаем копию для обработки
result = img.copy()

# 1. Рисуем горизонтальную линию по центру
RGB_LINE = (0, 255, 0)  # Зеленый цвет
LINE_PX = 5
cv2.line(result, (0, H // 2), (W, H // 2), RGB_LINE, LINE_PX)

# 2. Поворачиваем на 75°
ANGLE = 75
CENTER = (W // 2, H // 2)
matrix = cv2.getRotationMatrix2D(CENTER, ANGLE, 1.0)
result = cv2.warpAffine(result, matrix, (W, H))

# 3. Уменьшаем масштаб на 90% (оставляем 10% от исходного размера)
SCALE = 0.1  # 90% уменьшение = остаётся 10% от исходного размера
new_width = int(W * SCALE)
new_height = int(H * SCALE)
result = cv2.resize(result, (new_width, new_height), interpolation=cv2.INTER_AREA)

# 4. Добавляем текст "super dog" в произвольном месте
RGB_TEXT = (255, 0, 0)  # Синий цвет (BGR: Blue, Green, Red)
TEXT_PX = 2  # Толщина текста
TEXT_SCALE = 0.9  # Размер шрифта

# Выбираем произвольное место для текста (нижний правый угол с отступом)
text_position = (10, new_height - 10)  # Левая нижняя часть
cv2.putText(result, "super dog", text_position, cv2.FONT_HERSHEY_SIMPLEX, 
            TEXT_SCALE, RGB_TEXT, TEXT_PX)

# Показываем и сохраняем результат
show_img(result, "Итоговое изображение")
# Сохраняем результат
cv2.imwrite("Tosha_final.png", result)
print(f"Размер итогового изображения: {new_width}x{new_height}")

