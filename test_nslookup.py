import unittest

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("test_csv_file.csv")

class TestDataframeAssertions(unittest.TestCase):
    def test_ip_address_comparison(self):
        for index, row in df.iterrows():
            ip_address = row["ip_address"]
            get_ip_address = row["get_ip_address"]
            self.assertEqual(ip_address, get_ip_address, f"IP address mismatch at row {index}: Expected {ip_address}, Got {get_ip_address}")

if __name__ == '__main__':
    unittest.main()