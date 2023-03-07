#%%


from pdfminer.high_level import extract_text
from glob import glob
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import re

applicants = glob("*.pdf")

#%%

# Define a function to plot word cloud
def plot_cloud(wordcloud, file_name):
    # # Set figure size
    # plt.figure(figsize=(40, 30))
    # # Display image
    # plt.imshow(wordcloud)
    # # No axis details
    # plt.axis("off")
    # save image
    plt.savefig(f"{file_name}.png")


for app in applicants:
    file_name = os.path.splitext(app)[0]
    text = extract_text(app)

    comment_words = ""
    stopwords = set(STOPWORDS)

    # Clean text
    text = re.sub(r"==.*?==+", "", text)
    text = text.replace("\n", "")

    wordcloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="salmon",
        colormap="Pastel1",
        collocations=False,
        stopwords=STOPWORDS,
    ).generate(
        text
    )  # Plot
    plot_cloud(wordcloud, file_name)

# %%

import pandas as pd

pd.read_excel(r"./2023 MS Apps Geog.xlsx")
for app in applicants:
    file_name = os.path.splitext(app)[0]
    text = extract_text(app)

    comment_words = ""
    stopwords = set(STOPWORDS)

    # Clean text
    text = re.sub(r"==.*?==+", "", text)
    text = text.replace("\n", "")

    # get gwid
    gwid = re.search(r"[a-zA-Z][0-9]{8}", text).group(0)
#%%
list(wordcloud.words_.keys())
# list(a)
#%%

# %%
