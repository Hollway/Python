

def func(a: int, b: int) -> int:
    """Summ 2 int values

    :param a: first digint
    :type a: int
    :param b: second digit
    :type b: int
    :return: summ
    :rtype: int
    """    
    return a + b


func(2, 3)

def check_n():
    n = int(input("Задайте размер таблицы n x n: "))
    while True:
        if n < 1 or n > 10**5:
            print("Некорректный ввод. Повторите еще раз")
        else:
            return n

def check_k():
    k = int(input("Задайте параметр k "))
    while True:
        if k < 1 or k > 10**9:
            print("Некорректный ввод. Повторите еще раз")
        else:
            return k
n = check_n()
k = check_k()

# decorator 