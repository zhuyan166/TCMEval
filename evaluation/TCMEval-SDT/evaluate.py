# coding=utf-8
import json
import sys
import os
import numpy as np
import time
import pandas as pd

# 自定义函数
# Task 1 计分函数
def clinical_info_extraction_eval(LLMs_answers, cli_info_list):
    cli_info_list_length = len(cli_info_list)
    answers_count = 0
    LLMs_answers_list =  LLMs_answers.split(';')
    # 去重
    LLMs_answers_list = list(set(LLMs_answers_list))
    for item in cli_info_list:
        #if item in LLMs_answers_list:
        #    answers_count = answers_count + 1
        for item_y in LLMs_answers_list:
            if item == item_y:
                answers_count = answers_count + 1
    if answers_count == 0:
        return 0
    else:
        # 加入惩罚得分
        #if answers_count <= cli_info_list_length:
        #    extract_score = answers_count/cli_info_list_length
        #else:
        #    extract_score = 0
        return answers_count/cli_info_list_length
        #return extract_score

# 自定义函数
# Task 2,3 计分函数
# 比例评分法，评分规则：根据正确答案和总选项数比例评分。
def score_proportional(LLMs_answers, correct_answers, max_score):
    correct_set = set(correct_answers)
    LLMs_set = set(LLMs_answers)
    correct_count = len(LLMs_set.intersection(correct_set))
    wrong_count = len(LLMs_set.difference(correct_set))
    total_possible = len(correct_set) + wrong_count
    if total_possible == 0:
        return 0
    return max_score * correct_count / total_possible
    '''
    # 示例
    student_answers = ['C', 'B', 'H',  'I']
    correct_answers = ['B', 'C', 'D']
    max_score = 1
    print(score_proportional(student_answers, correct_answers, max_score))
    '''

# 自定义函数
# Task 4 计分函数
# 计算rouge_L
def lcs_length(s1, s2):
    """
    计算两个字符串的最长公共子序列长度
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# s1: 参考文本
# s2: 生成文本
def rouge_l(s1, s2, beta=1):
    """
    计算 ROUGE-L 分数
    """
    # 避免除以零的错误
    if len(s1) == 0 or len(s2) == 0:
        return 0.0

    lcs_len = lcs_length(s1, s2)

    # 如果LCS长度为0，直接返回0.0
    if lcs_len == 0:
        return 0.0

    r = lcs_len / len(s1)
    p = lcs_len / len(s2)

    # 再次避免除以零的错误
    if r + p == 0:
        return 0.0

    rouge_l_score = ((1 + beta ** 2) * r * p) / (r + beta ** 2 * p)
    return rouge_l_score

# 自定义函数
# 自动计算分数
# 自动计算分数
def automated_score(standard_anwsers_path, submitted_anwsers_path):
    standard_result = []
    submitted_result = []

    # 读入标准答案
    with open(standard_anwsers_path) as f:
        for item in f.readlines():
            standard_result.append(item)

    # 读入用户提交答案
    with open(submitted_anwsers_path) as f:
        for item in f.readlines():
            submitted_result.append(item)

    # 只抽取用户提交答案的唯一病案数
    all_yian = []
    submitted_result_limit = []
    for item in submitted_result:
        yian_item_result_list = item.split('@') 
        if yian_item_result_list[0] not in all_yian:
            submitted_result_limit.append(item)
            all_yian.append(yian_item_result_list[0])
        
    # 任务分数
    task1_score = 0
    task2_score = 0
    task3_score = 0
    task4_score = 0
    for item in submitted_result_limit:
        for item_y in standard_result:
            # 用户提交答案
            item_result_list = item.split('@')
            # 正确答案
            item_y_result_list = item_y.split('@')
            # 对应案例，以防止用户输入错误
            if item_result_list[0] == item_y_result_list[0]:
                # Task1 任务
                if len(item_result_list[1]) <= 0:
                    task1_score = task1_score + 0
                else:
                    submitted_task1_score = clinical_info_extraction_eval(item_result_list[1], item_y_result_list[1].split(';'))
                    task1_score = task1_score + submitted_task1_score
                # Task2 任务
                if len(item_result_list[2]) <= 0:
                    task2_score = task2_score + 0
                else:
                    submitted_task2_score = score_proportional(item_result_list[2].split(';'), item_y_result_list[2].split(';'), 1)
                    task2_score = task2_score + submitted_task2_score
                # Task3 任务
                if len(item_result_list[3]) <= 0:
                    task3_score = task3_score + 0
                else:
                    submitted_task3_score = score_proportional(item_result_list[3].split(';'), item_y_result_list[3].split(';'), 1)
                    task3_score = task3_score + submitted_task3_score
                # Task4 任务
                if len(item_result_list[4]) <= 0:
                    task4_score = task4_score + 0
                else:
                    submitted_task4_score = rouge_l(item_result_list[4], item_y_result_list[4])
                    task4_score = task4_score + submitted_task4_score
    return 0.2 * task1_score + 0.3 * task2_score + 0.4 * task3_score + 0.1 * task4_score


# 错误字典，这里只是示例
error_msg={
    1: "Bad input file",
    2: "Wrong input file format",
}

def dump_2_json(info, path):
    with open(path, 'w') as output_json_file:
        json.dump(info, output_json_file)

def report_error_msg(detail, showMsg, out_p):
    error_dict=dict()
    error_dict['errorDetail']=detail
    error_dict['errorMsg']=showMsg
    error_dict['score']=0
    error_dict['scoreJson']={}
    error_dict['success']=False
    dump_2_json(error_dict,out_p)

def report_score(score, out_p):
    result = dict()
    result['success']=True
    result['score'] = score

    # 这里{}里面的score注意保留，但可以增加其他key，比如这样：
    # result['scoreJson'] = {'score': score, 'aaaa': 0.1}
    result['scoreJson'] = {'score': score}

    dump_2_json(result,out_p)

if __name__=="__main__":
    '''
      online evaluation
      
    '''
    in_param_path = sys.argv[1]
    out_path = sys.argv[2]

    # read submit and answer file from first parameter
    with open(in_param_path, 'r') as load_f:
        input_params = json.load(load_f)

    # 标准答案路径
    standard_path=input_params["fileData"]["standardFilePath"]
    print("Read standard from %s" % standard_path)

    # 选手提交的结果文件路径
    submit_path=input_params["fileData"]["userFilePath"]
    print("Read user submit file from %s" % submit_path)

    try:
        # TODO: 执行评测逻辑
        # 提供自动计算的函数
        # NOTICE: 这个是示例
        score = automated_score(standard_path, submit_path)
        report_score(score, out_path)
    except Exception as e:
        print(e)
        # NOTICE: 这个只是示例
        check_code = 1
        report_error_msg(error_msg[check_code],error_msg[check_code], out_path)
