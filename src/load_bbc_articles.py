import os

def load_bbc_articles(data_dir="../data/BBC News Summary/News Articles"):
    articles = []
    labels = []

    for category in os.listdir(data_dir):
        category_path = os.path.join(data_dir, category)
        if os.path.isdir(category_path):
            for filename in os.listdir(category_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(category_path, filename)
                    with open(file_path, "r", encoding="latin-1") as f:
                        content = f.read().strip()
                        articles.append(content)
                        labels.append(category)
    return articles, labels