# snakes-and-ladders
import random
import time

# Board size
BOARD_SIZE = 100

# Snakes and Ladders mapping
# key = start, value = end
moves = {
    4: 14,   # ladder
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,

    17: 7,   # snake
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice):
    new_position = position + dice
    
    if new_position > BOARD_SIZE:
        return position  # cannot move beyond 100
    
    print(f"Moved to {new_position}")
    
    if new_position in moves:
        if new_position < moves[new_position]:
            print("🎉 Ladder! Climb up!")
        else:
            print("🐍 Snake! Slide down!")
        return moves[new_position]
    
    return new_position

def play_game():
    print("🎲 Welcome to Snakes and Ladders!")
    
    players = int(input("Enter number of players: "))
    positions = [0] * players
    
    winner = None
    
    while not winner:
        for i in range(players):
            input(f"\nPlayer {i+1}, press Enter to roll dice...")
            
            dice = roll_dice()
            print(f"🎲 You rolled: {dice}")
            
            positions[i] = move_player(positions[i], dice)
            print(f"Player {i+1} is now at {positions[i]}")
            
            if positions[i] == BOARD_SIZE:
                winner = i + 1
                break
            
            time.sleep(1)
    
    print(f"\n🏆 Player {winner} wins!")

if __name__ == "__main__":
    play_game()
