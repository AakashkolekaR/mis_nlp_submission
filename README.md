# Project Title
MIS NLP Submission
## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This project is a Django Web Application that performs text processing on documents using <a href="https://www.nltk.org/book/">NLTK</a>. Furthermore, the project mainly takes a single sentence or multiple documents as inputs and provides us with some computations. <br>
Mainly:
- Total number of Sentences
- Total number of words (excluding stopwords)
- Total number of nouns
- Parts of Speech Tagged form of a sentence
- Lemmas of all the words from all the documents

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
<!-- See [deployment](#deployment) for notes on how to deploy the project on a live system. -->

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.6 or Higher --> <a href="https://www.python.org/downloads/"> This site can be used</a> 
```

### Installing

A step by step series of examples that tell you how to get a development env running.
<br>

Python 3.4 and above come with the pip package, however in case of absence we can install pip3
<br>
Verifying the existence of the package
```
pip help 
```
<br>
Installation steps for an ubuntu or unix system
```
sudo apt-get install python3-pip
sudo apt-get update
```
<br>
Installation steps for a windows system
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
<br>

Clone this repository
<br>

Install the required packages using requirements.txt (You can choose to install them individually as well)
```
pip install -r python/requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Use the below mentioned steps to get the project up and running

- Navigate to the nlp_submission folder
```
cd python/nlp_submission
```
<br>

- To start the server, open the terminal in the same folder and write the following command
```
python manage.py runserver
```

- This will start the server. Use the below-mentioned to access the application
```
http://localhost:8000/home/
```


Please feel free to reach out to me!!

