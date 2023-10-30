import matplotlib.pyplot as plt
from wordcloud import WordCloud

from utils.filepath import DATA_FILEPATH
from utils.loader import load_data

if __name__ == "__main__":
    data = load_data(DATA_FILEPATH)
    company_counts = dict(data["company"].value_counts())

    wc = WordCloud(background_color="white", max_words=1000)
    wc.generate_from_frequencies(company_counts)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
