import random

def generate_random_set(size):
    return set(random.randint(1, 100) for _ in range(size))

size_set1 = 15
size_set2 = 15

#Генерируем два случайных множества:
set1 = generate_random_set(size_set1)
set2 = generate_random_set(size_set2)

print("Первое множество:", set1)
print("Второе множество:", set2)

#Находим пересечение множеств и сортируем результат:
common_elements = sorted(set1.intersection(set2))

print("\nЧисла, входящие в оба множества в порядке возрастания:")
print(common_elements)