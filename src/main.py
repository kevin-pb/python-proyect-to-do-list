from lib.file import FileDB
from lib.menu import MenuUI
from taskui import UITask

taskUi = UITask(db=FileDB())

options = [
    {"title": "Add task", "handler": taskUi.add},
    {"title": "Show task", "handler": taskUi.show},
    {"title": "Delete task", "handler": taskUi.dell},
    {"title": "Delete all", "handler": taskUi.dellAll},
]
menu = MenuUI(options)
menu.render()
