
"""try:

while True is True:
        
    print("\n Selcet an option: \n")
    
    print("1-Add task \n")
        
    print("2-See tasks \n")
    
    print("3-Delete 1 task \n")
        
    print("4-Delete all tasks \n")
        
    print("5-Finish program \n")

    option = int(input("- "))
        
    if option == 5:
            
        break
        
    elif option == 1:
            
        with open("tasks-list.json", "a", encoding= "UTF-8") as tasks_list:
                
            tasks_list.write(input("Introduce a task: "))
                
            tasks_list.write("\n")
        
    elif option == 2:
            
        tasks_list = pd.read_json("tasks-list.json")
            
        print(tasks_list.to_string())
        
    elif option == 3:
            
        with open("tasks-list.json", encoding= "UTF-8") as tasks_list:
                
            tasks_list.readline()
            
            
    elif option == 4:
            
        pass
        
except:
    pass"""
