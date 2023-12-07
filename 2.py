def get_block(size, start):
    block = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(start + i * size + j)
        block.append(row)
    return block

def swap_blocks(lst, n):
    size = len(lst)
    for i in range(0, size, n * 2):
        for j in range(n):
            for k in range(n):
                lst[i + j][k], lst[i + n + j][k] = lst[i + n + j][k], lst[i + j][k]

def print_list(lst):
    for row in lst:
        print(row)

block_size = 2  #Пример для N = 2

original_list = []
for i in range(1, 2 * block_size + 1):
    original_list += get_block(block_size, i)

print("Исходный список:")
print_list(original_list)

modified_list = original_list.copy()

swap_blocks(modified_list, block_size)

print("Измененный список после перестановки блоков:")
print_list(modified_list)

#Неправильно, я не понял как это сделать.