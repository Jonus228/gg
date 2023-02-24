from random import randint
Ist1 = [randint(0, 30) for i in range(12)]
Ist2 = [randint(0, 30) for i in range(12)]
all = Ist1 + Ist2
print("First:")
print(Ist1)
print("Two")
print(Ist2)
print("All lists:")
print(all)