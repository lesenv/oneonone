from game import Game
import view_terminal as vw
import task as t

def main():
    Game(t.Multiplizieren(), vw.Terminal())

if __name__ == "__main__":
    main()