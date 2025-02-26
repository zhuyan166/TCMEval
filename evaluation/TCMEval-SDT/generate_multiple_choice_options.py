import pandas as pd
import random


def combine_lists(list1, list2):
    if len(list1) > 10:
        raise ValueError("The length of list1 cannot exceed 10")

    # Ensure that the value selected from list2 is not in list1
    list2_filtered = [item for item in list2 if item not in list1]

    # Randomly select item from list2_filtered up to 10
    remaining_slots = 10 - len(list1)
    additional_items = random.sample(list2_filtered, remaining_slots)

    # Merge and random list1 and additional_items
    combined_list = list1 + additional_items
    random.shuffle(combined_list)

    result = [f"{chr(ord('A') + idx)}:{item}" for idx, item in enumerate(combined_list)]
    positions = [chr(ord('A') + combined_list.index(item)) for item in list1]

    positions.sort()
    return positions, result



if __name__ == '__main__':
    tcm_data = pd.read_excel('path_to_final_data.xlsx')
    bingji_list = []
    zhenghou_list = []

    for _, item in tcm_data.iterrows():
        # collect all TCM Pathogenesis 
        if ';' in item[5]:
            item_bingji_list = item[5].split(';')
            for item_y in item_bingji_list:
                bingji_list.append(item_y)
        else:
            bingji_list.append(item[5])

        #collect all TCM Syndrome
        if ';' in item[6]:
            item_zhenghou_list = item[6].split(';')
            for item_y in item_zhenghou_list:
                zhenghou_list.append(item_y)
        else:
            zhenghou_list.append(item[6])

    result = []

    for _, item in tcm_data.iterrows():
        item_bingji_list = []
        item_zhenghou_list = []

        if ';' in item[5]:
            item_bingji_list = item[5].split(';')
        else:
            item_bingji_list.append(item[5])

        if ';' in item[6]:
            item_zhenghou_list = item[6].split(';')
        else:
            item_zhenghou_list.append(item[6])

        item_bingji_right_answer, item_bingji_xuanxiang = combine_lists(item_bingji_list, bingji_list)
        item_zhenghou_right_anwser, item_zhenghou_xuanxiang = combine_lists(item_zhenghou_list, zhenghou_list)
        result.append([item[0],item[1],item[2],item[3],item[4],item[5],';'.join(item_bingji_right_answer),';'.join(item_bingji_xuanxiang),item[6],';'.join(item_zhenghou_right_anwser),';'.join(item_zhenghou_xuanxiang),item[7],item[8]])

    pd.DataFrame(result, columns=["案例编号","临床资料","临证体会","辨证","信息抽取能力：核心临床信息","信息抽取能力：核心病机","病机答案","病机选项","信息抽取能力：核心证候","证候答案","证候选项","推理能力：病机推断","推理能力：证候推断"]).to_excel("path_to_final_data.xlsx", index=False)
