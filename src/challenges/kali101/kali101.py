import json

from python_shell import Shell # pip install python-shell
from python_shell.util.streaming import decode_stream

COMMANDS = {
    "level01": Shell.ncat('--help'),
    "level02": Shell.man('ssh'),
}

def clear_console():
    command = Shell.clear()
    print(decode_stream(command.output), end="")

def get_level_data(file="levels.json"):
    data = None
    with open(file, 'r') as f:
        data = f.read()
    data = json.loads(data)
    return data

def load_level(level, levels):
    current_level = 0
    for i, l in enumerate(levels):
        if level == l: current_level = i+1
    clear_console()
    print(f"Loading level: {current_level}\n")
    print(levels[level]['intro'])
    while True:
        print(levels[level]['task'])
        command = input("$ ")
        if command == levels[level]["command"]:
            command = COMMANDS[level]
            print(decode_stream(command.output), end="")
            while True:
                print(f"\n{level} question: {levels[level]['prompt']}")
                answer = input(f"{level} answer >> ")
                if answer == levels[level]['solution']:
                    print(f"That's correct! Here's your flag for {level}: {levels[level]['flag']}")
                    return 1
                else:
                    print("Try again!")

def main():
    # Greet the user
    print(">> Welcome to Hackers Teaching Hackers CTF 2022 Kali 101! <<")
    
    # Prompt the user until they select a valid option
    while True:
        print("Please enter a command from the following list:")
        print(" - start (start the CTF challenge set)")
        print(" - level (select a level to jump to)")
        print(" - exit  (disconnect from the challenge set)")
        command = input(">> ")
        if command.lower() in ["start", "level", "exit"]:
            break
        else:
            print(f"\n'{command}' is not a valid command. Try again.\n")

    # Read level data from 'levels.json'
    levels = get_level_data()

    # START
    if command.lower() == "start":
        for level in levels:
            load_level(level, levels)
            input("Press enter to load the next level. Ctrl+C to quit.")

    # LEVEL
    elif command.lower() == "level":
        while True:
            print("Which level would you like to jump to?")
            selected_level = input(">> ")
            try:
                selected_level = int(selected_level)
            except ValueError:
                print("That's not a valid entry. Try again.\n")
            if selected_level < 1 or selected_level > len(levels):
                print(f"That's not a valid level. Please select from 1 to {len(levels)}.\n")
            else:
                break
        for i, level in enumerate(levels):
            if selected_level == i+1:
                load_level(level, levels)

    # EXIT
    elif command.lower() == "exit":
        print("See ya!")
        return 0


if __name__=="__main__":
    main()