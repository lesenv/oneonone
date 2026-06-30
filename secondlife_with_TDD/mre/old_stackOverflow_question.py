

---- below the old stuff. I don't know, if this is relevant -----

I want to let my son have fun with the multiplication table. I made a little game with a multiplayer-mode. For the future I have started to decouple the logic and the output, so I can easily (easier) add new math-tasks like addition, division, differentiation, ...I have a script game, that's controlling two others: one task is calculating the tasks and can give the right answer, the other view_terminal is doing the output. game can take new tasks from task, propose 3 times the same task and give a point to the current player if they get it right, otherwise substract one.

excerpt from game with the core elements:

import view_terminal as vw
import task as t

class Game():
    def __init__(self, tasker, viewer):
        self.tasker = tasker
        self.viewer = viewer

        self.people = collectionsdeque()
        self.add_Person()

        self.start_game()
    
    def get_answer_3_times(self):
        new_mult_task = self.tasker.make_task()
        for _ in range(3):
            ans = self.viewer.get_input(self.viewer.get_task(new_mult_task))
            if ans == self.tasker.get_result():
                return True
        return False

    def start_game(self):
        while any(f.lives for f in self.people):
            self.viewer.output(self.viewer.header(self.title))
            self.people.rotate(1)
            active_person = self.people[0]
            if not active_person.lives:
                continue
            self.viewer.output(self.out_names(active_person))
            active_person.change_life(self.get_answer_3_times())

outputting per terminal is working like a charm, everything is fine. but now I want to advance the fun for my kid. first thought is another way of output. I was thinking of Flask or tkinter. First try is Flask and the first dummy is working, but when the server started the flow is never getting back to game.

from usercase_Flask:

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
 

and from view_flask:

from flask import Flask, request, render_template, redirect


class FlaskViewer(Viewer):
    @property
    def app(self) -> Flask:
        return self._app
    
    @app.setter
    def app(self, app: Flask):
        self._app = app
    
    def __init__(self):
        self.app = Flask(__name__)
        self.old_tries = []
        self.register_endpoints()

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

    def register_endpoints(self):
        self.app.add_url_rule(rule="/", endpoint="index", view_func=self.index, methods=['GET', 'POST'])
        self.app.add_url_rule(rule="/guess", endpoint="guess", view_func=self.guess, methods=['GET', 'POST'])
        
    def _get_post_data(self):
            request.get_data()
            answer = self.input2int(request.form.get("c_input"))
            if answer:
                self.old_tries.append(answer)

    def input2int(self, input):
        try:
            return int(input)
        except ValueError:
            return 0

    def index(self):
        if request.method == "POST":
            self._get_post_data()
            return redirect('/guess')
        return render_template("table.html", len = len(self.old_tries), old_tries = self.old_tries)
    
    def guess(self):
        if len(self.old_tries) > 3:
            self.old_tries = []
            return redirect("/index")
        self.read_input_number()
        return render_template("table.html", len = len(self.old_tries), old_tries = self.old_tries)

    def read_input_number(self):
        if request.method == 'POST':
            self._get_post_data()
    
    def get_input(self, txt: str) -> int:
        if request.method == 'POST':
           txt_list = request.form['username']
        if type(txt_list) == list:
            for txt in txt_list:
                print(f"{txt}")
        else:
            print()
        return render_template("table.html")

    def get_task(self, task: list = []) -> str:
        return("{} {} {} = ".format(*task))

Do I have to do all the game logic in Flask again? How can I give control back to the game script?