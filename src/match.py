from src.game import Game


class Match:

    def __init__(self, playerOne: str, playerTwo: str):
        self.sets = {playerOne: 0, playerTwo: 0}
        self.games = [Game(playerOne, playerTwo)]

    def __str__(self):
        return f"{'-'.join(str(x) for x in self.sets.values())}, {str(self.current_game())}"

    def pointWonBy(self, player: str) -> None:
        winning_point = self.current_game().pointWonBy(player)
        if(winning_point):
            self.sets[player] += 1
            self.games.append(Game(*self.sets.keys()))

    def current_game(self) -> Game: return self.games[self.games.count(
        self.games) - 1]

    def has_current_player_won(self, player: str) -> bool:
        current_sets = self.sets

        current_players_score = current_sets.get(player)

        for other_player in current_sets:
            other_players_score = current_sets.get(other_player)

        return current_players_score >= 6 and current_players_score > other_players_score + 1

    def score(self) -> str: return str(self)
