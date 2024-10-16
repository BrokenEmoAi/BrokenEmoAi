import unittest
from core.luna_engine import LunaEngine

class TestLuna(unittest.TestCase):
    def setUp(self):
        self.luna = LunaEngine("FAKE_API_KEY")

    def test_generate_tweet(self):
        tweet = self.luna.generate_tweet()
        self.assertIsInstance(tweet, str)
        self.assertGreater(len(tweet), 10)

if __name__ == '__main__':
    unittest.main()
