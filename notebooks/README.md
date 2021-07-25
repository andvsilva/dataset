a# Data Science - Landscape

Here I will describe in details each step to do a Machine Learning (ML) project. In the Figure below, we will following this roadmap to guide our studies in data science.

![](figures/data_science_landscape.png)


## Data Pre-processing

- Data Cleaning
- Handling Missing Data
- Obtaining Data
- Feature Engineering
- Feature Selection

### Hands on data cleaning

First, we will explore the dataset using some techniques to make the data cleaning process.

- ```>>> dataset: data/lending_club_loans.csv```

```bash
$ python
Python 3.7.9 (default, Aug 31 2020, 12:42:55) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> df = pd.read_csv('../data/lending_club_loans.csv')
>>> df.shape
(39786, 47)
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 39786 entries, 0 to 39785
Data columns (total 47 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   id                          39786 non-null  int64  
 1   member_id                   39786 non-null  int64  
 2   loan_amnt                   39786 non-null  int64  
 3   funded_amnt                 39786 non-null  int64  
 4   funded_amnt_inv             39786 non-null  float64
 5   term                        39786 non-null  object 
 6   int_rate                    39786 non-null  object 
 7   installment                 39786 non-null  float64
 8   grade                       39786 non-null  object 
 9   sub_grade                   39786 non-null  object 
 10  emp_length                  38708 non-null  object 
 11  home_ownership              39786 non-null  object 
 12  annual_inc                  39786 non-null  float64
 13  verification_status         39786 non-null  object 
 14  issue_d                     39786 non-null  object 
 15  loan_status                 39786 non-null  object 
 16  pymnt_plan                  39786 non-null  object 
 17  zip_code                    39786 non-null  object 
 18  addr_state                  39786 non-null  object 
 19  dti                         39786 non-null  float64
 20  delinq_2yrs                 39786 non-null  int64  
 21  earliest_cr_line            39786 non-null  object 
 22  inq_last_6mths              39786 non-null  int64  
 23  open_acc                    39786 non-null  int64  
 24  pub_rec                     39786 non-null  int64  
 25  revol_bal                   39786 non-null  int64  
 26  revol_util                  39736 non-null  object 
 27  total_acc                   39786 non-null  int64  
 28  initial_list_status         39786 non-null  object 
 29  out_prncp                   39786 non-null  float64
 30  out_prncp_inv               39786 non-null  float64
 31  total_pymnt                 39786 non-null  float64
 32  total_pymnt_inv             39786 non-null  float64
 33  total_rec_prncp             39786 non-null  float64
 34  total_rec_int               39786 non-null  float64
 35  total_rec_late_fee          39786 non-null  float64
 36  recoveries                  39786 non-null  float64
 37  collection_recovery_fee     39786 non-null  float64
 38  last_pymnt_d                39715 non-null  object 
 39  last_pymnt_amnt             39786 non-null  float64
 40  last_credit_pull_d          39784 non-null  object 
 41  collections_12_mths_ex_med  39730 non-null  float64
 42  application_type            39786 non-null  object 
 43  chargeoff_within_12_mths    39730 non-null  float64
 44  delinq_amnt                 39786 non-null  int64  
 45  pub_rec_bankruptcies        39089 non-null  float64
 46  tax_liens                   39747 non-null  float64
dtypes: float64(18), int64(11), object(18)
memory usage: 14.3+ MB
>>> df.isna().sum()
id                               0
member_id                        0
loan_amnt                        0
funded_amnt                      0
funded_amnt_inv                  0
term                             0
int_rate                         0
installment                      0
grade                            0
sub_grade                        0
emp_length                    1078
home_ownership                   0
annual_inc                       0
verification_status              0
issue_d                          0
loan_status                      0
pymnt_plan                       0
zip_code                         0
addr_state                       0
dti                              0
delinq_2yrs                      0
earliest_cr_line                 0
inq_last_6mths                   0
open_acc                         0
pub_rec                          0
revol_bal                        0
revol_util                      50
total_acc                        0
initial_list_status              0
out_prncp                        0
out_prncp_inv                    0
total_pymnt                      0
total_pymnt_inv                  0
total_rec_prncp                  0
total_rec_int                    0
total_rec_late_fee               0
recoveries                       0
collection_recovery_fee          0
last_pymnt_d                    71
last_pymnt_amnt                  0
last_credit_pull_d               2
collections_12_mths_ex_med      56
application_type                 0
chargeoff_within_12_mths        56
delinq_amnt                      0
pub_rec_bankruptcies           697
tax_liens                       39
dtype: int64
>>>

# dictionary feature 

# 1 - annual_inc: .......The self-reported annual income provided by the borrower during registration.
# 2 - chargeoff_within_12_mths: .......Number of charge-offs within 12 months
# 3 - collection_recovery_fee: .......post charge off collection fee
# 4 - collections_12_mths_ex_med: .......Number of collections in 12 months excluding medical collections
# 5 - delinq_2yrs: .......The number of 30+ days past-due incidences of delinquency in the borrower's credit file for the past 2 years
# 6 - delinq_amnt: .......The past-due amount owed for the accounts on which the borrower is now delinquent.
# 7 - dti: .......A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.
# 8 - funded_amnt: .......The total amount committed to that loan at that point in time.
# 9 - funded_amnt_inv: .......The total amount committed by investors for that loan at that point in time.
# 10 - id: .......A unique LC assigned ID for the loan listing.
# 11 - inq_last_6mths: .......The number of inquiries in past 6 months (excluding auto and mortgage inquiries)
# 12 - installment: .......The monthly payment owed by the borrower if the loan originates.
# 13 - int_rate: .......Interest Rate on the loan
# 14 - last_pymnt_amnt: .......Last total payment amount received
# 15 - loan_amnt: .......The listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value.
# 16 - member_id: .......A unique LC assigned Id for the borrower member.
# 17 - open_acc: .......The number of open credit lines in the borrower's credit file.
# 18 - out_prncp: .......Remaining outstanding principal for total amount funded
# 19 - out_prncp_inv: .......Remaining outstanding principal for portion of total amount funded by investors
# 20 - pub_rec: .......Number of derogatory public records
# 21 - pub_rec_bankruptcies: .......Number of public record bankruptcies
# 22 - recoveries: .......post charge off gross recovery
# 23 - revol_bal: .......Total credit revolving balance
# 24 - revol_util: .......Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
# 25 - tax_liens: .......Number of tax liens
# 26 - total_acc: .......The total number of credit lines currently in the borrower's credit file
# 27 - total_pymnt: .......Payments received to date for total amount funded
# 28 - total_pymnt_inv: .......Payments received to date for portion of total amount funded by investors
# 29 - total_rec_int: .......Interest received to date
# 30 - total_rec_late_fee: .......Late fees received to date
# 32 - pub_rec_bankruptcies: .......Number of public record bankruptcies
# 33 - pymnt_plan: .......Indicates if a payment plan has been put in place for the loan
# 34 - recoveries: .......post charge off gross recovery
# 35 - revol_bal: .......Total credit revolving balance
# 36 - revol_util: .......Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
# 37 - sub_grade: .......LC assigned loan subgrade
# 38 - tax_liens: .......Number of tax liens
# 39 - term: .......The number of payments on the loan. Values are in months and can be either 36 or 60.
# 40 - total_acc: .......The total number of credit lines currently in the borrower's credit file
# 41 - total_pymnt: .......Payments received to date for total amount funded
# 42 - total_pymnt_inv: .......Payments received to date for portion of total amount funded by investors
# 43 - total_rec_int: .......Interest received to date
# 44 - total_rec_late_fee: .......Late fees received to date
# 45 - total_rec_prncp: .......Principal received to date
# 46 - verification_status: .......Indicates if income was verified by LC, not verified, or if the income source was verified
# 47 - zip_code: .......The first 3 numbers of the zip code provided by the borrower in the loan application.
```

## Tasks

```bash
@andvsilva
## Done so far 2021-07-20 11h32 
- impute mode (category feature) and mean value to the missing data
- convert object (string) to category
- convert object (number) to float64

# Next thing to do  2021-07-21 17h18 - done
- Check for outliers.
- Using boxplot to look for outlier for each column.

# Sat Jul 24 21:15:40 -03 2021 done
# Working on - Exploring it and understanding what feature 
# each column represents. 
A nice way to show the data is using 'pandas_profiling' 
(see the documentation for more information, link in resources)

# Next explore dataset in more details

- dictionary features - notebook - cleaning already.

# To prepare the dataset feather file format to feature selection
```

- [report-lending_club_loans.html](notebooks/reports/lending_club_loans.html)
### resources

- [A Straightforward Guide to Cleaning and Preparing Data in Python](https://towardsdatascience.com/a-straightforward-guide-to-cleaning-and-preparing-data-in-python-8c82f209ae33)
- [Ways to Detect and Remove the Outliers](https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba)
- [Detecting And Treating Outliers In Python — Part 1](https://towardsdatascience.com/detecting-and-treating-outliers-in-python-part-1-4ece5098b755)
- [Pandas Profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)
