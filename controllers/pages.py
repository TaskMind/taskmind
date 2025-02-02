from flask import render_template

class PagesContoller:
    def __init__(self):
        pass

    def index(self):
        return render_template("index.html")
