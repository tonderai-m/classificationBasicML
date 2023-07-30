import pandas as pd
import os
import click
from sklearn.model_selection import train_test_split

def assemble_data(datasets: list):
    return pd.concat(datasets)

def combine_text_features(dataset: pd.DataFrame, cols: list, target_col: str):
    dataset[cols] = dataset[cols].astype(str)
    dataset['description'] = dataset[cols].agg(' '.join, axis=1)
    return dataset[['description', target_col]]

def class_based_split(dataset: pd.DataFrame, target_col: str):
    X = dataset[[x for x in dataset.columns if x != target_col]]
    y = dataset[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2022, test_size=0.2)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = pd.read_csv("data/combined_data.csv")
    df = combine_text_features(df, ['Product Description', 'Size'], 'Category Description')
    X_train, X_test, y_train, y_test = class_based_split(df, "Category Description")
    X_train = pd.DataFrame(X_train)
    X_train["Category Description"] = y_train
    print(X_train.columns)
    X_test = pd.DataFrame(X_test)
    X_test["Category Description"] = y_test
    X_train.to_csv("data/training_data.csv", index=False)
    X_test.to_csv("data/test_data.csv", index=False)

    
