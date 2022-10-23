import string
import time

from random import randint

def encode(text, n):
    trans = lambda x,n:str.maketrans(x,x[n:]+x[:n])
    lower_case = string.ascii_lowercase
    return text.lower().translate(trans(lower_case, n))

def main():
    flag = "hth{skip_the_tongue_go_with_the_caesar_salad}"

    while True:
        rand_num = randint(1, 25)
        cipher_text = encode(flag, rand_num)
        
        print("Welcome to a really easy 'crypto' problem.")
        print(f"Here's your challenge: {cipher_text}")
        print("Passphrase >> ", end="")

        user_input = ""
        try:
            user_input = input("").lower()
        except EOFError:
            pass

        print("\nChecking input...")
        time.sleep(1)

        if user_input == flag:
            print("Access granted! Please submit your solution as the flag!\n")
            return
        
        print("Access denied!\n\n")

if __name__ == "__main__":
    main()
