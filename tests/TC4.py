import os
import sys
import unittest

# 把项目根目录 lab1 加入模块搜索路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from word_graph import WordGraph, normalize_text_to_words


class TestFindBridgeWordsTC4(unittest.TestCase):
    def setUp(self):
        text = (
            "The scientist carefully analyzed the data, wrote a detailed report, "
            "and shared the report with the team, but the team requested more data, "
            "so the scientist analyzed it again."
        )
        words = normalize_text_to_words(text)
        self.wg = WordGraph(words)

    def test_tc4_same_input_words(self):
        bridge_words, err = self.wg.find_bridge_words("the", "the")

        self.assertEqual(bridge_words, [])
        self.assertEqual(err, "No bridge words from the to the!")


if __name__ == "__main__":
    unittest.main()