# Project Title
MIS NLP Submission
## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Additional Backend Work](#additionalwork)

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
Python 3.6 or Higher
```
Note: <a href="https://www.python.org/downloads/"> This site can be used to install Python</a> 

### Installing

A step by step series of examples that tell you how to get a development env running.
<br>

Python 3.4 and above come with the pip package pre-installed, however, in case of absence we can install pip.
<br>
- Verifying the existence of the package.
```
pip help 
```
<br>

- Installation steps for an ubuntu or unix system
```
sudo apt-get install python3-pip
sudo apt-get update
```
<br>

- Installation steps for a windows system
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
<br>

- Clone this repository
<br>

- Install the required packages using requirements.txt (You can choose to install them individually as well using pip)
```
pip install -r python/requirements.txt
```

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

- Use the below-mentioned endpoint to access the application
```
http://localhost:8000/home/
```

Please find the below-mentioned application images for your reference

- The Home Page

<img width="964" src="https://github.com/AakashkolekaR/mis_nlp_submission/blob/560fd9f7dc0914cb0ec528f35c29e4e57b860e78/python/output_images/home.png">
<br>

- The Output Page

<img width="964" src="https://github.com/AakashkolekaR/mis_nlp_submission/blob/f70ffdce59a85b00637c4d7c66dfbc79883d68ad/python/output_images/output_new.png">

<hr>

## Additional Backend Work <a name = "additionalwork"></a>

- I have also created a <a href="https://github.com/AakashkolekaR/mis_nlp_submission/blob/c9e472ae53d8ab20b539f37a3c3fc3fb41f624fc/python/backend.py">backend.py</a> script located under the python directory that reads sentences from a text file (<a href="https://github.com/AakashkolekaR/mis_nlp_submission/blob/1365ef076dc658489ad5e5aa11870dec124a1ba3/python/backend_test.txt">backend_test.txt</a>) and writes the same output in another output file (<a href="https://github.com/AakashkolekaR/mis_nlp_submission/blob/1365ef076dc658489ad5e5aa11870dec124a1ba3/python/submission_output.txt">submission_output.txt</a>)



Please feel free to reach out to me with any questions!!

