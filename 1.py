def find_matching_rows_and_columns(matrix):
    n = len(matrix)

    for k in range(n):
        is_matching = True

        # Проверяем, совпадает ли k-я строка с k-м столбцом
        for i in range(n):
            if matrix[k][i] != matrix[i][k]:
                is_matching = False
                break

        # Если строки совпадаю��, выводим номер строки (k)
        if is_matching:
            print(f"Строка {k + 1} совпадает с {k + 1}-м столбцом")


# Запрашиваем размер матрицы у пользователя
n_str = input("Введите размер матрицы (N): ")

# Преобразуем введенную строку в целое число
n = int(n_str)

# Инициализируем матрицу
matrix = []

# Заполняем матрицу значениями, можно также запросит�� их у пользователя
for i in range(n):
    row = []
    for j in range(n):
        # Запрашиваем элемент матрицы у пользователя
        element_str = input(f"Введите элемент матрицы ({i + 1}, {j + 1}): ")
        # Преобразуем введенную строку в целое число
        row.append(int(element_str))
    # Добавляем строку в матрицу
    matrix.append(row)

# Вызываем функцию для поиска совпадающих строк и столбцов
find_matching_rows_and_columns(matrix)


