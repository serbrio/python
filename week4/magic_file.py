import os
import tempfile


class File:
    """Class File with some magic"""

    def __init__(self, pth):
        if not os.path.isabs(pth):
            raise ValueError('{} is not abs path'.format(pth))
        self.path = os.path.abspath(pth)
        self._rawpath = pth
        self.current = 0

    def write(self, content):
        with open(self.path, 'a') as f:
            return f.write(content)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __iter__(self):
        return self

    def _count_file_lines(self):
        n = 0
        with open(self.path, 'r') as f:
            for _ in f.readlines():
                n += 1
        return n

    def __next__(self):
        if self.current >= self._count_file_lines():
            raise StopIteration
        with open(self.path, 'r') as f:
            counter = 0
            for line in f.readlines():
                if counter == self.current:
                    self.current += 1
                    return line
                counter += 1

    def __str__(self):
        return self._rawpath

    def __add__(self, obj):
        if not isinstance(obj, __class__):
            raise TypeError('"{}" is not instance of {}'.format(obj, __class__))
        sumpath = tempfile.NamedTemporaryFile(delete=False).name
        sumfile = File(sumpath)
        sumfile.write(self.read() + obj.read())
        return sumfile

