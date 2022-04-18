import unittest
from reaper_python_connector import main


class MyTestCase(unittest.TestCase):
    def test_parsing(self):
        main.reaper_connector(t1='0,0', t2='100,0', elev_list=['30', '31', '32', '30', '31', '32', '30', '31', '132'], az_list=['-130', '-131', '-132', '-130', '-131', '-132', '-130', '-131', '32'])
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
