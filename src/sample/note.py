class Note:
    def __init__(self, name, note):
        if name == '' or name is None:
            raise ValueError('Name values can not be '' or none')
        if type(name) != str:
            raise TypeError('Bad type name')
        if type(note) != float:
            raise TypeError('Bad type note')
        if note < 2 or note > 6:
            raise ValueError('Note bad values')
        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
