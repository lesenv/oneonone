from flask import Flask, request, render_template

class FlaskViewer():
    @property
    def app(self) -> Flask:
        return self._app
    
    @app.setter
    def app(self, app: Flask):
        self._app = app
    
    def __init__(self, logic = None):
        self.app = Flask(__name__)
        self.register_endpoints()
        self.logic = logic

    def register_endpoints(self):
        self.app.add_url_rule(rule="/", endpoint="index", view_func=self.index, methods=['GET', 'POST'])
        
    def index(self):
        return render_template("table.html")

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)
    
    def get_input(self) -> int:

        if request.method == 'POST':
           txt_list = request.form['username']
        if type(txt_list) == list:
            for txt in txt_list:
                print(f"{txt}")
        else:
            print()
        return render_template("table.html")
