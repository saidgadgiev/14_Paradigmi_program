"""Task 1"""
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()


n = int(input("Введите число n: "))
multiplication_table(n)

"""Выбор процедурного программирования обоснован простотой задачи и её структурой, которая предполагает 
последовательную обработку данных. Процедурное программирование позволяет легко организовать итерацию по
 числам и вывод на экран."""
