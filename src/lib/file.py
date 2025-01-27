import pandas as pd
from pathlib import Path


def readFile(fileName="tasks-list", format="json"):
    file = fileName + "." + format
    if format == "json":
        list = pd.read_json(file, orient="records")
    if format == "csv":
        list = pd.read_csv(file)
    return list


def writeFile(data, fileName="tmp", format="json"):
    file = fileName + "." + format
    dataFrame = pd.DataFrame(data)
    if format == "json":
        dataFrame.to_json(file, orient="records")
    if format == "csv":
        dataFrame.to_csv(file)


def pathTo(destination, origin=__file__):
    pathORG = Path(origin).resolve().parent
    pathDES = pathORG.joinpath(destination).resolve()
    return str(pathDES)
