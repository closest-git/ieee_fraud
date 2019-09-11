This tutorial demonstrates how to use [LiteMORT](https://github.com/closest-git/LiteMORT "LiteMORT") to solve [IEEE-CIS Fraud Detection competition](https://www.kaggle.com/c/ieee-fraud-detection/overview "IEEE-CIS Fraud Detection competition").Both data and most codes are forked from kyakovlev's notebook (https://www.kaggle.com/kyakovlev/ieee-simple-lgbm). I just add LiteMORT to compare performace with LightGBM.
##### 1）To reach the same accurary of LightGBM, LiteMORT only need less than half the time.
##### 2）Public Score of this demo is 0.949.

Detailed steps are as follows
1. Download three pkl files(remove_features.pkl,test_df.pkl,train_df.pkl) from https://www.kaggle.com/kyakovlev/ieee-fe-with-some-eda.
(Thanks very much for kyakovlev's work. )
1. Run the following command in Anaconda:
`python case_ieee_fraud.py mort`

I'm busy in developing LiteMORT. So have little time to do EDA.I would join a team with rich experience in feature engineering. If any team need an expert in gradient boosting algorithm, please contanct me. Feature engineering is the key in many practical applications and kaggle competitions. It's really hard to do automatic feature engineering to improve GBDT. Any suggestion are welcome.
