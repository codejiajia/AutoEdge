# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math
##get node feature
cancer = pd.read_csv('./cancer_simfusion.csv', header=0, encoding='gb18030').values
drug = pd.read_csv('./drug_simfusion.csv', header=0, encoding='gb18030').values
circ = pd.read_csv('./circRNA_simfusion.csv', header=0, encoding='gb18030').values
cancer = np.mat(cancer)
drug = np.mat(drug)
circ = np.mat(circ)
node_feature = np.zeros([478, 408])
for m in range(0,408):
    for n in range (0,408):
        node_feature[m, n] = circ[m,n]
for m in range(408,432):
    for n in range (0,24):
        node_feature[m, n] = drug[m-408,n-24]  
for m in range(432,478):
    for n in range (0,46):
        node_feature[m, n] = cancer[m-432,n-46]
result = pd.DataFrame(node_feature)
result.to_csv('./node_feature.csv')
#get edge index
cancer2drug = pd.read_csv('./cancer2drug_assoMatrix.csv', header=None, encoding='gb18030').values
circ2cancer = pd.read_csv('./circ2cancer_assoMatrix.csv', header=None, encoding='gb18030').values
circ2drug = pd.read_csv('./circ2drug_assoMatrix.csv', header=None, encoding='gb18030').values
cancer2drug = np.mat(cancer2drug)
circ2cancer = np.mat(circ2cancer)
circ2drug = np.mat(circ2drug)
edge_index = np.zeros([2343,2]) 
i=0
for m in range(0,408):
    for n in range (0,46):
        if circ2cancer[m,n]==1:
            edge_index[i,0]=m
            edge_index[i,1]=407+24+n
            i+=1
j=614
for m in range(0,408):
    for n in range (0,24):
        if circ2drug[m,n]==1:
            edge_index[j,0]=m
            edge_index[j,1]=407+n
            j+=1
k=1811
for m in range(0,46):
    for n in range (0,24):
        if cancer2drug[m,n]==1:
            edge_index[k,0]=407+24+m
            edge_index[k,1]=407+n
            k+=1
result = pd.DataFrame(edge_index)
result.to_csv('./edge_index.csv')