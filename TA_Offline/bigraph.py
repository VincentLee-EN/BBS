# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   bigraph.py
@Time    :   2021/06/23 09:29:34
@Author  :   Vincent
@Version :   1.0
@Contact :   wqli@seu.edu.cn
@License :   (C)Copyright 2021-2022
@Desc    :   None
"""

# --------------- offline part -------------------


def construct_ttobg(task_info, worker_info):
    """
    @description  : construct bipartite graph
    ---------
    @param  :
        - task_info: dict {#cluster: bike_num}
        - worker_info: dict {#cluster: worker_num}
    -------
    @Returns  :
        - ttobg: task-type oriented bipartite graph <task_type, worker_type, utility>
        - task_cap_info: dict {task_type: capacity}
        - worker_cap_info: dict {}
    -------
    """

    pass


def transform_bg(ttobg, task_cap_info, worker_info):
    """
    @description  : transform to task oriented bipartite graph <task, worker, utility>
    ---------
    @param  :
        ttobg: bipartite graph <task_type, worker_type, utility>
    -------
    @Returns  :
        tobg: bipartite graph <task, worker, utility>
    -------
    """
    tobg = []
    for assign in ttobg:
        task_type = assign[0]
        worker_type = assign[1]
        task_cap = task_cap_info[task_type]
        utility = assign[2] / task_cap
        worker_num = worker_info[worker_type]
        for i in range(worker_num):
            for j in range(task_cap):
                tobg.append([task_type+'_'+str(j), i, utility])
    return tobg
