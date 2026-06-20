from game import Game
import task as t
from flask_app.app_factory import app
import view_flask as vw
""" 
@app.route('/')
def index():
    return 'hello world'
 """
def main():
    Game(t.Multiplizieren(), vw.FlaskViewer())

if __name__ == "__main__":
    main()
 