
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import numpy as np
from os import path

timesData = pd.read_csv("timesData.csv")

x2011 = timesData.country[timesData.year == 2011]
plt.subplots(figsize=(8,8))
wordcloud = WordCloud(
                          background_color='white',
                          width=1200,
                          height=900
                         ).generate(" ".join(x2011))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('graph.png')

plt.show()