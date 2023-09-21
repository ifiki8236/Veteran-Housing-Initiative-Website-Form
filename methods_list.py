#python methods that I can import into the main program

#converts the dict to a list
def dictToList(data):
    main_key = list(data.keys())
    some_list = list(data['landlords'].keys())
    print(some_list)
    
    for key in some_list:
        value = data[main_key[0]][key]
        print(f'{key} : {value}')

#creates an SQL database

#reads data into 
