import unittest

from router import route_request


class RouterTests(unittest.TestCase):
    def test_urgent(self):
        self.assertEqual(route_request("urgent"), "duty")

    def test_standard(self):
        self.assertEqual(route_request("standard"), "service")

    def test_uppercase_priority(self):
        self.assertEqual(route_request("URGENT"), "duty")

    def test_whitespace_priority(self):
        self.assertEqual(route_request("   URGENT   "), "duty")
        self.assertEqual(route_request("\tstandard\t"), "service")
        self.assertEqual(route_request("\nurgent\n"), "duty")

    def test_critical(self):
        self.assertEqual(route_request("critical"), "duty")
