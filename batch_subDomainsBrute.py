#!/usr/bin/python3
# coding: utf-8
import subprocess
import os
import argparse
import re


def main(data1):
    target = data1
    cmd = r"python3 subDomainsBrute.py {}".format(target)
    print(cmd)
    rsp = os.system(cmd)
    print(rsp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="subDomains辅助工具,批量扫描")
    parser.add_argument("-t", "--target", type=str, metavar="target", help="txt目标路径 eg:\"/XX/XX/xx.txt\"")
    args = parser.parse_args()
    target_target = args.target
    file = open(target_target, encoding='utf-8', errors='ignore')
    for text in file.readlines():
        data1 = text.strip('\n')
        main(data1)
