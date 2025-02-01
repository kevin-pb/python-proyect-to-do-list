# To do list

This project is an application that allows you to manage a task list using pandas DataFrames

## Architecture

In the src folder you will find the "[main](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/main.py)"file, the "[taskui](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/taskui.py)" file and the "file.demo" file. The "[taskui](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/taskui.py)" file contains a class that contains a series of methods that allow you to perform operations on a pandas DataFrame; the operations that it allows you to perform are: add a task, show all tasks, delete a task and delete all tasks. The "[main](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/main.py)" file is the file that will be executed in the application; it contains the union of all the files with which the application can be executed. La carpeta "[lib](https://github.com/kevin-pb/python-proyect-to-do-list/tree/main/src/lib)" contiene dos módulos: "[file](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/lib/file.py)" y "[menu](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/lib/menu.py)"; "[file](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/lib/file.py)" contiene una clase con varios métodos para el trabajo de DataFrames de pandas, estos métodos se usan en el archivo "[taskui](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/taskui.py)" y el archivo "[menu](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/src/lib/menu.py)" contiene todo lo referente a la interfaz gráfica. La carpeta "[db](https://github.com/kevin-pb/python-proyect-to-do-list/tree/main/db)" contiene el archivo "[tasks-list](https://github.com/kevin-pb/python-proyect-to-do-list/blob/main/db/tasks-list.json)" en el que se almacena la información

# Run & Configure

python main.py

# References 

- [Path Lib Docs](https://docs.python.org/3/library/pathlib.html)

- [File & Path Demo](./src/file.demo.py)

- [Panda Demo Lib](./src/lib/file.py)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)

- [Inos](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/funciones-lambda-de-python/?gad_source=1&gclid=CjwKCAiAqfe8BhBwEiwAsne6gVu7-MI4-s2c0JjcOse-mGsRFU2Vo0wSJbuhn74i3eCDRztFQJ-v1hoC-moQAvD_BwE&gclsrc=aw.ds&itc=3VVVRR75-XIDLQ6-&utm_campaign=SGE-ES-DOM-DOMX-PMX-----&utm_content=DOM&utm_medium=cpc&utm_source=google)

- [Codigo python](https://www.codigopiton.com/como-recorrer-un-diccionario-en-python/)

- [Data Camp](https://www.datacamp.com/tutorial/python-dictionary-comprehension?utm_source=google&utm_medium=paid_search&utm_campaignid=21057859163&utm_adgroupid=157296744657&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=726134766170&utm_targetid=aud-1459190388940:dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=1005424&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-es-lang-en_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-jan25&gad_source=1&gclid=CjwKCAiAqfe8BhBwEiwAsne6gUOkz6dxmgEZAemFAuC1_JMmVjjpgwTyC2k_pfRXaS4qQOGUsJcrmhoCErsQAvD_BwE)