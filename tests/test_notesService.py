from src.sample.notesStorage import NotesStorage
from src.sample.notesService import NotesService
from src.sample.note import Note
from unittest.mock import *
from unittest import TestCase, main


class testNotesService(TestCase):

    def test_add_note(self):
        objectStorage = NotesStorage()
        objectStorage.add = MagicMock()
        objectStorage.add.return_value = Note("Maciej", 4.5).note

        test_object = NotesService()
        test_object.notesStorage = objectStorage

        result = test_object.add(Note("Maciej", 4.5))
        self.assertEqual(result, Note("Maciej", 4.5).note)

    def test_add_note_type_error(self):
        objectStorage = NotesStorage()
        objectStorage.add = MagicMock()
        objectStorage.add.side_effect = TypeError

        test_object = NotesService()
        test_object.notesStorage = objectStorage

        result = test_object.add
        self.assertRaises(TypeError, result, False)

    def test_average(self):
        objectStorage = NotesStorage()
        objectStorage.getAllNotesOf = MagicMock()
        objectStorage.getAllNotesOf.return_value = [Note("Maciej", 4.0), Note("Maciej", 5.0), Note("Maciej", 3.0)]

        test_object = NotesService()
        test_object.notesStorage = objectStorage

        result = test_object.averageOf("Maciej")
        self.assertEqual(result, 4)

    def test_average_exception(self):
        objectStorage = NotesStorage()
        objectStorage.getAllNotesOf = MagicMock()
        objectStorage.getAllNotesOf.return_value = []

        test_object = NotesService()
        test_object.notesStorage = objectStorage

        result = test_object.averageOf
        self.assertRaisesRegex(Exception, "This person has not notes", result, "Maciej")

    def test_average_value_error(self):
        objectStorage = NotesStorage()
        objectStorage.getAllNotesOf = MagicMock()
        objectStorage.getAllNotesOf.side_effect = ValueError

        test_object = NotesService()
        test_object.notesStorage = objectStorage

        result = test_object.averageOf
        self.assertRaises(ValueError, result, 13)

    def test_clear(self):
        objectStorage = NotesStorage()
        objectStorage.clear = MagicMock()
        objectStorage.clear.return_value = "data cleaned"

        test_object = NotesService()
        test_object.notesStorage = objectStorage

        result = test_object.clear()
        self.assertEqual(result, "data cleaned")


if __name__ == '__main__':
    main()
