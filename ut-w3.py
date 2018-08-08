import os
import unittest
from week3.solution import FileReader


class TestFileReaderMethods(unittest.TestCase):
    def test_not_found(self):
        self.assertEqual(FileReader('file/not/found').read(), '')
        self.assertFalse(FileReader('file/not/found').read())

    def test_found(self):
        path_to_cur_file = os.path.realpath(__file__)
        with open(path_to_cur_file) as f:
            cur_file_content = f.read()
        self.assertTrue(FileReader('ut-w3.py'))
        self.assertEqual(FileReader('ut-w3.py').read(), cur_file_content)
        with self.assertRaises(TypeError):
            FileReader().read()


if __name__ == '__main__':
    unittest.main()