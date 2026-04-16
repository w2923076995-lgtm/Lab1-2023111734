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


class TC5(unittest.TestCase):
    """
    TC5：测试交互模式下，用户按回车继续，之后遇到无出边节点结束。

    构造单词序列：
    ["a", "b"]

    形成的有向边为：
    a -> b

    随机游走过程：
    1. 随机起点固定为 a
    2. 从 a 走到 b
    3. interactive=True，用户按回车继续
    4. 下一轮 b 没有出边，随机游走结束

    覆盖基本路径5：
    502 → 515 → 516(F) → 519 → 521 → 522 → 523
    → 525 → 526 → 529(F)
    → 534 → 535 → 538 → 539
    → 542(F) → 546 → 547
    → 550(T) → 551 → 552(F)
    → 525 → 526 → 529(T)
    → 530 → 531
    → 556 → 559 → 560 → 561 → 565
    """

    def test_random_walk_interactive_continue_then_no_out_edge(self):
        # 构造图：
        # a -> b
        # b 没有出边
        wg = WordGraph(["a", "b"])

        output_file = os.path.join(CURRENT_DIR, "random_walk_tc5.txt")

        # 如果之前测试生成过文件，先删除
        if os.path.exists(output_file):
            os.remove(output_file)

        # 固定 random.choice 的结果：
        # 第一次：从 nodes 中选择起点 a
        # 第二次：从 a 的出边中选择 b
        #
        # 同时模拟用户输入：
        # input() 返回 ""，表示用户直接按回车继续
        with patch("word_graph.random.choice", side_effect=["a", "b"]):
            with patch("builtins.input", return_value=""):
                walk_text, stop_reason = wg.random_walk(
                    output_file=output_file,
                    interactive=True
                )

        # 验证返回的游走文本
        self.assertEqual(walk_text, "a b")

        # 验证停止原因
        self.assertEqual(stop_reason, "节点 'b' 没有出边，随机游走结束。")

        # 验证文件已生成
        self.assertTrue(os.path.exists(output_file))

        # 验证文件内容
        with open(output_file, "r", encoding="utf-8") as f:
            file_content = f.read()

        self.assertEqual(file_content, "a b\n")


if __name__ == "__main__":
    unittest.main()