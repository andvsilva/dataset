## Data Cleaning

To train our skills in data cleaning, let's go to make an example using the dataset from ```kaggle```

### Download dataset

```bash
# install kaggle API to download
pip install kaggle
```

#### API token

![API token](figures/key_token.png)

```bash
# download the API token 'kaggle.json'

mkdir ~/.kaggle/
mv ~/.kaggle/kaggle.json

# Done, now we can download from kaggle using API.

# list datasets, e.g. dataset titanic

$ ~/repo/dataset/data
$ kaggle datasets list -s 'titanic'
```

![API token](figures/dataset_list_titanic.png)

# Hands on

```bash
$ kaggle datasets list -s 'NFL Play by Play 2009-2017'                     
ref                                                       title                                        size  lastUpdated          downloadCount  voteCount  usabilityRating  
--------------------------------------------------------  ------------------------------------------  -----  -------------------  -------------  ---------  ---------------  
maxhorowitz/nflplaybyplay2009to2016                       Detailed NFL Play-by-Play Data 2009-2018    274MB  2018-12-22 05:39:34          21880        601  0.6764706        
omzqwonxei/nfl-passing-statistics-20092018                NFL Passing Statistics 2009-2018            108KB  2019-08-19 09:14:57            482          4  0.7058824        
salimoussayfi/nfl-play-by-play-20092016-v3csv             NFL Play by Play 2009-2016 (v3).csv          67MB  2021-05-14 06:45:09             66          5  0.29411766       
tobycrabtree/nfl-scores-and-betting-data                  NFL scores and betting data                 235KB  2021-05-15 14:59:36          10854        243  1.0              
timoboz/superbowl-history-1967-2020                       Superbowl History 1967 - 2020                 2KB  2020-02-03 23:41:14           5288        219  1.0              
toddsteussie/nfl-play-statistics-dataset-2004-to-present  NFL Play Statistics dataset (primary)       135MB  2020-04-27 22:34:06           1780         68  1.0              
maxhorowitz/nflplaybyplay2015                             Detailed NFL Play-by-Play Data 2015           2MB  2016-10-03 02:16:14           3850         72  0.5882353        
kendallgillies/nflstatistics                              NFL Statistics                               12MB  2017-06-09 15:54:44          10006        189  0.7058824        
speckledpingu/nfl-qb-stats                                Quarterback Stats from 1996 - 2016          394KB  2017-01-12 16:37:50           2519         36  0.8235294        
zynicide/nfl-football-player-stats                        NFL Football Player Stats                    33MB  2017-12-08 03:40:48           3275        109  0.875            
ttahara/nfl-impact-detection-train-frames                 NFL-ID: Extracted Frames From Train Videos   62GB  2020-12-05 06:36:51            231         24  0.75             
jpmiller/nfl-competition-data                             🏈  NFL Concussion Data                       11KB  2019-01-05 05:34:41            673          9  0.5588235        
its7171/nfl-models                                        nfl-models                                  828MB  2020-11-28 02:03:43            509         10  0.3125           
its7171/nfl-lib                                           nfl-lib                                     459KB  2020-11-29 06:48:23            484         10  0.3125           
savvastj/nfl-combine-data                                 NFL combine data                            168KB  2018-04-26 19:12:54           1247         32  0.29411766       
tombliss/nfl-big-data-bowl-2021-bonus                     Nfl Big Data Bowl 2021 Bonus                101KB  2020-10-22 17:42:29            431          8  0.3529412        
patrickmurphy/nfl-arrests                                 NFL Arrests 2000-2017                        50KB  2017-04-05 23:16:02           1055         19  0.64705884       
robikscube/helmet-assignment-helpers                      NFL Helmet Assignment Helper Code            12KB  2021-08-19 16:41:49             87          8  0.875            
dtrade84/2019-nfl-scouting-combine                        2019 NFL Scouting Combine                     8KB  2019-03-28 17:32:05            384          8  0.7647059        
washingtonpost/nfl-arrests                                NFL Arrests                                  11KB  2016-11-27 21:18:12           1201         11  0.8235294 

$ kaggle datasets download -d salimoussayfi/nfl-play-by-play-20092016-v3csv
Downloading nfl-play-by-play-20092016-v3csv.zip to /home/andsilva/repo/dataset/kaggle
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉| 67.0M/67.0M [00:09<00:00, 7.38MB/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 67.0M/67.0M [00:09<00:00, 7.21MB/s]
(base) 

# unzip
$ unzip nfl-play-by-play-20092016-v3csv.zip
# remove file zip 
$ rm -rf nfl-play-by-play-20092016-v3csv.zip

# change name of the file csv
$ mv NFL\ Play\ by\ Play\ 2009-2016\ \(v3\).csv NFL_play_2009-2016.csv

$ python                                                              
Python 3.8.11 (default, Aug  3 2021, 15:09:35) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> df = pd.read_csv("NFL_play_2009-2016.csv")
sys:1: DtypeWarning: Columns (25,51) have mixed types.Specify dtype option on import or set low_memory=False.
>>> df
              Date      GameID  Drive  qtr  down   time  ...  Away_WP_post  Win_Prob       WPA    airWPA    yacWPA  Season
0       2009-09-10  2009091000      1    1   NaN  15:00  ...      0.453567  0.485675  0.060758       NaN       NaN    2009
1       2009-09-10  2009091000      1    1   1.0  14:53  ...      0.448912  0.546433  0.004655 -0.032244  0.036899    2009
2       2009-09-10  2009091000      1    1   2.0  14:16  ...      0.489207  0.551088 -0.040295       NaN       NaN    2009
3       2009-09-10  2009091000      1    1   3.0  13:35  ...      0.538783  0.510793 -0.049576  0.106663 -0.156239    2009
4       2009-09-10  2009091000      1    1   4.0  13:27  ...      0.441071  0.461217  0.097712       NaN       NaN    2009
...            ...         ...    ...  ...   ...    ...  ...           ...       ...       ...       ...       ...     ...
362442  2017-01-01  2017010102     20    4   1.0  00:22  ...      0.906565  0.051901  0.041534  0.041534  0.000000    2016
362443  2017-01-01  2017010102     20    4   NaN  00:13  ...      0.965931  0.093435 -0.059366       NaN       NaN    2016
362444  2017-01-01  2017010102     21    4   NaN  00:13  ...      0.964292  0.965931 -0.001639       NaN       NaN    2016
362445  2017-01-01  2017010102     21    4   1.0  00:12  ...      1.000000  0.964292  0.035708       NaN       NaN    2016
362446  2017-01-01  2017010102     21    4   NaN  00:00  ...      1.000000  0.934245  0.000000       NaN       NaN    2016

[362447 rows x 102 columns]
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 362447 entries, 0 to 362446
Columns: 102 entries, Date to Season
dtypes: float64(33), int64(31), object(38)
memory usage: 282.1+ MB

```

## To Clean

```bash
code clean.ipynb
```

### Cle


## Resources

[Kaggle API](https://github.com/Kaggle/kaggle-api#datasets)

[How to Use Kaggle](https://www.kaggle.com/docs/api)

[How to Search and Download Data using Kaggle API?](https://towardsdatascience.com/how-to-search-and-download-data-using-kaggle-api-f815f7b98080)
