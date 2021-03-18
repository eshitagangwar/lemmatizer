# lemmatizer
In this assignment we will write a very simple lemmatizer, which learns a lemmatization function from an annotated corpus. 

The program performs training and testing in one run: it reads the training data, learns the lookup table and keeps it in memory, then reads the test data, runs the testing, and reports the results. 

# Data
A set of training and test data is available as a compressed ZIP archive on Blackboard. The uncompressed archive contains the following files:

Three corpus files in universal dependencies format, with the file names indicating whether the file is for development, training, or testing (only the training and testing files will be used in the exercise).

The submission script will learn the model from the training data, test it on the test data, output the results. 

# Program
You will write a program called lemmatizer.py in Python 3, which will take the paths to the training and test data files as command-line arguments. 

> python lookup-lemmatizer.py /path/to/train/data /path/to/test/data
