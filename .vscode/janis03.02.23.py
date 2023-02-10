import random
a = 1
b = 10
n = 20
saraksts = [random,randint(a, b) for i in range(n)]
saraksts2 = list(set(saraksts))
print("1)", saraksts)
print("2)", saraksts2)
#3
for el in saraksts2:
    print("[", el, "] - ", saraksts, count(el))