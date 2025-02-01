from lib.file import FileDB

db = FileDB()

dbPath = db.pathTo(destination="../db", origin=__file__)

inputData = [
    {"name": "Felipom1", "age": 23, "sex": "M"},
    {"name": "Maritsa1", "age": 34, "sex": "F"},
    {"name": "Julian1", "age": 25, "sex": "M"},
]

db.writeFile(
    data=inputData,
    fileName=dbPath + "/test",
    format="csv",
)

outputData = db.readFile(fileName=dbPath + "/test", format="csv")

print(dbPath)
print(outputData)