import MenuInterface.menuInterface as m

def menu_console():
    m.printMenuTitle("Main menu \n        Notebook program!")
    print("1 - Print your notes \n2 - Print your notes by id \n3 - Print your note by date \n4 - Edit your note"
          " \n5 - Create new note \n6 - Delete your note \n7 - Exit")
    m.printMenuLine()
    print("\n Insert number from menu ")