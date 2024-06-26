import argparse
from json import loads, dumps, JSONDecodeError
from random import choice
import string
from colorama import Fore, Back, Style


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(characters) for i in range(length))
    return password


if __name__ == "__main__":
    len = 40
    print(Back.WHITE + "█"*len + Back.RESET + Fore.RESET)
    print(Back.BLUE + Fore.BLUE+ "█"*len + Back.RESET + Fore.RESET)
    print(Back.RED + Fore.RED+"█"*len + Back.RESET + Fore.RESET)

    parser = argparse.ArgumentParser(description='Generate keys.')
    parser.add_argument('-n', help='generate key(by name)')
    parser.add_argument('-d', help='del key(by name)')

    args = parser.parse_args()

    if not args.n and not args.d:
        parser.print_help()
        exit(-1)
    elif args.n and not args.d:
        key_name = args.n
        print(Fore.MAGENTA + f"Generate new key with name {key_name}")

        t = 0  # 0 - read, 1 - regen
        try:
            with open("keys.json", "r", encoding="UTF-8") as f:
                loads(f.read())
        except FileNotFoundError:
            print(Fore.CYAN + "file not found. We need to create it")
            t = 1
        except JSONDecodeError:
            print(Fore.CYAN + "File is empty. Regen it.")
            t = 1
        except Exception as e:
            print(Fore.RED + "Unknown error:", e)
            i = input(Fore.CYAN + "ReCreate file(y - regenerate)?: ")
            if i.lower() != "y":
                print(Fore.RED + "Unknown error.")
                exit(-100)
        if t == 1:
            with open("keys.json", "w", encoding="UTF-8") as f:
                f.write(dumps({}))

        with open("keys.json", "r", encoding="UTF-8") as f:
            glob = loads(f.read())

        if key_name in glob.keys():
            print(Fore.YELLOW + "We found key with same name.")
            i = input(Fore.CYAN + "Recreate key - r, do nothing - e. What we should do: ")
            if i.lower() != "r":
                print(Fore.MAGENTA + "Ok, end.")
                exit(-1)

        passw = generate_password(50)

        glob[key_name] = passw
        with open("keys.json", "w", encoding="UTF-8") as f:
            f.write(dumps(glob))

        print(Fore.GREEN + f"User {key_name} has registered. His password: {Fore.MAGENTA}\n{passw}")

    elif not args.n and args.d:
        key_name = args.d
        print(f"{Fore.MAGENTA}Try to del {key_name} password")
        try:
            with open("keys.json", "r", encoding="UTF-8") as f:
                loads(f.read())
        except FileNotFoundError:
            print(Fore.RED + "file not found. We need to create it")
            exit(-100)
        except JSONDecodeError:
            print(Fore.RED + "File is empty. Regen it.")
            exit(-100)
        except Exception as e:
            print(Fore.RED + "Unknown error.")
            exit(-100)

        with open("keys.json", "r", encoding="UTF-8") as f:
            glob = loads(f.read())

        if key_name not in glob.keys():
            print("Key not found(")

        del glob[key_name]

        with open("keys.json", "w", encoding="UTF-8") as f:
            f.write(dumps(glob))
        print(Fore.MAGENTA+"Removed.")
