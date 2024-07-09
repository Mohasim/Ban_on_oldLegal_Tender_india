
# Notban Analysis

This project consists of analyzing data from a CSV file named `notbandhi1.csv` which contains information related to social media posts created with the use Tweeter's API(2021),now Known as "X" . The analysis is performed by two Python scripts: `notebanmapper.py` and `notebanreducer.py`.

NotBan Refers to the ban of old legal tender notes of 500 and 1000 INR. This analysis of tweets was done to figure out the general attitude towards such a sudden ban. 

## Data Format

The CSV file `notbandhi1.csv` includes columns for favorited status, favorite count, reply to screen name, creation date, ID, reply to user ID, status source, screen name, retweet count, is retweet, and retweeted status. Here's a brief overview of the data format:

```
favorited, favoriteCount, replyToSN, created, Id, replyToUID, statusSource, screenNam, retweetCount, isRetweet, retweeted
```

## Scripts

### notebanmapper.py

This script processes each line of the input CSV file, extracting relevant fields, and prints them in a comma-separated format. It's designed to work with streaming input/output, making it suitable for large datasets.

[notbanmapper.py](notebanmapper.py) performs the initial processing of the data, preparing it for further analysis.

### notebanreducer.py

After the mapper processes the data, [notebanreducer.py](notebanreducer.py) takes over to perform the reduction operation. It reads the processed data, aggregates it based on unique IDs, and performs calculations to determine the total number of posts that were not favorited and the total number of posts based on favorite counts.

## Usage

To use these scripts, pipe the output of `notebanmapper.py` into `notebanreducer.py` as follows:

```sh
cat notbandhi1.csv | python notebanmapper.py | python notebanreducer.py
```

This will output the analysis results to the console.

## Requirements

- Python 3.x
- Access to a Unix-like terminal (for using the `cat` command and pipes)

## Data Analysis

The analysis focuses on two main aspects:

1. The total number of posts that were not favorited.
2. The total number of posts based on favorite counts, specifically those with more than 10 and 50 favorites.

These insights can help understand user engagement and content popularity.
