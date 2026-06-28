from game import Game
import task as t
import view_flask as vw
""" 
@app.route('/')
def index():
    return 'hello world'
 """
def main():
    g = Game(t.Multiplizieren(), vw.FlaskViewer())

if __name__ == "__main__":
    main()
 