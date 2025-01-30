import os
import pandas as pd

output_file = "RawTrainingData/training_data.csv"

def cnbc_news_data(input_file = "RawTrainingData/cnbc_news_data.csv"):
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist. Skipping...")
        return
    data = pd.read_csv(input_file)
    processed_data = data[['description', 'category']]
    processed_data.to_csv(output_file, index=False)
    print(f"Processed {input_file}")
    os.remove(input_file)

def bbc_news_data(input_file = "RawTrainingData/bbc_text_cls new.csv"):
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist. Skipping...")
        return
    data = pd.read_csv(input_file)
    processed_data = data[['text', 'labels']]
    processed_data.to_csv(output_file, index=False)
    print(f"Processed {input_file}")
    os.remove(input_file)

def main():
    print(f"Creating {output_file}...")
    cnbc_news_data()
    bbc_news_data()
    print(f"Processed CSV into {output_file}")

if __name__ == "__main__":
    main()