
from operator import contains


class Game:
    score_mapping = {0: 0, 1: 15, 2: 30, 3: 40}

    def __init__(self, playerOne: str, playerTwo: str):
        self.score = {playerOne: 0, playerTwo: 0}

    def __str__(self):
        if(all(contains(self.score_mapping.keys(), x) for x in self.score.values())):
            return "-".join(str(self.score_mapping[x]) for x in self.score.values())

        if(all(score == list(self.score.values())[0] for score in self.score.values())):
            return 'Deuce'

        return f'Advantage Player {self.player_with_highest_score()}'

    def num_of_player_with_highest_score(self) -> int:
        highest = max(self.score, key=self.score.get)

        return list(self.score.keys()).index(highest) + 1

    def winning_condition(self, player: str) -> bool:
        current_scores = self.score

        current_players_score = current_scores.get(player)

        for other_player in current_scores:
            other_players_score = current_scores.get(other_player)

        return current_players_score >= 6 and current_players_score > other_players_score + 1

    # Returns winning player, or None if no winner yet
    def pointWonBy(self, player: int) -> str:
        self.score[player] += 1

        if(self.winning_condition(player)):
            return player
