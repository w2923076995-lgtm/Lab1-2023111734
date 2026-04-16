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


class TC3(unittest.TestCase):
    """
    TC3：测试非交互模式下，走到无出边节点后结束。

    覆盖基本路径3：
    502 → 515 → 516(F) → 519 → 521 → 522 → 523
    → 525 → 526 → 529(F)
    → 534 → 535 → 538 → 539
    → 542(F) → 546 → 547
    → 550(F)
    → 525 → 526 → 529(T)
    → 530 → 531
    → 556 → 559 → 560 → 561 → 565
    """

    def test_random_walk_non_interactive_end_with_no_out_edge(self):
        # 构造图：
        # 单词序列 ["a", "b"] 会形成一条有向边 a -> b
        # 节点 b 没有出边
        wg = WordGraph(["a", "b"])

        output_file = os.path.join(CURRENT_DIR, "random_walk_tc3.txt")

        # 如果之前测试生成过文件，先删除
        if os.path.exists(output_file):
            os.remove(output_file)

        # 固定 random.choice 的结果：
        # 第一次 random.choice(nodes) 返回 "a"
        # 第二次 random.choice(out_neighbors) 返回 "b"
        with patch("word_graph.random.choice", side_effect=["a", "b"]):
            walk_text, stop_reason = wg.random_walk(
                output_file=output_file,
                interactive=False
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