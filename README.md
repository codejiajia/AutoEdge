# AutoEdge
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
## Usage
* Run data_preprocessing.py using command:<br/>
  ```
  >>python ./code/data_preprocessing.py
  ```
* Run main.py using command:<br/> 
  ```
  >>python ./code/main.py
  ```
  Output files of main.py in data folder: `train_embeddings.csv`, `validation_embeddings.csv`, `test_embeddings.csv`
* Convert the three embedded files into the format required by Ranklib：<br/>
  Label qid:qid feature_id:value feature_id:value ... feature_id:value<br/>
  Example: 1 qid:5 1:0.5723 2:0.4280 3:1.3428 ... 100:4.287
* Run RankLib-2.16.jar<br/> 
  train:<br/>
  ```
  >> java -jar bin/RankLib.jar -train train.txt -ranker 6  -metric2t NDCG@10  -tree 1000 -shrinkage 0.1 -tc 256 -mls 1 -save model.txt
  ```
  test:<br/>
  ```
  >> java -jar bin/RankLib.jar -load model.txt -rank test.txt -score score.txt
  ```
