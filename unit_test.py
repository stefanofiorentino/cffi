# https://www.youtube.com/watch?v=zW_HyDTPjO0
import unittest
import cffi
import importlib


def load(filename):
    source = open(filename + '.c').read()
    includes = open(filename + '.h').read()

    ffibuilder = cffi.FFI()
    ffibuilder.cdef(includes)
    ffibuilder.set_source(filename + '_', source)
    ffibuilder.compile()

    module = importlib.import_module(filename + '_')
    return module.lib


class TestOne(unittest.TestCase):
    def test_one(self):
        module = load('example')
        self.assertEqual(module.get_one(), 1)


if __name__ == '__main__':
    unittest.main()
