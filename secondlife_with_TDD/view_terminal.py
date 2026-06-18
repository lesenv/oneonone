import subprocess, os # just for Terminal
from view_abstract import *
from person import Person

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

class Terminal(Viewer):
    def out_names(self, p_list: list[str], lives: dict = {}, active: str = "") -> None:
        self.output(self.header())
        maxtabs = (max( length for length in [len(p) for p in p_list] ))
        for p in p_list:
            prefix = ">> " if p == active else "   "
            grid = f"{(maxtabs - len(p))*' '}"
            line = prefix + f"{p}: {grid}{"O"*lives[p]}"
            if not lives[p]:
                line = '\033[91m' + line + '\033[0m' # line in red
            self.output([line])
        self.output()

    def output(self, txt_list: list[str] = None) -> None:
        # only method to print
        # all the others are returning the strings
        if type(txt_list) == list:
            for txt in txt_list:
                print(f"{txt}")
        else:
            print()

    def new_menu(self):
        self.clear_display()

    def clear_display(self):
        subprocess.call('cls' if os.name == 'nt' else 'clear')
    
    def header(self) -> str:
        self.clear_display()
        txt = ["1x1-Übungen -..-''-..-''# help: type 'hhh'"]
        txt.append("")
        txt.append(self.seperate_line())
        return txt
    
    def seperate_line(self) -> str:
        return "================"
    
    def get_input(self, txt: str) -> int:
        try:
            return int(input(txt))
        except ValueError as e:
            return str(e)[-4:-1]
    
    def get_new_name(self, txt: str = "Wie heißt Du? ") -> str:
        self.clear_display()
        return input(txt)

    def get_task(self, task: list = []) -> str:
        return("{} {} {} = ".format(*task))
    
    def closing(self, textlist: list[str] = []):
        self.clear_display()
        if textlist:
            self.output(textlist)
        self.output(["", "Schön war's", "Bis zum nächsten Mal!"])