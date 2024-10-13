u"""指定した条件の配列（リスト）文字列を生成するスクリプト。

Usage:
    python generate-big-array.py <n> <min_value> <max_value> <unique>

Args:
    n: 生成する配列の要素数。
    min_value: 生成する配列の要素の最小値。
    max_value: 生成する配列の要素の最大値。
    unique: 生成する配列の要素が重複しないようにするかどうか。(0: 重複あり、1: 重複なし)
"""

import sys
import random

def generate_big_array(n, min_value, max_value, unique=False):
    u"""指定した条件の配列（リスト）文字列を生成する。

    Args:
        n: 生成する配列の要素数。
        min_value: 生成する配列の要素の最小値。
        max_value: 生成する配列の要素の最大値。
        unique: 生成する配列の要素が重複しないようにするかどうか。

    Returns:
        生成した配列の文字列。
    """
    array = []
    while len(array) < n:
        value = random.randint(min_value, max_value)
        if unique and value in array:
            continue
        array.append(value)
    return str(array)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: python generate-big-array.py <n> <min_value> <max_value> <unique>')
        sys.exit(1)

    n = int(sys.argv[1])
    min_value = int(sys.argv[2])
    max_value = int(sys.argv[3])
    unique = bool(int(sys.argv[4]))

    print(generate_big_array(n, min_value, max_value, unique))
