import os
import json
import mykaze
import unittest

class PyMySQLTestCase(unittest.TestCase):
    # You can specify your test environment creating a file named
    #  "databases.json" or editing the `databases` variable below.
    fname = "pymysql/tests/databases.json"
    if os.path.exists(fname):
        with open(fname) as f:
            databases = json.load(f)
    else:
        databases = [
            {"host":"localhost","user":"root",
             "passwd":"","db":"test_pymysql", "use_unicode": True},
            {"host":"localhost","user":"root","passwd":"","db":"test_pymysql2"}]

    def setUp(self):
        self.connections = []

        for params in self.databases:
            self.connections.append(mykaze.connect(**params))

    def tearDown(self):
        for connection in self.connections:
            connection.close()
