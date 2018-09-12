import os
import sys
import optparse


if sys.platform.startswith("win"):
    def get_files(names):
        for name in names:
            if os.path.isfile(name):
                yield name
            else:
                for file in glob.iglob(name):
                    if not os.path.isfile(file):
                        continue
                    yield file
else:
    def get_files(names):
        return (file for file in names if os.path.isfile(file))


def parse_options():
    pass


def main():
     child = os.path.join(os.path.dirname(__file__), "grepword-p-child.py")
     opts, word, args = parse_options()
     filelist = get_files(args, opts.recurse)
     files_per_process = len(filelist) // opts.count
     start, end = 0, files_per_process + (len(filelist) % opts.count)
     number = 1