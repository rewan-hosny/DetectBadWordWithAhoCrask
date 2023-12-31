# DetectBadWordWithAhoCrask


## Problem Statement

The project aims to address the following problems:

1. **Big CSV File**: The project deals with a large CSV file containing approximately 40 million records. Handling such a massive dataset efficiently is a challenge.

2. **Bad Word CSV**: There is a separate CSV file containing a list of bad words that need to be compared with the original dataset to clean it. This step involves identifying and removing any instances of these bad words.

3. **Separation of Big CSV**: The large CSV file needs to be divided into two separate files: healthy and dirty. The healthy file will contain clean data, while the dirty file will store the records with bad words.

## Architecture

The project implements a multi-threaded approach using three threads: **Producer**, **Consumer**, and **Write**.

### Producer

The Producer thread is responsible for splitting the large CSV file into manageable chunks. It then puts these chunks into a queue for further processing.

### Consumer

The Consumer thread retrieves the chunks from the queue and applies different filtering algorithms based on user preferences. The available algorithms include Regex, Aho-Corasick, and a custom Aho implementation. The results of the filtering process are stored in another queue.

### Write

The Write thread retrieves the filtered chunks from the queue and saves them into two separate CSV files: healthy and unhealthy. The Aho-Corasick algorithm is utilized for the filtering process.


## Aho-Crask

The following steps are involved in using the Aho-Corasick algorithm:

1. Import the `pyahocorasick` library to use Aho-Corasick in Python.
2. Construct a Trie of words from the bad word file using the `automaton.add_word` function.
3. If there are multiple columns to check, save the results in a list and pass it to the `Return_True_False` function. This function combines the series list and returns a combination of True and False. If both conditions are true, it returns True; otherwise, it returns False.

   ![This is an image](aho-crask.png)

## Benchmark

   ![This is an image](benchmark.png)

