import os
import sys
import unittest

# 当前测试文件所在目录：wtests
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 项目根目录，也就是 word_graph.py 所在目录
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# 将项目根目录加入 Python 模块搜索路径
sys.path.insert(0, PROJECT_ROOT)

from word_graph import WordGraph


class TC2(unittest.TestCase):
    """
    TC2：测试图非空，但随机起点没有出边的情况。

    覆盖基本路径2：
    502 → 515 → 516(F) → 519 → 521 → 522 → 523
    → 525 → 526 → 529(T) → 530 → 531
    → 556 → 559 → 560 → 561 → 565
    """

    def test_random_walk_single_node_no_out_edge(self):
        # 构造只有一个节点的图
        # 由于只有一个单词 hello，所以不会形成任何有向边
        wg = WordGraph(["hello"])

        output_file = os.path.join(CURRENT_DIR, "random_walk_tc2.txt")

        # 如果之前测试生成过文件，先删除
        if os.path.exists(output_file):
            os.remove(output_file)

        # 执行随机游走
        walk_text, stop_reason = wg.random_walk(
            output_file=output_file,
            interactive=True
        )

        # 期望的函数返回结果
        self.assertEqual(walk_text, "hello")
        self.assertEqual(stop_reason, "节点 'hello' 没有出边，随机游走结束。")

        # 期望文件被正常创建
        self.assertTrue(os.path.exists(output_file))

        # 期望文件内容为 hello 加换行
        with open(output_file, "r", encoding="utf-8") as f:
            file_content = f.read()

        self.assertEqual(file_content, "hello\n")


if __name__ == "__main__":
    unittest.main()