import os
import sys
import unittest

# 获取当前测试文件所在目录：wtests
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 获取上级目录，也就是 word_graph.py 所在目录
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# 将上级目录加入 Python 搜索路径，方便导入 word_graph.py
sys.path.insert(0, PROJECT_ROOT)

from word_graph import WordGraph


class TC1(unittest.TestCase):
    """
    TC1：测试空图情况下的随机游走函数
    覆盖基本路径1：
    502 → 515 → 516(T) → 517
    """

    def test_random_walk_empty_graph(self):
        # 构造空图
        wg = WordGraph([])

        output_file = os.path.join(CURRENT_DIR, "random_walk_tc1.txt")

        # 如果之前运行测试生成过文件，先删除
        if os.path.exists(output_file):
            os.remove(output_file)

        # 执行随机游走
        walk_text, stop_reason = wg.random_walk(
            output_file=output_file,
            interactive=True
        )

        # 验证返回的游走文本为空
        self.assertEqual(walk_text, "")

        # 验证停止原因为“图为空”
        self.assertEqual(stop_reason, "图为空，无法进行随机游走。")

        # 空图时函数直接 return，不会执行写入文件操作
        self.assertFalse(os.path.exists(output_file))


if __name__ == "__main__":
    unittest.main()