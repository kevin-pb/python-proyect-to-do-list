import pandas as pd
from pathlib import Path


def readFile(fileName="tasks-list", format="json", columns=["name", "value"]):
    try:
        file = fileName + "." + format
        if format == "json":
            dataFrame = pd.read_json(file, orient="records")
        if format == "csv":
            dataFrame = pd.read_csv(file)
        return dataFrame
    except Exception:
        return pd.DataFrame([], columns=columns)

def writeFile(data, fileName="tmp", format="json"):
    file = fileName + "." + format
    dataFrame = pd.DataFrame(data)
    if format == "json":
        dataFrame.to_json(file, orient="records")
    if format == "csv":
        dataFrame.to_csv(file)
    return dataFrame

def addFile(data, fileName="tmp", format="json", columns=["name", "value"]):
    df = readFile(fileName, format, columns)
    df.loc[len(df)] = data
    return writeFile(df, fileName, format)

def pathTo(destination, origin=__file__):
    pathORG = Path(origin).resolve().parent
    pathDES = pathORG.joinpath(destination).resolve()
    return str(pathDES)
