from wordcloud import WordCloud
from typing import List, Dict
from re import sub
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

IN_PATH: str = 'sherlock.txt'
OUT_PATH: str = 'out/wordify.png'
MIN: int = 3

def main():
    print('Generating Word Cloud...')
    data = load_data(IN_PATH)

    res: Dict = clean_data(data)

    generate_cloud(res)

def load_data(path: str) -> List[str]:
    ignore: List[str] = set(stopwords.words('english'))
    with open(path, 'r') as f:
        data = f.readlines()

    # Join all lines and split the result in words
    data = " ".join(data).split(" ")

    # Clean up the list
    data = list(map(lambda word: str.lower(word), data)) # Lower case
    data = list(filter(lambda word: len(word) > 1, data)) # Remove empty words
    data = list(map(lambda word: sub('[^A-Za-z0-9]+', '', word), data)) # Trim special chars

    # Update and remove ignored words
    data = list(filter(lambda word: word not in ignore, data))  # Remove ignored words

    return data

def clean_data(data: List[str]) -> Dict:
    res: Dict = {}

    for word in data:
        if word in res.keys():
            res[word] += 1
        else:
            res[word] = 1

    res = dict(sorted(res.items(), key=lambda item: item[1]))

    return res

def generate_cloud(res: Dict) -> None:
    wc = WordCloud(
        background_color='white',
        width=1000,
        height=1000,
        max_words=10,
        relative_scaling=0.5,
        normalize_plurals=False
        ).generate_from_frequencies(res)

    wc.to_file(OUT_PATH)

if __name__ == '__main__':
    main()