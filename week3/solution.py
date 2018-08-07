import os


class FileReader:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def read(self):
        try:
            if not os.path.exists(self.path_to_file):
                raise IOError('')
        except IOError as err:
            return err.args[0]
        with open(self.path_to_file) as f:
            content = f.read()
            return content