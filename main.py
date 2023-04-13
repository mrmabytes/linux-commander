import json
import sys

print("*" * 24)
print("* Linux Commander v1.0 *")
print("*" * 24)
print("Example usage: Type 'add new user' or 'add' and hit Enter. To exit press 'q'.")
print()


def query_command():
    while True:
        with open('data.json') as f:
            data = json.load(f)
        try:
            query = input("What do you want to do? ").lower()
            words = query.split()
            for key in data:
                if all(word in key.lower() for word in words):
                    print("Command: " + data[key])
            if query == 'q':
                break
            print()
        except BaseException:
            pass


query_command()


def exit_program():
    while True:
        x = input("Exit program (y/n)? ").lower()
        if x == 'y':
            sys.exit()
        elif x == 'n':
            print()
            query_command()
        elif x != 'y' or 'n':
            print("Press 'y' or 'n'.")
            print()
        else:
            query_command()


exit_program()
