# AutoEdge-CCP
A novel cancer-centric multi-association prediction model based on multi-source heterogeneous network integrating node intrinsic attribute information and link information.<br/>
![image](https://github.com/codejiajia/AutoEdge-CCP/blob/main/framework.jpg)
<br/>
Please see our manuscript for more details.<br/>
## Requirements
* python>=3.7<br/>
* pytorch>=1.11<br/>
* pyg>=2.0<br/>
* numpy>=1.20<br/>
* networkx>=2.6<br/>
* pandas>=1.3<br/>
* scikit-learn>=1.0<br/>
* Java environment
## Code and Data
* `data_preprocessing.py`:Obtaining node features and edge indices of the multi-source heterogeneous network.<br/>
* `main.py`:Extracting edge features from the multi-source heterogeneous network.<br/>
## Usage
* Here, we provide a demo for the first application scenario:"associated cancer ranking for novel queries." Depending on the specific prediction task, data for `${train.txt}` and `${test.txt}` can be obtained from either `data/circRNA-cancer` or `data/drug-cancer`.  <br/> 
  train:<br/>
  ```
  >> java -jar bin/RankLib.jar -train ${train.txt} -ranker 6  -metric2t NDCG@10  -tree 1000 -shrinkage 0.1 -tc 256 -mls 1 -save model.txt
  ```
  test:<br/>
  ```
  >> java -jar bin/RankLib.jar -load model.txt -rank ${test.txt} -score score.txt
  ```
