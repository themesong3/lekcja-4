from lib2to3.pgen2.pgen import generate_grammar
import random
def generate_number():
    return random.randrange(1, 10)

def read_number():
    return int(input("Give me anumber "))