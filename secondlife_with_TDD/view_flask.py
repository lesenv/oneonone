from view_abstract import *
from flask_app.app_factory import app
from flask import request, render_template

'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
'''
@app.route('/')
def index():
    if request:
        answer = request.get_data("POST")
        print(answer)
        out(answer)
    return render_template("table.html")

@app.route("/output", methods=['GET', 'POST'])
def out(liststr):
    return liststr

class FlaskViewer(Viewer):
    def __init__(self):
        app.run(debug=True)

    @app.route("/output", methods=['GET', 'POST'])
    def output(self) -> None:
        # only method to print
        # all the others are returning the strings
        if request.method == 'POST':
           txt_list = request.form['username']
        if type(txt_list) == list:
            for txt in txt_list:
                print(f"{txt}")
        else:
            print()
        return render_template("table.html")

    def new_menu(self):
        self.clear_display()

    def clear_display(self):
        pass#subprocess.call('cls' if os.name == 'nt' else 'clear')
    
    def header(self, title: str = "") -> str:
        self.clear_display()
        txt = [title]
        txt.append("")
        txt.append(self.seperate_line())
        return txt
    
    def seperate_line(self) -> str:
        return "================"
    
    @app.route("/get_input", methods=['GET', 'POST'])
    def get_input(self, txt: str) -> int:

        if request.method == 'POST':
           txt_list = request.form['username']
        if type(txt_list) == list:
            for txt in txt_list:
                print(f"{txt}")
        else:
            print()
        return render_template("table.html")
        """ 
        try:
            return int(input(txt))
        except ValueError as e:
            return str(e)[-4:-1] """
    
    def get_new_name(self, txt: str = "Wie heißt Du? ") -> str:
        self.clear_display()
        return input(txt)

    def get_task(self, task: list = []) -> str:
        return("{} {} {} = ".format(*task))
    
    def closing(self, textlist: list[str] = []):
        self.clear_display()
        self.output(textlist)
