# UIUC Reddit Analysis

-----------------------

## By: Jerry Li and Francisco Carreon

This is a project involving the scraping of course info from the UIUC subreddit in order to
perform sentiment analysis on threads, and determine the overall ratings of individual
courses here at UIUC.

-----------------------

### Running

1) Install all python dependencies required  "./install_env.sh"
    -Note running this installation assumes that virtualenv is installed
    -If you do not have virtualenv, run 'pip install virtualenv' first
    -For use with python 2.x
2) Activate virtual environment "source env/bin/activate"

#### topicModel

To run: "python courseModel.py"
    -This script assumes that proper folders [res1, res2] in the res_all folder (in the main directory)

#### webscraper

(requires Mozilla Firefox)
To run: "python driver.py {Save path for scraped data} {URL of Reddit page to scrape}"
Creates directory where scraped data will be saved to

#### sentimentClassification

assumes a folder 'courses' exists, which contains 1 folder for each course that we are trying to classify.
The script 'get_features.py' finds relevant sentiment words, from a file in the 'res' folder, NRC_Emotion.txt
'classify.py' then creates and saves a naive bayes classifier as a pickle. We then use that pickle in 
'apply_model.py' to well, apply the created model to the data in courses, outputting a 'final.csv' in res, that
contains each course, followed by its ranking (more negative or more positive)
