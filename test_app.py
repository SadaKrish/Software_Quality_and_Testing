import unittest
from Software_Quality_and_Testing.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()

    def test_home(self):
        response=self.client.get("/")
        self.assertEqual(response.data.decode(), "CI/CD with GCP is working!")

    def test_add(self):
        response=self.client.get("/add")
        self.assertEqual(response.data.decode(), "4")

    def test_fail_example(self):
        #fail intentionally to test CI failure
        self.assertEqual(1+1,3)


if __name__=="__main__":
    unittest.main()