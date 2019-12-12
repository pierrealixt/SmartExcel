import os
import unittest
from smartexcel.smart_excel import SmartExcel
from smartexcel.tests.data.definitions.dummy import DUMMY_DEFINITION
from smartexcel.tests.data.data_models.dummy import DummyData


class TestDump(unittest.TestCase):
    def setUp(self):
        self.definition = DUMMY_DEFINITION
        self.data = DummyData()
        self.filepath = 'hello.xlsx'
        # /tmp/dummy_test.xlsx'

        if os.path.exists(self.filepath):
            os.remove(self.filepath)


    def runTest(self):
        self.assertFalse(os.path.exists(self.filepath))
        excel = SmartExcel(
            definition=self.definition,
            data=self.data,
            output=self.filepath
        )
        self.assertTrue(excel.WRITEMODE)

        excel.dump()

        self.assertTrue(os.path.exists(self.filepath))
        self.assertEqual(len(excel.sheets), 2)


    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)



if __name__ == "__main__":
    unittest.main()