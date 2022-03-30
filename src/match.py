from src.game import Game


class Match:

    def __init__(self, playerOne: str, playerTwo: str):
        self.sets = {playerOne: 0, playerTwo: 0}
        self.games = [Game(playerOne, playerTwo)]

    def __str__(self):
        return "-".join(str(x) for x in self.sets.values()) + ", " + str(self.current_game())

    def pointBy(self, player):
        winning_point = self.current_game().point_scored(player)
        if(winning_point):
            self.sets[player] += 1
            self.games.append(Game(*self.sets.keys()))

    def current_game(self): return self.games[self.games.count(
        self.games) - 1]
