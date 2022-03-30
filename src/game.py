
class Game:
    score_mapping = {0: 0, 1: 15, 2: 30, 3: 40}

    def __init__(self, playerOne: str, playerTwo: str):
        self.score = {playerOne: 0, playerTwo: 0}

    def __str__(self):
        if(all(score == list(self.score.values())[0] for score in self.score.values())):
            return 'Deuce'
        return "-".join(str(x) for x in self.score.values())

    def winningCondition(self, player: str) -> bool:
        current_scores = self.score
        current_players_score = current_scores.get(player)
        for other_player in current_scores:
            other_players_score = current_scores.get(other_player)

        return current_players_score >= 6 and current_players_score > other_players_score + 1

    # Returns winning player, or None if no winner yet
    def point_scored(self, player: int) -> str:
        self.score[player] += 1

        if(self.winningCondition(player)):
            return player
