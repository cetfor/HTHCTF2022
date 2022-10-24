import time

def main():
    flag = "HTH{time_can_tell_a_lot}"
    
    print("\nLet me see those coins, I'll check them for you.")
    print("Coins >> ", end="")

    user_input = ""
    try:
        user_input = input("")
    except EOFError:
        return
    
    if len(user_input) < len(flag):
        print("This isn't the right number of coins. You made more wishes than this.\n")
        return
    elif len(user_input) > len(flag):
        print("This isn't the right number of coins. You made less wishes than this.\n")
        return
    
    print("\nAhh, this is the right number of wishes, let me check them one by one...")

    for i, char in enumerate(flag):
        if char == user_input[i]:
            time.sleep(0.25)
    
    if user_input == flag:
        print(f"That's it! These are your wishes! Use '{user_input}' as your flag.")
        return
    else:
        print(f"Some of these aren't your wishes. Try again.")

if __name__ == "__main__":
    main()
