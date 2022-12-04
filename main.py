#Jonathan Sladish


#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }
# This gives the directions for moving to different rooms
directions = ['North', 'South', 'East', 'West', 'Exit']
# This is starting point for the game
current_room = 'Great Hall'

# This while statement starts the loop for the game
while True:
# this will show the current room that the player is located
    print('You are in  {}'.format(current_room))
# this command gives the user two options enter a direction or exit game
    command = input('Enter direction or exit:')
# this will print what the user chose from there command
    print(command)
#this if statement to exit game and the game finishes
    if command == 'exit':
        current_room = 'exit'
#this will print thanks for playing when user exit's game
        print("Thank's for playing, I hope you had fun!")
#this break stops the loop
        break
#if else statement to keep game running if user doesn't choose exit
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
#this else statement will print invalid move if user make incorrect move
    else:
        print('Invalid move')