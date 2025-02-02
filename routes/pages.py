from flask import Blueprint, render_template
from controllers.pages import PagesContoller

bp = Blueprint("pages", __name__)
pagesController = PagesContoller()

@bp.get("/")
def index():
    return pagesController.index()
