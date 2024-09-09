from player import Player

def get_player_cmd():
    return input("Action:\n> ")

def play():

    user_player = Player()
    user_player_active = True

    print("Escape from Greed Island -______-")
    while user_player_active:
        user_player_action = get_player_cmd()

        if user_player_action in ['q', 'Q', 'quit', 'Quit']:
            print("Thank you for playing :D")
            user_player_active = False
        elif user_player_action in ['n', 'N', 'north', 'North', '^']:
            print("You are going North!")
        elif user_player_action in ['e', 'E', 'east', 'East', '>']:
            print("You are going East!")
        elif user_player_action in ['s', 'S', 'south', 'South', 'v']:
            print("You are now travelling South!")
        elif user_player_action in ['w', 'W', 'west', 'West', '<']:
            print("You are now travelling West!")
        elif user_player_action in ['i', 'I', 'inventory', 'Inventory']:
            user_player.print_inventory()
        else:
            print("Try again Sailor...")

play()
