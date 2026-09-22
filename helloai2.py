#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""helloai2.py —— 第二代示例，用来演示「新增文件 → 同步到远端」这一步。

跟 helloai.py 相比多了两件事：
  1. 一次可以问候多个名字；
  2. 可以用 --shout 把招呼喊出来。

用法：
    python helloai2.py                          # Hello, AI!
    python helloai2.py 世界 相机 森山大道          # 一次问候多个
    python helloai2.py 世界 --shout              # HELLO, 世界!!!
    python helloai2.py --formal                  # Hello, AI.
"""

import argparse


def greet(name="AI", shout=False, formal=False):
    """返回一句问候。"""
    ends = "." if formal else "!"
    text = f"Hello, {name}{ends}"
    return text.upper().replace("!", "!!!") if shout else text


def main():
    parser = argparse.ArgumentParser(description="打个招呼（第二代）")
    parser.add_argument("names", nargs="*", default=None,
                        help="要问候的名字，可以给多个；不给则默认 AI")
    parser.add_argument("--shout", action="store_true", help="大声喊出来")
    parser.add_argument("--formal", action="store_true", help="用句号收尾，显得稳重")
    args = parser.parse_args()

    for name in (args.names or ["AI"]):
        print(greet(name, shout=args.shout, formal=args.formal))


if __name__ == "__main__":
    main()
