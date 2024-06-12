# 中国中医研究生考试数据集 
## Chinese Postgraduate Examination Dataset

## 目录
- [测评集介绍](#测评集介绍)
- [更新](#更新)
- [文件目录说明](#文件目录说明)
- [数据](#数据)
- [如何提交](#如何提交)
- [引用](#引用)

### 项目介绍
《2023年全国硕士研究生招生考试临床医学综合能力（中医）试题》为测试集，目前测试集共165道选择题数据。

### 更新
[2024/6/7]
- 发布**中国中医专业研究生考试数据集-例子** v0.1

### 文件目录说明
- TCMEval-CPE-example.xlsx: 中医专业研究所考试数据集-例子
- readme.md: 数据集说明文件

### 数据
#### 说明
- Number: 题目编号
- Type: 题目类型（单选题、多选题）
- Subject: 科目
- Question: 问题

#### 如何测试
在我们发布数据集时，我们使用了prompt进行测试
```
"以下是中国关于临床医学综合能力（中医）考试的单项选择题，请选出其中的正确答案,并生成一段正确、合理的答案解析。
"阴中求阳"的理论依据是( )
A.阳得阴制而不亢逆 B.阴得阳助而不凝滞 C.阳得阴助而生化无穷 D.阴得阳升是泉源不竭"

*LLMs 回复:
"正确答案是A.阳得阴制而不亢逆。

""阴中求阳""的理论依据是阳得阴制而不亢逆。这句话是指在中医治疗中，为了达到阴阳平衡的目的，在补阳的同时，也要补阴，这样可以使阳得到阴的制约，不会过于亢盛而引起阴阳失衡。因此，选项A是正确答案。"

*正确答案:
C
```
#### 测试结果
```
以《2023年全国硕士研究生招生考试临床医学综合能力（中医）试题》为测试集，对文心一言、智谱清言、讯飞星火和GPT-4四种大语言模型进行测试评分，并统计其在不同科目上的表现，利用逻辑推理能力、内部信息使用能力和外部信息使用能力这三个定性指标对输出答案进行评估。 结果显示，文心一言和智谱清言的考试得分通过了国家分数线，正确率分别为50.30%和46.67%。文心一言、智谱清言和GPT-4在不同科目上的表现差异有统计学意义，在医学人文精神类问题上表现最好。逻辑推理：智谱清言和GPT-4对每个答案选择都进行了逻辑解释，文心一言和讯飞星火分别有98.2%和43.6%的回答提供了逻辑推理。内部信息：智谱清言与GPT-4在所有的答案解析中都呈现了内部信息，讯飞星火呈现的数量明显偏低。外部信息：文心一言、智谱清言和GPT-4均有超过60%的回答提供了外部信息，正确答案包含外部信息的频率没有明显高于错误答案。在讯飞星火中，是否存在内部信息、外部信息的回答正确率差异有统计学意义(P<.001)。
```
#### Table 
##### Table 1 The performance of LLMs on different subjects
<img  alt="Table 1" src="https://github.com/zhuyan166/TCMEval/blob/main/figs/TCMEval-CPE-Figs/Table1.jpg"></div>

##### Table 2 Performance of LLMs' responses in evaluating indicators
<img  alt="Table 2" src="https://github.com/zhuyan166/TCMEval/blob/main/figs/TCMEval-CPE-Figs/Table2.jpg"></div>

##### Table 3 Statistical breakdown of reasons for incorrect responses
<img  alt="Table 2" src="https://github.com/zhuyan166/TCMEval/blob/main/figs/TCMEval-CPE-Figs/Table3.jpg"></div>

### 如何提交
您首先需要准备一个 excel文件，并按照以下格式编写。
**Number, The chosen answer from response **
共两列，然后提交到我们的邮箱。

### 引用
If you find our work useful for your research, please consider citing it:

```
@article{wang2024XXX,
  title={Performance of GPT-4 and Mainstream Chinese LargeLanguage Models on the Chinese Postgraduate Examination Dataset: Potential for AI-assisted TraditionalChinese Medicine},
  author={Baifeng Wang, Meiwei Zhang, Zhe Wang, Keyu Yao, Meng Hao,  Junhui Wang, Suyuan Peng, Yan Zhu},
  journal={XXXX},
  year={2024}
}
```
