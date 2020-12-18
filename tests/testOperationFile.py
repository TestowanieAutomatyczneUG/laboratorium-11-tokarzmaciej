from unittest.mock import mock_open, patch, Mock
from unittest import TestCase, main, mock

from src.sample.file import File


class testFile(TestCase):
    def setUp(self):
        self.temp = File()

    def test_open_file(self):
        openFile = mock_open(read_data="test_open_file")
        with patch('builtins.open', openFile):
            self.assertEqual(self.temp.read_file("file.txt"), "test_open_file")

    def test_edit_file(self):
        editFile = mock_open(read_data="test_open_file")

        with patch('builtins.open', editFile):
            self.temp.edit_file("file.txt", "test_write_file")
        editFile.assert_called_once_with("file.txt", "w")

    @mock.patch('src.sample.file.os')
    def test_delete_file_exception(self, mock_os):
        mock_os.path = Mock()
        mock_os.path.exists.return_value = False
        self.assertRaisesRegex(Exception,"This file not exist", self.temp.delete_file, "file.txt")

    @mock.patch('src.sample.file.os')
    def test_delete_file(self, mock_os):
        mock_os.path = Mock()
        mock_os.path.exists.return_value = True
        self.temp.delete_file("file.txt")
        mock_os.remove.assert_called_with("file.txt")


if __name__ == '__main__':
    main()
