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


class TC6(unittest.TestCase):
    """
    TC6：测试交互模式下，用户输入 q 手动停止随机游走。

    构造单词序列：
    ["a", "b"]

    形成的有向边为：
    a -> b

    随机游走过程：
    1. 随机起点固定为 a
    2. 从 a 走到 b
    3. interactive=True，程序询问用户是否继续
    4. 用户输入 q
    5. 随机游走结束

    覆盖基本路径6：
    502 → 515 → 516(F) → 519 → 521 → 522 → 523
    → 525 → 526 → 529(F)
    → 534 → 535 → 538 → 539
    → 542(F) → 546 → 547
    → 550(T) → 551 → 552(T)
    → 553 → 554
    → 556 → 559 → 560 → 561 → 565
    """

    def test_random_walk_interactive_user_quit(self):
        # 构造图：
        # a -> b
        wg = WordGraph(["a", "b"])

        output_file = os.path.join(CURRENT_DIR, "random_walk_tc6.txt")

        # 如果之前测试生成过文件，先删除
        if os.path.exists(output_file):
            os.remove(output_file)

        # 固定 random.choice 的结果：
        # 第一次：从 nodes 中选择起点 a
        # 第二次：从 a 的出边中选择 b
        #
        # 模拟用户输入：
        # input() 返回 "q"，表示用户手动停止
        with patch("word_graph.random.choice", side_effect=["a", "b"]):
            with patch("builtins.input", return_value="q"):
                walk_text, stop_reason = wg.random_walk(
                    output_file=output_file,
                    interactive=True
                )

        # 验证返回的游走文本
        self.assertEqual(walk_text, "a b")

        # 验证停止原因
        self.assertEqual(stop_reason, "用户手动停止随机游走。")

        # 验证文件已生成
        self.assertTrue(os.path.exists(output_file))

        # 验证文件内容
        with open(output_file, "r", encoding="utf-8") as f:
            file_content = f.read()

        self.assertEqual(file_content, "a b\n")


if __name__ == "__main__":
    unittest.main()