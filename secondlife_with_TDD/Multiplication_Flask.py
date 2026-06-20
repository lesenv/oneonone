from game import Game
import view_flask as vw
import task as t

def main():
    Game(t.Multiplizieren(), vw.FlaskApp())

if __name__ == "__main__":
    main()