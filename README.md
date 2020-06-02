# Use-Dynamic-network-embedding-for-Social-Network-Aligment-
###in this part, I will provide many tools for social networking, Link prediction and so on
#### We use this paper for dynamic social network alignment：
#### Dynamic Network Embedding: An Extended Approach for Skip-gram based Network Embedding
#### Authors: Lun Du, YunWang, Guojie Songy, Zhicong Lu, Junshan Wang
#### https://www.ijcai.org/Proceedings/2018/288
We use this work to do dynamic Social-Network-Aligment
You should frist 
                              run  'comebine_network.py',
      the data comes from IONE(Aligning Users Across Social Networks Using Network Embedding),With the permission of sharing anonymous twitter_foursquare data from Prof.Jiawei Zhang, we share the anonymous data and code of IONE here. the data and code only can be used for research purposes.
then:
```shell
# running the following command in code repos
conda env create -f dne_env.yml
c
```
- Using the following command in `./src` directory:
```shell
python main.py --conf amherst0.25
```

###data
1\twitter or foursquare
278  5
6    5
56  5
... ...

meas node 278 link with node 5 with network
2\train or test
1
2
5
6
meas this is the anchor node, you can use 'devite_node.py' clip train file and test file for 10%-90%

###last
  You can
  
           run 'result.py'  to get this work's result
