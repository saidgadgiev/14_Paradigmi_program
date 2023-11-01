print('Задача №1 Дан список целых чисел numbers. Необходимо написать в императивном стиле \n '
      'процедуру для сортировки числа в списке в порядке убывания. \n Можно использовать любой алгоритм сортировки.\n')


def sort_list_imperativ(numbers):
    # Проверяем, что список не пуст
    if len(numbers) == 0:
        return numbers
    # Проходимся по списку и выполняем сравнение соседних элементов
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            # Если предыдущий элемент меньше следующего, меняем их местами
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers


print(sort_list_imperativ([9, 8, 7, 5, 2, 3, 4]))

print('\n\nЗадача №2 Написать точно такую же процедуру, но в декларативном стиле\n')


def sort_list_imperativ(numbers):
    print(sorted(numbers, reverse=True))


sort_list_imperativ([9, 8, 7, 5, 2, 3, 4])
