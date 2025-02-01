import pandas as pd
from pathlib import Path

class FileDB:
    def readFile(self, fileName="tasks-list", format="json", columns=["name", "value"]):
        try:
            file = fileName + "." + format
            if format == "json":
                dataFrame = pd.read_json(file, orient="records")
            if format == "csv":
                dataFrame = pd.read_csv(file)
            return dataFrame
        except Exception:
            return pd.DataFrame([], columns=columns)

    def writeFile(self, data, fileName="tmp", format="json"):
        file = fileName + "." + format
        dataFrame = pd.DataFrame(data)
        if format == "json":
            dataFrame.to_json(file, orient="records")
        if format == "csv":
            dataFrame.to_csv(file)
        return dataFrame

    def addFile(self, data, fileName="tmp", format="json", columns=["name", "value"]):
        df = self.readFile(fileName, format, columns)
        df.loc[len(df)] = data
        return self.writeFile(df, fileName, format)

    def pathTo(self, destination, origin=__file__):
        pathORG = Path(origin).resolve().parent
        pathDES = pathORG.joinpath(destination).resolve()
        return str(pathDES)
