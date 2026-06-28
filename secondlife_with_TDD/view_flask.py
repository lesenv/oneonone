from view_abstract import *
from flask import Flask, request, render_template, redirect

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
        self.run(debug=True, port=1234)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

    def register_endpoints(self):
        self.app.add_url_rule(rule="/", endpoint="index", view_func=self.index, methods=['GET', 'POST'])
        self.app.add_url_rule(rule="/read_input_number", endpoint="read_input_number", view_func=self.read_input_number, methods=['GET', 'POST'])
        #self.app.add_url_rule(rule="/get_input", endpoint="get_input", view_func=self.get_input, methods=['GET', 'POST'])
        
    def _get_post_data(self):
            request.get_data()
            answer = int(request.form.get("c_input"))
            self.old_tries.append(answer)

    def index(self):
        if request.method == "POST":
            self._get_post_data()
            return redirect('/read_input_number')
        return render_template("table.html")
    
    def read_input_number(self, txt_list = []):
        if request.method == 'POST':
            self._get_post_data()
            txt_list = request.form['c_input']
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
        self.read_input_number(textlist)
