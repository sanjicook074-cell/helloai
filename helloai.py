#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""helloai.py —— 一个最小可运行的示例项目。

它存在的唯一目的，是当作 git-sync 的试验品：一个干净、无密钥、
无大文件的小文件夹，用来走通「本地文件夹 → 远端仓库」的完整流程。

用法：
    python helloai.py                  # Hello, AI!
    python helloai.py --name 世界       # Hello, 世界!
    python helloai.py --repeat 3       # 连说三遍
"""

import argparse


def greet(name="AI"):
    """返回一句问候。"""
    return f"Hello, {name}!"


def main():
    parser = argparse.ArgumentParser(description="打个招呼")
    parser.add_argument("--name", default="AI", help="要问候的名字，默认 AI")
    parser.add_argument("--repeat", type=int, default=1, help="重复几次，默认 1")
    args = parser.parse_args()

    for _ in range(max(1, args.repeat)):
        print(greet(args.name))


if __name__ == "__main__":
    main()
