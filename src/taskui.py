class UITask:

    def __init__(self, db):
        self.db = db
        pass

    def showDataList(self, df):
        print("=======================")
        print("Index", "name", "time")
        print("=======================")
        for index, row in df.iterrows():
            print(index, row["name"], row["time"])
            print("......................")

    def add(self):
        inputName = input("Enter the task name: ")
        inputData = {"name": inputName, "time": "1d"}

        dbPath = self.db.pathTo(destination="../db", origin=__file__)

        tmp = self.db.addFile(
            data=inputData,
            fileName=dbPath + "/tasks-list",
            format="json",
            columns=["name", "time"],
        )

        self.showDataList(tmp)

    def show(self):
        print("This is show task")
        pass

    def dell(self):
        pass

    def dellAll(self):
        pass

    def extra(self):
        print("this is an extra option \n")