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






"""try:"""


# def showTaskList(df):
#     print("=======================")
#     print("Index", "name", "time")
#     print("=======================")
#     for index, row in df.iterrows():
#         print(index, row["name"], row["time"])
#         print("......................")


# def showMenuHeader():
#     print("\n Selcet an option: \n")
#     print("1-Add task \n")
#     print("2-See tasks \n")
#     print("3-Delete 1 task \n")
#     print("4-Delete all tasks \n")
#     print("5-Finish program \n")


# while True is True:
#     showMenuHeader()
#     option = int(input("- "))
#     dbPath = pathTo(destination="../db", origin=__file__)
#     if option == 5:
#         break

#     elif option == 1:
#         inputData = input("Enter a task:")
#         inputData = {"name": inputData, "time": "1d"}

#         tmp = addFile(
#             data=inputData,
#             fileName=dbPath + "/tasks-list",
#             format="json",
#             columns=["name", "time"],
#         )

#         showTaskList(tmp)

#     elif option == 2:
#         file_read = readFile(fileName=dbPath + "/tasks-list", format="json")
#         print(file_read)

#     elif option == 3:
#         with open("tasks-list.json", encoding="UTF-8") as tasks_list:
#             tasks_list.readline()

#     elif option == 4:
#         pass

"""except:
    pass"""
