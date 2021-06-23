# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   task_assign.py
@Time    :   2021/06/20 10:53:47
@Author  :   Vincent
@Version :   1.0
@Contact :   wqli@seu.edu.cn
@License :   (C)Copyright 2021-2022
@Desc    :   None
"""

from Kuhn_Munkres_Algorithm import run_kuhn_munkres

# --------------- offline part -------------------


def offline_task_assign(tobg):
    """
    @description  : use KM algorithm to generate task assignment stratege
    ---------
    @param  :
        tobg: bipartite graph <task, worker, utility>
    -------
    @Returns  :
    -------
    """
    return run_kuhn_munkres(tobg)
