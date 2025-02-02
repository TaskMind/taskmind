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

        aboutUs = [
            {
              "title": "Nacido de la Necesidad",
              "desc": "TaskMind surgió de nuestra propia experiencia como estudiantes, al no encontrar una plataforma simple y efectiva para gestionar proyectos grupales académicos.",
              "icon": "fa-solid fa-graduation-cap"
            },
            {
              "title": "Potenciado por lA",
              "desc": "Integramos tecnologia de inteligencia artificial para ayudarte a organizar y priorizar tareas de manera más inteligente, adaptándose a tu forma de trabajar.",
              "icon": "fa-solid fa-brain"
            },
            {
              "title": "Open Source",
              "desc": "Creemos en la transparencia y la colaboración. Por eso, TaskMind es completamente open source y está abierto a contribuciones de la comunidad.",
              "icon": "fa-solid fa-code"
            },
        ]

        contribute = [
            {
              "title": "Desarrollo",
              "desc": "Ayúdanos a mejorar el código, agregar nuevas funcionalidades o corregir errores.",
              "icon": "fa-solid fa-code"
            },
            {
              "title": "Feedback",
              "desc": "Comparte tus ideas y sugerencias para hacer TaskMind aún mejor.",
              "icon": "fa-solid fa-comments"
            },
            {
              "title": "Difusión",
              "desc": "Ayúdanos a llegar a más estudiantes compartiendo el proyecto.",
              "icon": "fa-solid fa-heart"
            },
        ]

        return render_template("index.html", characteristics=characteristics, aboutUs=aboutUs, contribute=contribute)
