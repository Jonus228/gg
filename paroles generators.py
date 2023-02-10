import random
import string
garums = int(input("Ievadi paroles garumu: ""))
mazie = string.ascii_uppercase
lielie = string.ascii_uppercase
cipari = string.digits
simboli = string.punctuation
elementi = lielie + mazie  + cipari + simboli
gadijuma_elimenti = random.sample