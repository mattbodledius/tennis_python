
from operator import contains


class Game:
    score_mapping = {0: 0, 1: 15, 2: 30, 3: 40}

    def __init__(self, playerOne: str, playerTwo: str):
        self.score = {playerOne: 0, playerTwo: 0}

    def __str__(self):
        def scoresDisplayable(scores: dict): return all(
            contains(self.score_mapping.keys(), x) for x in scores.values())

        def scoresEqual(scores: dict): return all(
            score == list(scores.values())[0] for score in scores.values())

        if(scoresDisplayable(self.score)):
            return "-".join(str(self.score_mapping[x]) for x in self.score.values())

        if(scoresEqual(self.score)):
            return 'Deuce'

        return f'Advantage Player {self.num_of_player_with_highest_score()}'

    def num_of_player_with_highest_score(self) -> int:
        highest = max(self.score, key=self.score.get)

        return list(self.score.keys()).index(highest) + 1

    def has_current_player_won(self, player: str) -> bool:
        current_scores = self.score

        current_players_score = current_scores.get(player)

        for other_player in current_scores:
            other_players_score = current_scores.get(other_player)

        return current_players_score >= 4 and current_players_score > other_players_score + 1

    # Returns winning player, or None if no winner yet
    def pointWonBy(self, player: int) -> str:
        self.score[player] += 1

        if(self.has_current_player_won(player)):
            return player
