"""
Week 8 Assignment - Design Patterns
-----------------------------------
Extend last week's assignment:
    1) Play Against the Computer:
        -You will be able to play against a pre-defined strategy computer
        -implemented as inherited class from Player; separate class from human player
        -design PlayerFactory class that instantiates correct Player class
        -computer's strategy will be to hold when the score is between 25 and 100
        -This will be inpmpleted in ComputerPlayer class that inherits Player base class
        -It should accept 2 command-line arguments (--player1 and --player2), which can be
         human or computer
         -Should use Factory class to instantiate either human or computer players,
          depending on the input
         -Game class should
    2) You will be able to play a timed version of Pig; with a one minute time limit, winner is
     first to reach 100 or has the highest score wins
        -implement using Proxy pattern Game class; uses Game methods but keeps track of time to
         determine winner
        -
"""
import random

class Player:
    def __init__(self, player):
        self.player_type = player
        self.player_score = None
        self.die_roll = random.seed(0)
        self.response = None

    def get_player_type(self):
        return self.player_type

    def get_player_score(self):
        return self.player_score

    def get_die_roll(self):
        self.die_roll = random.randint(1,6)
        return self.die_roll

    def get_player_response(self):
        return self.response

class HumanPlayer(Player):
    def __init__(self, player):
        self.player_type = player

class ComputerPlayer(Player):
    def __init__(self, player):
        self.player_type = player

    def computer_strategy(self):
        if self.player_score >= 25:
            self.response = 'h'
            return self.response
        else:
            self.response = 'r'
            return self.response

class PlayerFactory:
    def get_player(self,player):
        if player =='human':
            return HumanPlayer(player)
        elif player == 'computer':
            return ComputerPlayer(player)

class Game(Player):
    def __init__(self, name, score=0):
        Player.__init__(self, name, score=0)
        self.die_roll = random.randint(1,6)

    def get_die_roll(self):
        return self.die_roll

    def single_player_game(self):
        turn_total = 0
        display_message = "{} rolled a {}, have a roll total of {}, and a current score of {}."
        r_or_h_message = "Would you like to roll(r) or hold(h)? "
        winner = False
        while not winner:
            die_roll = self.get_die_roll()
            if die_roll != 1:
                turn_total += die_roll
                print(display_message.format(self.player_name, die_roll, turn_total, self.player_score))
                invalid_answer = True
                while invalid_answer:
                    response = input(r_or_h_message)
                    if response == 'r':
                        invalid_answer = False
                    elif response == 'h':
                        self.player_score += turn_total
                        turn_total = 0
                        invalid_answer = False
                    else:
                        print("Please enter valid response.")
            else:
                turn_total = 0
            if self.player_score >= 10:
                winner = True
                print("You win!")
                self.player_score = 0
                break

    def multiplayer_game(self):
        turn_total = 0
        display_message = "{} rolled a {}, has a roll total of {}, and a current score of {}."
        r_or_h_message = "Would you like to roll(r) or hold(h)? "
        winner = False
        while not winner:
            for  player in self.get_player_name():
                die_roll = self.get_die_roll()
                if die_roll != 1:
                    turn_total += die_roll
                    invalid_answer = True
                    while invalid_answer:
                        print(display_message.format(player.player_name, die_roll, turn_total, player.player_score))
                        response = input(r_or_h_message)
                        response = response.lower()
                        if response == 'r':
                            invalid_answer = False
                        elif response == 'h':
                            self.player_score += turn_total
                            turn_total = 0
                            invalid_answer = False
                            break
                        else:
                            print("Please enter valid response.")
                else:
                    turn_total = 0
            if self.player_score >= 10:
                    winner = True
                    print("You win!")
                    self.player_score = 0
                    break

"""
parser = argparse.ArgumentParser(description="Selection PlayerHello")
parser.add_argument("--player1")
parser.add_argument("--player2")
args = parser.parse_args()

print(args.echo)
"""
#print(Game('John').player_name) #John
#print(Game('John').get_die_roll()) #1-6
#print(Game("You").single_player_game()) #player "You"

#for player in Game(Player.players(3)).get_player_name():
#    print(player.player_name)
print(Game(Player.players(3)).multiplayer_game()) #Returns memory location of each generated player

#print(ComputerPlayer().player_name)
#print(ComputerPlayer())
#print(Game.single_player_game())
#print(type(Player.players(3)))
#for player in  Player.players(3):
#print(player.player_name)