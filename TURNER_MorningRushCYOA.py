# Morning Rush CYOA


def print_header():
    """Print title and a divider. (No parameters)"""
    print("=== Morning Rush Adventure ===")
    print("-" * 36)

def ask_choice(prompt, valid_options):
    """
    Ask until the player types a valid option.
    Parameters:
        prompt (str): the text shown to the player
        valid_options (list[str]): the valid options the player can choose from are ["a", "b"]

    Returns:
        str: the validated answer
    """

    while True:  #loops until player types a valid option
        ans = input(prompt).strip().lower()
        if ans in valid_options:
            return ans
        print('Please choose "a" or "b".')

def end_game(won, message):
    """Show a final message. Parameters: won (True/False), message (str)."""
    print("\n" + "-" * 36)
    print("You Win!" if won else "Game Over.")
    print(message)
    print("=" * 36)

print_header()

# Game Variables
player_name = input("Enter your name? ")
minutes_until_class = 45
on_bus = False
has_pass = False
missed_stop = False


print(f"Hi {player_name}, it is {minutes_until_class} minutes until your 9:00 AM class.")
print("Answer each prompt with 'a' or 'b'.")

# Simple Countdown (loop)
print ("\nGetting ready:")
for i in range(3, 0, -1):
    print(i, "...")
print("GO!\n")

first = ask_choice("Do you (a) leave now or (b) make coffee first? [a/b] ", ["a", "b"])

if first == "b":
    end_game(False, "You made coffee in an open cup, spilling it all over your shirt.")
    raise SystemExit()

second = ask_choice("Quick! Pick a transportation option: (a) take the bus or (b) ride your bike? [a/b] ", ["a", "b"])

if second == "b":
    end_game(False, "Your tire went flat and now you're stuck.")
    raise SystemExit()

else:
    on_bus = True
    bus_stops = ["Library", "Gym", "CASE building"]

third = ask_choice("Do you (a) remember to bring your student ID to catch the bus or (b) accidentally leave your student ID at home? [a/b] ", ["a", "b"])

if third == "b":
    end_game(False, "Fare inspection! You didn't have your student ID and were asked to exit the bus.")
    raise SystemExit()

else:
    has_pass = True

print("\nThe bus is passing by the:")
for stop in bus_stops:
    print("-", stop)

fourth = ask_choice("Your stop is coming up. Do you (a) get off at the CASE building or (b) put on headphones and zone out? [a/b] ", ["a", "b"])

if fourth == "b":
    end_game(False, "You missed your stop and had to sprint to class. You're late.")
    raise SystemExit()

else:
    if on_bus and has_pass and not missed_stop:
        end_game(True, "You hop off the bus right in front of the CASE building and make it to class on time! You're feeling proud of yourself.")
        raise SystemExit()