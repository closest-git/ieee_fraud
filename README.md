This tutorial demonstrates how to use [LiteMORT](https://github.com/closest-git/LiteMORT "LiteMORT") to solve [IEEE-CIS Fraud Detection competition](https://www.kaggle.com/c/ieee-fraud-detection/overview "IEEE-CIS Fraud Detection competition").Both data and most codes are forked from kyakovlev's notebook (https://www.kaggle.com/kyakovlev/ieee-simple-lgbm). I just add LiteMORT to compare performace with LightGBM.
##### 1）To reach the same accurary of LightGBM, LiteMORT only need less than half the time.
##### 2）Public Score of this demo is 0.949.

Detailed steps are as follows
1. Download three pkl files from https://www.kaggle.com/kyakovlev/ieee-fe-with-some-eda
Thanks very much for kyakovlev's work. I'm busy in developing LiteMORT. So have little time to do EDA.
1. Run the following command in Anaconda:
`python case_ieee_fraud.py mort`
