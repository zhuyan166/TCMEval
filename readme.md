# TCM Evaluation(TCM-Eval): 一个全面、专业的中医测评基准
TCM Evaluation: A comprehensive and professional benchmark for traditional Chinese medicine (TCM)

![image](https://github.com/zhuyan166/TCMEval/blob/main/figs/TCM_bench_logo)<div align=center><img width="250" alt="TCM-Eval Logo" src=""></div>

<h1 align="center">
  <a href="">
    <img src="https://img.shields.io/badge/releases-v0.1-red" />
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/docs-v1.0-yellow" />
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/TCM-Benchmark-blue" />
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/LICENSE-Apache%202.0-brightgreen" />
  </a>
</h1>

## 目录
- [项目介绍](#项目介绍)
- [更新](#更新)
- [文件目录说明](#文件目录说明)
- [组织者](#组织者)
- [引用](#引用)

### 项目介绍
TCM Evaluation(TCM-Eval)是由中医药理论、中医药信息专业背景团队构建的一个中医测评基准，包含了中医药领域如基础研究、临床研究、信息学、政策与管理等方面基础或复杂测评集，可全面评估中医药领域的研究成果、技术水平等方面表现，也可做为中医药领域教育的测试标准，为中医药行业的发展提供有力的支持。

### 更新
[2024/6/1]发布v0.1版本
- 初始化项目
- 发布**中医数据集** v0.1
- 发布**中医方剂分类数据集** v0.1

### 文件目录说明
```
filetree 
├── ARCHITECTURE.md
├── LICENSE.txt
├── README.md
├── /evaluation/
│  ├── /TCMEval-SDT/
│  │  ├── train.json
│  │  └── test.json
│  │  └── readme.md
│  ├── /TCMFormula/
│  │  ├── train.json
│  │  ├── test.json
│  │  ├── validation.json
│  │  └── readme.md
├── readme.md
└── /data/

```

### 组织者
- 朱彦，中国中医科学院基础医学研究所

### 引用
```
todo

# 中医方剂分类数据集
@article{zhe2023bibm,
  title={Traditional Chinese Medicine Formula Classification Using Large Language Models},
  author={Wang, Zhe and Li, Keqian and Ren, Quanying and Yao, Keyu and Zhu, Yan},
  journal={2023 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)},
  year={2023}
}
```
**如果您希望进一步的完善中医药领域的测评集或参与测评集构建工作，请随时联系我们。**

