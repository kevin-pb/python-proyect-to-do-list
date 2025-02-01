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
        
        dbPath = self.db.pathTo(destination="../db", origin=__file__)
        
        tmp = self.db.readFile(fileName=dbPath + "/tasks-list",
                               format="json",
                               columns=["name", "time"])
        
        self.showDataList(tmp)
        

    def dell(self):
        dbPath = self.db.pathTo(destination="../db", origin=__file__)
        
        df = self.db.readFile(fileName=dbPath + "/tasks-list",
                               format="json",
                               columns=["name", "time"])
        self.show()
        row_to_eliminate = int(input("Introduce the index of the row to eliminate: "))
        
        new_df= df.drop([row_to_eliminate])
        self.db.writeFile(new_df, fileName=dbPath + "/tasks-list", format="json")
            
    def dellAll(self):
        dbPath = self.db.pathTo(destination="../db", origin=__file__)
        self.db.writeFile(None, fileName=dbPath + "/tasks-list", format="json")