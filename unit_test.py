# https://www.youtube.com/watch?v=zW_HyDTPjO0
import unittest
import cffi
import importlib


ffibuilder = cffi.FFI()

def load(filename):
    source = open(filename + '.c').read()
    includes = open(filename + '.h').read()

    ffibuilder.cdef(includes)
    ffibuilder.set_source(filename + '_', source, include_dirs=['/usr/include/x86_64-linux-gnu/python3.8', '/usr/include/python3.8'])
    ffibuilder.compile()

    module = importlib.import_module(filename + '_')
    return module.lib


class TestOne(unittest.TestCase):
    def test_one(self):
        module = load('example')
        rc = ffibuilder.new("int*", 0)
        self.assertEqual(module.get_one(rc), -1)
        self.assertEqual(1, rc[0])


if __name__ == '__main__':
    unittest.main()
