# 决明测评集
### TCM Evaluation(TCM-Eval)
<a href="https://github.com/zhuyan166/TCMEval">
  <img src="https://github.com/zhuyan166/TCMEval/blob/main/figs/TCM_bench_logo.png" alt="Logo">
</a>
TCM-Eval: A comprehensive and professional benchmark for traditional Chinese medicine (TCM)
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
    <img src="https://img.shields.io/badge/LICENSE-CC BY NC ND 4.0-brightgreen" />
  </a>
</h1>

([English](readme.md)) | ([简体中文](readme_zh.md))

## 目录
- [项目介绍](#项目介绍)
- [更新](#更新)
- [文件目录说明](#文件目录说明)
- [组织者](#组织者)
- [引用](#引用)

### 项目介绍
决明测评集（TCM Evaluation，TCM-Eval）是由具备中医药理论、中医药信息专业背景的杏息树下团队构建的一个综合性中医测评基准，包含了中医药领域如基础研究、临床研究、信息学、政策与管理等方面基础或复杂测评集，可全面评估中医药领域的研究成果、技术水平等方面表现，也可做为中医药教育领域测试标准，为中医药行业的发展提供有力的支持。

### 更新
[2024/6/7]
- 发布**中国中医专业研究生考试数据集** v0.1

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
│  ├── /TCMEval-Formula/
│  │  ├── TCMEval-Formula-example.xlsx
│  │  └── readme.md
│  ├── /TCMEval-CPE/
│  │  ├── TCMEval-CPE-example.xlsx
│  │  └── readme.md
├── readme.md
└── /data/

```

### 组织者
- 朱彦，中国中医科学院中医药信息研究所
- 王哲，中国医学科学院基础医学研究所
- 黄玉燕，中国中医科学院中医基础理论研究所

#### 学生：
- 郝梦，中国中医科学院中医药信息研究所
- 李可千，长春中医药大学医药信息学院
- 王柏沣，北京中医药大学

### 引用
If you find our work useful for your research, please consider citing it:
```
- Chinese Postgraduate Examination Dataset
@article{wang2024XXX,
  title={Performance of GPT-4 and Mainstream Chinese LargeLanguage Models on the Chinese Postgraduate Examination Dataset: Potential for AI-assisted TraditionalChinese Medicine},
  author={Baifeng Wang, Meiwei Zhang, Zhe Wang, Keyu Yao, Meng Hao,  Junhui Wang, Suyuan Peng, Yan Zhu},
  journal={XXXX},
  year={2024}
}

- TCM Formula Classification Dataset
@article{wang2023bibm,
  title={Traditional Chinese Medicine Formula Classification Using Large Language Models},
  author={Zhe Wang, Keqian Li, Quanying Ren, Keyu Yao, Yan Zhu},
  journal={2023 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)},
  year={2023}

- todo
```

**如果您希望进一步的完善中医药领域的测评集或参与测评集构建工作，请随时联系我们（zhuyan166@126.com）。**

