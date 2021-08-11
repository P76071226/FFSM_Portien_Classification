# Portien classfication
Portien Classfication based on FFSM graph mining.


## 建置環境
1. `make`
2. `g++ -o PDBformater.o PDBformater.cpp`



## 前處理：
先將所有不同蛋白質的class的pdb檔案，利用PDBformater轉換成.dat檔案以符合FFSM讀入的形式。如已處理完的資料夾`db_formate`


```
./PDBformater.o <pdf_file_path> > <dat_file_path>
```

FOR EXAMPLE:
```
./PDBformater.o 4n41.pdb > 4n41.dat
```


## 實驗執行(default dataset:db_formate)
輸出各**class平均時間**與**預測準確度**
輸出檔名`exp_result.csv`
執行以下指令:
1. `cd exp`
2. `python3 run_exp.py`


## 執行流程說明：
在run_exp.py中
將P1（FFSM演算法的執行檔）以.dat檔案為輸入取得各個子圖的code存於`subgraph.txt`,並透過`classfy.py`檔案以LCS概念來做分類預測

## Statement

modify with [https://github.com/ChristalC/Frequent-Subgraph-Mining](https://github.com/ChristalC/Frequent-Subgraph-Mining)

[1]: Huan, Jun, Wei Wang, and Jan Prins. "Efficient mining of frequent subgraphs in the presence of isomorphism." Data Mining, 2003. ICDM 2003. Third IEEE International Conference on. IEEE, 2003. ([pdf](http://www.cs.unc.edu/techreports/03-021.pdf))
