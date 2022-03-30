from src.match import Match
import os
os.system('clear')

# Just for testing the input for the interface


def main():
    match = Match('Joe', 'Jimmy')
    match.pointWonBy('Joe')
    match.pointWonBy('Joe')
    match.pointWonBy('Joe')
    match.pointWonBy('Joe')
    print(match.score())


main()
