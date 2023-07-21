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
* `circRNA_set.csv`:A complete mapping from circRNA index IDs to circRNA names.<br/>
* `drug_set.csv`:A complete mapping from drug index IDs to drug meshID, smile and pubchemID.<br/>
* `cancer_set.csv`:A complete mapping from cancer index IDs to cancer meshID, cancer names.<br/>
* `circ2cancer_assoMatrix.csv`:circRNA-cancer association matrix.<br/>
* `circ2drug_assoMatrix.csv`:circRNA-drug association matrix.<br/>
* `cancer2drug_assoMatrix.csv`:cancer-drug association matrix.<br/>
* `circRNA_functional_similarity.csv`:circRNA functional similarity scores.<br/>
* `circRNA_GIP_similarity.csv`:circRNA Gaussian Interaction Profile kernel similarity scores.<br/>
* `circRNA_simfusion.csv`:circRNA fusion similarity scores.<br/>
* `drug_structure_similarity.csv`:drug chemical structure similarity scores.<br/>
* `drug_GIP_similarity.csv`:drug Gaussian Interaction Profile kernel similarity scores.<br/>
* `drug_simfusion.csv`:drug fusion similarity scores.<br/>
* `cancer_semantic_similarity.csv`:cancer semantic similarity scores.<br/>
* `cancer_GIP_similarity.csv`:cancer Gaussian Interaction Profile kernel similarity scores.<br/>
* `cancer_simfusion.csv`:cancer fusion similarity scores.<br/>
* `circRNA_cancer_LabEdgEmbs4LTR.txt`:Input data of learning to rank for circRNA-cancer prediction.<br/>
* `drug_cancer_LabEdgEmbs4LTR.txt`:Input data of learning to rank for drug-cancer prediction.<br/>
Note：1) The header IDs “0-476” in the mentioned dataset can be mapped to specific information about circRNAs, drugs, and cancers by the three mapping files `circRNA_set.csv`, `drug_set.csv`, and `cancer_set.csv`, respectively. 2) See manuscript Section 2.5 for data format details of `circRNA_cancer_LabEdgEmbs4LTR.txt` and `drug_cancer_LabEdgEmbs4LTR.txt`.
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
