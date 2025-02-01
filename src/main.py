from lib.file import *

"""try:"""

while True is True:

    print("\n Selcet an option: \n")
    print("1-Add task \n")
    print("2-See tasks \n")
    print("3-Delete 1 task \n")
    print("4-Delete all tasks \n")
    print("5-Finish program \n")

    option = int(input("- "))
    dbPath = pathTo(destination="../db", origin=__file__)
    if option == 5:
        break

    elif option == 1:
        inputData = input("Enter a task:")
        inputData = {"name": inputData, "time": "1d"}

        tmp = addFile(
            data=inputData,
            fileName=dbPath + "/tasks-list",
            format="json",
            columns=["name", "time"],
        )

        print("Index", "name", "time")
        for index, row in tmp.iterrows():
            print(index, row["name"], row["time"])


    elif option == 2:

        file_read = readFile(fileName=dbPath + "/tasks-list", format="json")

        print(file_read)

    elif option == 3:

        with open("tasks-list.json", encoding="UTF-8") as tasks_list:

            tasks_list.readline()

    elif option == 4:

        pass

"""except:
    pass"""
