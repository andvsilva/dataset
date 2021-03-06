## Dataset

- ```data/housing.csv```

### Data description

```bash
>>> housing.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   longitude           20640 non-null  float64
 1   latitude            20640 non-null  float64
 2   housing_median_age  20640 non-null  float64
 3   total_rooms         20640 non-null  float64
 4   total_bedrooms      20433 non-null  float64
 5   population          20640 non-null  float64
 6   households          20640 non-null  float64
 7   median_income       20640 non-null  float64
 8   median_house_value  20640 non-null  float64
 9   ocean_proximity     20640 non-null  object 
dtypes: float64(9), object(1)
memory usage: 1.6+ MB

>>> housing["ocean_proximity"].value_counts()
<1H OCEAN     9136
INLAND        6551
NEAR OCEAN    2658
NEAR BAY      2290
ISLAND           5
Name: ocean_proximity, dtype: int64

>>> housing.describe()
          longitude      latitude  ...  median_income  median_house_value
count  20640.000000  20640.000000  ...   20640.000000        20640.000000
mean    -119.569704     35.631861  ...       3.870671       206855.816909
std        2.003532      2.135952  ...       1.899822       115395.615874
min     -124.350000     32.540000  ...       0.499900        14999.000000
25%     -121.800000     33.930000  ...       2.563400       119600.000000
50%     -118.490000     34.260000  ...       3.534800       179700.000000
75%     -118.010000     37.710000  ...       4.743250       264725.000000
max     -114.310000     41.950000  ...      15.000100       500001.000000
```

### TODO list

1 - Preprocessing
- [x] Loading dataset (**DONE**)
- [x] Cleaning Dataset (**DONE**)
- [x] Dataset ([feather-format](https://github.com/wesm/feather)) already to do feature engineering

1.1 - **Notebooks/script**
  - [x] [exploredata.ipynb](notebooks/exploredata.ipynb)
  - [x] [preprocessing.py](scripts/preprocessing.py)

2 - Feature Engineering
- [x] [feature engineering notebook](notebook/feature_engineering.ipynb)
- [x] [feature engineering script](script/feature_engineering.py)

3 - Train/Modeling

- [x] [training model](notebook/modeling.ipynb)
    - Model:
        - [CatBoost Documentation](https://catboost.ai/docs):
            ```Bash
            Ease to use categorical features
            Implementation of dataset processing
            Improved accuracy
            ```

4 - Evalutation model
 
- [ ] Evaluate modeling (**WIP**)
- [ ] What we can improve? (**WIP**) 

## Dataset - Club Loans
- ```data/lending_club_loans_2007_2011.csv```

```bash
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 42538 entries, 0 to 42537
Data columns (total 54 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   id                          42538 non-null  object 
 1   member_id                   42535 non-null  float64
 2   loan_amnt                   42535 non-null  float64
 3   funded_amnt                 42535 non-null  float64
 4   funded_amnt_inv             42535 non-null  float64
 5   term                        42535 non-null  object 
 6   int_rate                    42535 non-null  object 
 7   installment                 42535 non-null  float64
 8   grade                       42535 non-null  object 
 9   sub_grade                   42535 non-null  object 
 10  emp_title                   39909 non-null  object 
 11  emp_length                  41423 non-null  object 
 12  home_ownership              42535 non-null  object 
 13  annual_inc                  42531 non-null  float64
 14  verification_status         42535 non-null  object 
 15  issue_d                     42535 non-null  object 
 16  loan_status                 42535 non-null  object 
 17  purpose                     42535 non-null  object 
 18  title                       42522 non-null  object 
 19  zip_code                    42535 non-null  object 
 20  addr_state                  42535 non-null  object 
 21  dti                         42535 non-null  float64
 22  delinq_2yrs                 42506 non-null  float64
 23  earliest_cr_line            42506 non-null  object 
 24  fico_range_low              42535 non-null  float64
 25  fico_range_high             42535 non-null  float64
 26  inq_last_6mths              42506 non-null  float64
 27  open_acc                    42506 non-null  float64
 28  pub_rec                     42506 non-null  float64
 29  revol_bal                   42535 non-null  float64
 30  revol_util                  42445 non-null  object 
 31  total_acc                   42506 non-null  float64
 32  out_prncp                   42535 non-null  float64
 33  out_prncp_inv               42535 non-null  float64
 34  total_pymnt                 42535 non-null  float64
 35  total_pymnt_inv             42535 non-null  float64
 36  total_rec_prncp             42535 non-null  float64
 37  total_rec_int               42535 non-null  float64
 38  total_rec_late_fee          42535 non-null  float64
 39  recoveries                  42535 non-null  float64
 40  collection_recovery_fee     42535 non-null  float64
 41  last_pymnt_d                42452 non-null  object 
 42  last_pymnt_amnt             42535 non-null  float64
 43  last_credit_pull_d          42531 non-null  object 
 44  last_fico_range_high        42535 non-null  float64
 45  last_fico_range_low         42535 non-null  float64
 46  collections_12_mths_ex_med  42390 non-null  float64
 47  policy_code                 42535 non-null  float64
 48  application_type            42535 non-null  object 
 49  acc_now_delinq              42506 non-null  float64
 50  chargeoff_within_12_mths    42390 non-null  float64
 51  delinq_amnt                 42506 non-null  float64
 52  pub_rec_bankruptcies        41170 non-null  float64
 53  tax_liens                   42430 non-null  float64
dtypes: float64(34), object(20)
memory usage: 17.5+ MB
```
### Estrutura do Reposit??rio

```Bash
$ tree                                                                                                                         3ms 
.
????????? commit.sh
????????? data
??????? ????????? cumulative.csv
??????? ????????? cumulative_nohead.csv
??????? ????????? dataset_cleaning.ftr
??????? ????????? dataset_featureselect.ftr
??????? ????????? dataset_preprocessed.ftr
??????? ????????? diabetes.csv
??????? ????????? housing.csv
??????? ????????? kc-house-data
??????? ????????? kc_house_data.csv
??????? ????????? LCDataDictionary.csv
??????? ????????? lending_club_loans.csv
????????? exploredata.ipynb
????????? notebooks
??????? ????????? catboost_info
??????? ??????? ????????? catboost_training.json
??????? ??????? ????????? learn
??????? ??????? ??????? ????????? events.out.tfevents
??????? ??????? ????????? learn_error.tsv
??????? ??????? ????????? time_left.tsv
??????? ??????? ????????? tmp
??????? ????????? cleaning.ipynb
??????? ????????? exploredata.ipynb
??????? ????????? feature_selection.ipynb
??????? ????????? figures
??????? ??????? ????????? data_science_landscape.png
??????? ??????? ????????? feature_importance_model_CatBoost.pdf
??????? ??????? ????????? feature_importance_model_CatBoost.png
??????? ??????? ????????? feature_importance_model_DecisionTree.pdf
??????? ??????? ????????? feature_importance_model_DecisionTree.png
??????? ??????? ????????? feature_importance_model_RandomForest.pdf
??????? ??????? ????????? feature_importance_model_RandomForest.png
??????? ??????? ????????? feature_importance_model_XGBoost.pdf
??????? ??????? ????????? feature_importance_model_XGBoost.png
??????? ????????? modeling.ipynb
??????? ????????? modeling_stacking.ipynb
??????? ????????? README.md
??????? ????????? reports
??????? ??????? ????????? lending_club_loans.html
??????? ????????? requirements.txt
????????? README.md
????????? scripts
    ????????? catboost_info
    ??????? ????????? catboost_training.json
    ??????? ????????? learn
    ??????? ??????? ????????? events.out.tfevents
    ??????? ????????? learn_error.tsv
    ??????? ????????? time_left.tsv
    ??????? ????????? tmp
    ????????? cleaning.py
    ????????? feature_engineering.py
    ????????? figures
    ??????? ????????? feature_importance_model_CatBoost.pdf
    ??????? ????????? feature_importance_model_CatBoost.png
    ??????? ????????? feature_importance_model_DecisionTree.pdf
    ??????? ????????? feature_importance_model_DecisionTree.png
    ??????? ????????? feature_importance_model_RandomForest.pdf
    ??????? ????????? feature_importance_model_RandomForest.png
    ??????? ????????? feature_importance_model_XGBoost.pdf
    ??????? ????????? feature_importance_model_XGBoost.png
    ??????? ????????? scores_importance_models.pdf
    ??????? ????????? scores_models.png
    ????????? logs
    ??????? ????????? feature-eng.dat
    ??????? ????????? info-preprocess.dat
    ??????? ????????? modeling.dat
    ????????? master.py
    ????????? modeling.py
    ????????? preprocessing.py
    ????????? requirements.txt

13 directories, 58 files
```

## [MLFlow](https://mlflow.org/)

### Install 
```bash
pip install mlflow
```

### Run

```bash
~/repo/dataset/examples

$ mlflow run mlflow_housing -P k_features=8

$ mlflow ui

```



- [requirements.txt](requirements.txt) - Lista de bibliotecas utilizadas no projeto. Para instalar essas bibliotecas, basta fazer 
```Bash
$ pip3 install -r requirements.txt

#Para criar o arquivo 'requirements.txt'

basta fazer: 
instalar: freeze usando pip
$ pip3 install freeze

$ pip3 freeze > requirements.txt
```

## Download dataset from Kaggle using command line interface

```bash
# If you want make things much more fast, maybe this 
# can help you
# Install kaggle API.
pip install --user kaggle

# Go to your account on the kaggle and create API Token
# https://www.kaggle.com/HERE-YOUR-USERNAME/account?isEditing=False

# This will trigger the download of kaggle.json
# mv kaggle.json ~/.kaggle
ls ~/.kaggle/kaggle.json

# For security, ensure that other users of your
# computer do not have read access to your credentials.
chmod 600 ~/.kaggle/kaggle.json

# To check if this works?
kaggle competitions download -c titanic
ls
titanic.zip

# Or for general
kaggle competitions download -c dataset_name
```

## Refer??ncias

- [Data Science Starter Kit](https://towardsdatascience.com/data-science-starter-kit-2d8e2291914b): A guide for getting started in data science (**Very good**)

- [Get Interactive plots directly with pandas](https://towardsdatascience.com/get-interactive-plots-directly-with-pandas-13a311ebf426) - A tutorial on creating Plotly and Bokeh plots directly with Pandas plotting syntax

- [All Python Debugging Tools You Need to Know in 2020](https://medium.com/swlh/all-python-debugging-tools-you-need-to-know-in-2020-e3ff66b8f318)
  This can help you in your journey as data science or data engineer, a valuable skill.

- [Machine Learning model overview](https://medium.com/@cs.sabaribalaji/machine-learning-model-overview-8c305f8f6737)

- [A Practical Guide to Exploratory Data Analysis (EDA) in Python ??? How to Start Any Data Analysis.](https://medium.com/analytics-vidhya/a-practical-guide-to-exploratory-data-analysis-eda-in-python-how-to-start-any-data-analysis-3fd200516553)
  - EDA is a must for any data project. It is a critical first step that can make your life easier and shed a light on your data.
 
- [Feature Selection in Large Datasets - Use of Shapash and Scikit-Learn???s Recursive Feature Selection](https://mdsohel-mahmood.medium.com/feature-selection-in-large-datasets-fc27a7e8e388) 

### Programming
- [Introduction to programming](https://beknazarsuranchiyev.medium.com/introduction-to-programming-56dda6a1cbd7)


### Git

- [ Version Control System(VCS)](https://git-scm.com/)
- [The 13 Git Commands I Use Daily](https://medium.com/analytics-vidhya/13-git-commands-i-use-daily-14e3ad562068)
### Python
- [w3schools](https://www.w3schools.com/python/default.asp)
- [Learning Python: From Zero to Hero](https://medium.com/the-renaissance-developer/learning-python-from-zero-to-hero-8ceed48486d5)

### Pandas
- [The Mastery of Pandas - I](https://medium.com/swlh/the-mastery-of-pandas-i-50156db42125)

- [The Mastery of Pandas - II](https://medium.com/analytics-vidhya/the-mastery-of-pandas-ii-bc4cf58c04f5)

 
### Linux

- [20 Basic Linux Commands for Beginners!](https://medium.com/100-days-of-linux/20-basic-linux-commands-for-beginners-78516ab936d6)
- [Basic Linux command line tutorial to start developing in Ubuntu Linux](https://medium.com/@zibon/basic-linux-command-lines-to-get-started-developing-in-ubuntu-linux-b54def1c2190)

### C++

- [How to Learn C++: The Complete Guide for Beginners](https://medium.com/educative/how-to-learn-c-the-complete-guide-for-beginners-eb26b20c7ff0)
- [C++ tutorials](https://www.cplusplus.com/doc/tutorial/variables/)

### Data Science and Machine Learning
- [Notes On Using Data Science & Machine Learning](https://chrisalbon.com/#machine_learning)

  - **Machine Learning - Basics**
  - Vectors, Matrices, And Arrays
  - Preprocessing Structured Data
  - Preprocessing Images
  - Preprocessing Text
  - Preprocessing Dates And Times
  - Feature Engineering
  - Feature Selection
  - Model Evaluation
  - Model Selection
  - Linear Regression
  - Logistic Regression
  - Trees And Forests
  - Nearest Neighbors
  - Support Vector Machines
  - Naive Bayes
  - Clustering
  - **Deep Learning**
    - Setup
    - Keras
    - PyTorch
  - **Python** 
    - Basics
    - Data Wrangling
    - Data Visualization
    - Web Scraping
    - Testing
    - Logging
  - **Statistics**
    - Basics
    - Frequentist
    - Scala
    - Regular Expressions
  - **Snowflake**
    - Basics
    - Tables
  - **PostgreSQL**
    - Basics
    - Add, Delete, Change Rows
    - Merging And Joining
    - Tables
    - Text
    - Numeric
    - Dates
    - Interview Questions
  - **Mathematics**
  - **AWS** Amazon Web Services (AWS) - Cloud Computing Services
  - **Computer Science**
    - Algorithms
  - **Linux Command Line**
    - Basics
    - Inputs And Outputs
    - Search
    - Text
    - Flow Control
    - Processes
    - Shell Scripts
  - **Git And GitHub**
  - **Machine Learning Engineering**
  - **Kubeflow**
  - **Docker**
  - **Dockerfiles**
  - PHP

- [Data Science - medium ](https://medium.com/topic/data-science)
