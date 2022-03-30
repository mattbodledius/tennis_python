from src.match import Match
import os
os.system('clear')


def main():
    match = Match('Joe', 'Jimmy')
    match.pointWonBy('Joe')
    match.pointWonBy('Joe')
    match.pointWonBy('Joe')
    match.pointWonBy('Joe')
    print(match.score())


main()
