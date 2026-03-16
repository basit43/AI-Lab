import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("/Users/app/Downloads/archive/HDFS_2k/HDFS_2k.log_structured.csv")

def loadData():
    df = pd.read_csv(DATA_PATH)
    return df

def exploreData(df):
    print("Dataframe shape:", df.shape)
    print("Columns:", df.columns)
    print("First 5 rows:")
    print(df.head())
    print("Unique event types:", df['EventId'].nunique())
    print("Event type distribution:")
    print(df['EventId'].value_counts())
    print("Unique log levels:", df['Level'].nunique())
    # Plotting the distribution of event types
    plt.figure(figsize=(10, 6))
    df['EventId'].value_counts().plot(kind='bar')
    plt.title('Distribution of Event Types')
    plt.xlabel('Event Type')
    plt.ylabel('Count')
    plt.show()

def visualize_levels(df):
    print("Log level distribution:")
    df['Level'].value_counts().plot(kind='bar')
    plt.title("Log Level Distribution")
    plt.xlabel("Log Level")
    plt.ylabel("Count")
    plt.show()    

def main():
    df = loadData()
    exploreData(df)
    visualize_levels(df)
if __name__ == "__main__":    main()