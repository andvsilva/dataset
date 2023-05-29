# generator - fake data.
import random
import pandas as pd
import snoop
import feather
import time
import gc
import sys
import feather
from tqdm import tqdm

from faker import Faker
from varname import nameof
from icecream import ic
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Pandas has a high consume of memory RAM usage
def release_memory(df):  # release memory RAM
    del df
    gc.collect() 
    df = pd.DataFrame() # point to NULL
    print('memory RAM released.')

fake = Faker()

def generate_words(ngroup):
    df = pd.DataFrame(columns=['word'])
    
    for i in tqdm(range(800)):
        word = fake.word()
        df.loc[len(df.index)] = [f'{word}']

    countingwords = dict(df['word'].value_counts())
    
    f = open(f'countingwordstxt/countingwords_groups_{ngroup}.txt', "w")
    f.write("{\n")

    for k in countingwords.keys():
        f.write("'{}':'{}'\n".format(k, countingwords[k]))
    
    f.write("}")
    f.close()
    
    text = df['word'].values

    wordcloud = WordCloud().generate(str(text))

    f = plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    #plt.show()
    f.savefig(f"pdfs/wordscloud_group_{ngroup}.pdf", bbox_inches='tight')
    f.savefig(f"pngs/wordscloud_group_{ngroup}.png", bbox_inches='tight')
        
    release_memory(df)
    print('word cloud successfully created!')


for ngroup in range(1,5):
    generate_words(ngroup)
    