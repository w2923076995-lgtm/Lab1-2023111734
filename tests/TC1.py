import unittest
from word_graph import WordGraph, normalize_text_to_words


class TestFindBridgeWordsTC1(unittest.TestCase):
    def setUp(self):
       
        text = (
            "The scientist carefully analyzed the data, wrote a detailed report, "
            "and shared the report with the team, but the team requested more data, "
            "so the scientist analyzed it again."
        )
        words = normalize_text_to_words(text)
        self.wg = WordGraph(words)

    def test_tc1_scientist_to_analyzed(self):
        bridge_words, err = self.wg.find_bridge_words("scientist", "analyzed")

        self.assertEqual(bridge_words, ["carefully"])
        self.assertIsNone(err)


if __name__ == "__main__":
    unittest.main()