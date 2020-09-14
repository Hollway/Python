from functools import wraps

A = []

args = input("Введите входные данные n и k: ")
argsSplit = args.split(" ")
n = int(argsSplit[0]) + 1
k = int(argsSplit[1])


def decor(abt):
    """Декоратор"""
    A.append(abt.__name__)

    @wraps(abt)
    def _executor():
        print(  "\n{:-^35}".format(""),
                "\n{:-^35}".format("Задекорировано"),
                "\n{:-^35}".format("")
        )
        res = abt()
        print("{:-^35}".format(""))
        return res

    return _executor


@decor
def create_table ():
    tabl = []
    for i in range(1, n):
        for j in range(1, n):
            res = i*j
            print("%4d" % (res), end='')
            if i==1 or j==1:
                continue
            else:
                tabl.append(res)
        print()
    return tabl


@decor
def stats():
    decorFunc = str(len(A))
    decorFunc = "Задекорировано функций: " + decorFunc
    count_int = str(count.count(k))
    count_int = "Повторяющихся чисел k в таблице: " + count_int
    print(  "{:^35}".format(decorFunc),
            "\n{:^35}".format(count_int)
    )

if __name__ == "__main__":
    count = create_table()
    stats()
