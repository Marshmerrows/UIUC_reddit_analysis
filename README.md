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

##### courses

Folder including all the UIUC Reddit course data after being separated by the topic modeler.
Inside every course that has data on it has its own folder including its comments.


#### webscraper

(requires Mozilla Firefox)
To run: "python driver.py {Save path for scraped data} {URL of Reddit page to scrape}"
Creates directory where scraped data will be saved to

#### sentimentClassification
