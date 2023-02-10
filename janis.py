import random 
n = int(input("Ievadi sarakstu garumu n ="))
a = int(input("Ievadi mazāko intervala vertību a="))
b = int(input("Ievadi lielāko intervāla vērtību b="))
s1 = [random.randint(a,b) for i in range(n)]
s2 = [random.choise("string".ascii_uppercase) for i in range(n)]
print(s1)
print(s2)
s3 = []
print(s3)
s4 = [el for saraksts in zip(s1,s2) for el in saraksts]
print(s4)