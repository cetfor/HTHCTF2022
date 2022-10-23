import string
import time

from random import randint

def encode(text, n):
    trans = lambda x,n:str.maketrans(x,x[n:]+x[:n])
    lower_case = string.ascii_lowercase
    return text.lower().translate(trans(lower_case, n))

def main():
    flag = "hth{caesar_salad_shift}"

    while True:
        rand_num = randint(1, 25)
        cipher_text = encode(flag, rand_num)
        
        print("Welcome to a really easy 'crypto' problem.")
        print(f"Today's challenge is: {cipher_text}")
        print("Please enter your secure pass phrase >> ", end="")
        user_input = input("").lower()

        if len(user_input) < len(cipher_text):
            print("Access denied!")
        
        print("\nChecking input...")
        time.sleep(1)
        
        if len(user_input) == len(flag):
            print("Access granted! Please submit your solution as the flag!\n")
            return

        print("Access denied!\n\n")

if __name__ == "__main__":
    main()
