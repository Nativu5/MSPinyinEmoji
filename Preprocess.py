# 此脚本用于将搜狗输入法的 UDP 词库 TXT 文件转换为 JSON 文件

import json
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Sogou UDP TXT to JSON")
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Input TXT file path",
    )
    args = parser.parse_args()

    input_file = args.input
    output_file = os.path.splitext(os.path.basename(input_file))[0] + ".json"

    # Sample TXT data
    # a,2=😦
    # a,3=😮
    # ab,2=🆎
    # abc,2=🔤
    # abcd,2=🔡

    data = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            pair, word = line.strip().split("=")
            py, rank = pair.split(",")
            data.append({"py": py, "str": word, "rank": int(rank)})

    json.dump(
        data,
        open(output_file, "w", encoding="utf-8"),
        ensure_ascii=False,
    )
