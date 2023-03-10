import os
import unittest
import pandas as pd
from local_files_management.import_local_file import import_local_file_to_df


class TestImportLocalFile(unittest.TestCase):
    """
    A class to test the `import_local_file_to_df` function from the `local_files_management` module.
    """

    def setUp(self):
        """
        Sets up the test by creating the test file 'my_local_file.csv' and filling it with test data.
        """
        data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
        df = pd.DataFrame(data)
        df.to_csv('my_local_file.csv', index=False)

    def test_import_local_file_to_df(self):
        """
        Tests the `import_local_file_to_df` function by importing the test file and checking if the resulting
        DataFrame has the expected values.
        """
        expected_data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = import_local_file_to_df('my_local_file.csv')
        pd.testing.assert_frame_equal(actual_df, expected_df)

    def tearDown(self):
        """
        Cleans up the test by deleting the test file 'my_local_file.csv'.
        """
        os.remove('my_local_file.csv')
