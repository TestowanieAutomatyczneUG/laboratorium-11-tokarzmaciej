import os


class File:
    def read_file(self, path):
        file = open(path, "r")
        return file.read()

    def edit_file(self, path, data):
        file = open(path, "w")
        file.write(data)

    def delete_file(self, path):
        if os.path.exists(path):
            os.remove(path)
        else:
            raise Exception("This file not exist")
