## 執行（分類）
:::info
Input: a.dat
Output: *class name*, *longest common string*
:::

以"workflow.sh"為執行腳本
進到工作目錄後使用
```
$./workflow.sh a.dat
```
即可得到所屬於的class以及代表最大子圖的code
![](https://i.imgur.com/nUFawCn.png)

### Time measurement
```
$time ./workflow.sh a.dat
```
![](https://i.imgur.com/0anHDNt.png)


## 執行說明：
一開始會先將a.dat依同樣的方式取得各個子圖的code存於"subgraph.txt"
在"classify.py"，將前者最長的code和在“lcs_all_class_dict"各個代表class的最長code，利用LCS演算法取得最大的子圖(longest code)和所在的類別


modify with [https://github.com/ChristalC/Frequent-Subgraph-Mining](https://github.com/ChristalC/Frequent-Subgraph-Mining)

[1]: Huan, Jun, Wei Wang, and Jan Prins. "Efficient mining of frequent subgraphs in the presence of isomorphism." Data Mining, 2003. ICDM 2003. Third IEEE International Conference on. IEEE, 2003. ([pdf](http://www.cs.unc.edu/techreports/03-021.pdf))
