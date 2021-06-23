# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2021/06/23 09:36:38
@Author  :   Vincent
@Version :   1.0
@Contact :   wqli@seu.edu.cn
@License :   (C)Copyright 2021-2022
@Desc    :   None
"""

from bigraph import transform_bg
from task_assign import offline_task_assign

if __name__ == '__main__':
    task_cap_info = {'3->1': 2, '3->4': 3}
    worker_cap_info = {'1': 0, '3': 3}
    ttobg = [
        ('3->1', '3', 5),
        ('3->4', '3', 6)
    ]
    tobg = transform_bg(ttobg, task_cap_info, worker_cap_info)
    offline_strat = offline_task_assign(tobg)
    print(offline_strat)
