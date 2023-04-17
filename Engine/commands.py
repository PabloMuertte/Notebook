import SubPrograms.loadNotesFromFile as lF
import SubPrograms.saveNotesToFile as wF
import NoteFormat.NoteFormat

def add_note():
    title = input("Input subject of note:\n")
    body = input("Input description of note:\n")
    note = NoteFormat.NoteFormat.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if NoteFormat.NoteFormat.Note.get_id(note) == NoteFormat.NoteFormat.Note.get_id(i):
            NoteFormat.NoteFormat.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Note is added to the notebook!")

def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("Your Notebook:")
            for i in array_notes:
                print(NoteFormat.NoteFormat.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", NoteFormat.NoteFormat.Note.get_id(i))
            id = input("\nInput ID of Note: ")
            flag = True
            for i in array_notes:
                if id == NoteFormat.NoteFormat.Note.get_id(i):
                    print(NoteFormat.NoteFormat.Note.map_note(i))
                    flag = False
            if flag:
                print("There is no such ID")

        elif txt == "date":
            date = input("Please input date in format: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(NoteFormat.NoteFormat.Note.get_date(i))
                if date == date_note[:10]:
                    print(NoteFormat.NoteFormat.Note.map_note(i))
                    flag = False
            if flag:
                print("There is no such date!")
        else:
            print("Notebook is empty!")

def del_notes():
    id = input("Input ID of note which you want to delete: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == NoteFormat.NoteFormat.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Note with id: ", id, " successful deleted!")
    else:
        print("There is no such id")

def change_note():
    id = input("Input ID of editing note: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == NoteFormat.NoteFormat.Note.get_id(i):
            i.title = input("Edit  subject:\n")
            i.body = input("Edit  description:\n")
            NoteFormat.NoteFormat.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("Note with id: ", id, " edited successful!")
    else:
        print("there is no such id")
