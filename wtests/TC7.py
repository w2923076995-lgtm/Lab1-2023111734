import os
import sys
import unittest
from unittest.mock import patch

# 当前测试文件所在目录：wtests
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 上级目录，也就是 word_graph.py 所在目录
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# 将项目根目录加入 Python 模块搜索路径
sys.path.insert(0, PROJECT_ROOT)

from word_graph import WordGraph


class TC7(unittest.TestCase):
    """
    TC7：测试随机游走结束后，写入文件失败的情况。

    构造单词序列：
    ["hello"]

    图中只有一个节点 hello，没有任何出边。

    随机游走过程：
    1. 随机起点为 hello
    2. hello 没有出边，随机游走结束
    3. 尝试写入文件
    4. 模拟 open() 抛出异常
    5. stop_reason 中追加“写入文件失败”信息

    覆盖基本路径7：
    502 → 515 → 516(F) → 519 → 521 → 522 → 523
    → 525 → 526 → 529(T)
    → 530 → 531
    → 556 → 559 → 560
    → 562 → 563
    → 565
    """

    def test_random_walk_write_file_failed(self):
        # 构造只有一个节点的图
        # hello 没有出边
        wg = WordGraph(["hello"])

        output_file = os.path.join(CURRENT_DIR, "random_walk_tc7.txt")

        # 如果之前测试生成过文件，先删除
        if os.path.exists(output_file):
            os.remove(output_file)

        # 模拟 open() 写文件时失败
        with patch("builtins.open", side_effect=OSError("模拟写入失败")):
            walk_text, stop_reason = wg.random_walk(
                output_file=output_file,
                interactive=True
            )

        # 验证随机游走文本
        self.assertEqual(walk_text, "hello")

        # 验证停止原因中包含“节点无出边”
        self.assertIn("节点 'hello' 没有出边，随机游走结束。", stop_reason)

        # 验证停止原因中追加了“写入文件失败”
        self.assertIn("写入文件失败：模拟写入失败", stop_reason)

        # 由于 open() 被模拟为失败，所以文件不会被创建
        self.assertFalse(os.path.exists(output_file))


if __name__ == "__main__":
    unittest.main()