import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        while True:
            hpMove = input("What's your move? " +
                           "Enter 'rock', 'paper', or 'scissors'\n")
            hpMove = hpMove.lower()
            if 'rock' in hpMove:
                return 'rock'
            elif 'paper' in hpMove:
                return 'paper'
            elif 'scissors' in hpMove:
                return 'scissors'
            else:
                print("Sorry, I don't understand.\n")

# For now, I assume player 2 will be the only player who can choose this player
# class. Later, I want to build out the code so that either player 1 or player
# 2 can be the ReflectPlayer, or both!


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.round_count = 0

    def move(self):
        self.round_count += 1
        if self.round_count == 1:
            return random.choice(moves)
        else:
            if self.their_move == 'rock':
                return 'rock'
            elif self.their_move == 'paper':
                return 'paper'
            elif self.their_move == 'scissors':
                return 'scissors'


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.round_count = 0
        self.first_move = ""
        self.first_move_index = 0
        self.second_move = ""
        self.second_move_index = 0
        self.third_move = ""
        self.third_move_index = 0

    def move(self):
        self.round_count += 1
        if self.round_count == 1:
            self.first_move = random.choice(moves)
            self.first_move_index = moves.index(self.first_move)
            return self.first_move
        elif self.round_count == 2:
            self.second_move_index = (self.first_move_index + 1) % 3
            self.second_move = moves[self.second_move_index]
            return self.second_move
        elif self.round_count == 3:
            self.third_move_index = (self.second_move_index + 1) % 3
            self.third_move = moves[self.third_move_index]
            return self.third_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def keep_score(self, p1_move, p2_move):
        if beats(p1_move, p2_move):
            self.p1.score += 1
        else:
            self.p2.score += 1
        print(f"Player 1 score: {self.p1.score}    " +
              f"Player 2 score: {self.p2.score}\n")

    def winner(self):
        if self.p1.score > self.p2.score:
            print("Player 1 wins! Final Scores:\n" +
                  f"Player 1: {self.p1.score}     Player 2: {self.p2.score}\n")
        elif self.p1.score < self.p2.score:
            print("Player 2 wins! Final Scores:\n" +
                  f"Player 1: {self.p1.score}     Player 2: {self.p2.score}\n")
        elif self.p1.score == self.p2.score:
            print("We have a tie! Final Scores:\n" +
                  f"Player 1: {self.p1.score}     Player 2: {self.p2.score}\n")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("Tie! Doesn't count!\n")
        else:
            self.keep_score(move1, move2)

    def play_game(self):
        print("\nGame start!\n")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        self.winner()
        print("Game over!\n")


if __name__ == '__main__':
    computer_players = ([Player(), RandomPlayer(), ReflectPlayer(),
                         CyclePlayer()])
    opponent = random.choice(computer_players)
    game = Game(HumanPlayer(), opponent)
    game.play_game()
