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
    g.run(debug=True, port=1234)

if __name__ == "__main__":
    main()
 