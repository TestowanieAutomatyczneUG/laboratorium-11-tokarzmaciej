from src.sample.notesStorage import NotesStorage


class NotesService:
    def __init__(self):
        self.notesStorage = NotesStorage()

    def add(self, note):
        return self.notesStorage.add(note)

    def averageOf(self, name):
        if not self.notesStorage.getAllNotesOf(name):
            raise Exception("This person has not notes")
        else:
            marks = map(lambda person: person.note, self.notesStorage.getAllNotesOf(name))
            return sum(marks) / len(self.notesStorage.getAllNotesOf(name))

    def clear(self):
        return self.notesStorage.clear()
