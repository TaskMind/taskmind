from flask import render_template

class PagesContoller:
    def __init__(self):
        pass

    def index(self):
        characteristics = [
          {
            "title": "Grupos de trabajo",
            "desc": "Crea grupos para diferentes proyectos o equipos",
            "content": "Organiza a tu equipo en grupos específicos para mejor coordinación y seguimiento de tareas.",
            "icon": "fa-solid fa-user-group"
          },
          {
            "title": "Gestión de tareas",
            "desc": "Asigna y supervisa tareas fácilmente",
            "content": "Crea, asigna y da seguimiento a tareas con fechas limite y prioridades.",
            "icon": "fa-solid fa-list"
          },
          {
            "title": "Control de acceso",
            "desc": "Gestiona permisos y roles",
            "content": "Define roles de administrador y miembro para mantener el control de tu equipo.",
            "icon": "fa-solid fa-shield"
          },
          {
            "title": "Grupos de trabajo",
            "desc": "Crea grupos para diferentes proyectos o",
            "content": "Recibe notificaciones sobre actualizaciones y cambios en las tareas de tu grupo.",
            "icon": "fa-solid fa-bell"
          }
        ]

        return render_template("index.html", characteristics=characteristics)
