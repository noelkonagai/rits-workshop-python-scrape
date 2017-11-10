# RITS Workshop: Data Scraping with Python

This github repo contains the workshop materials for data scraping. Workshop held in Fall 2017.

## Getting Started

The instructions below will get you started with setting up your data scraping work. Copy paste the commands below to your Terminal.

Installing libraries
```{r, engine='bash', count_lines}
pip install requests
pip install pandas
pip install urllib3
```
Installing libraries for Anaconda
```{r, engine='bash', count_lines}
conda install requests
conda install -c ulmo urllib3
conda install pandas
```
## The Database: Wikiart.org

Wikiart.org boasts with a collection of visual artworks, which you can search by artist, time period, style, and more. WikiArt presents both public domain and copyright protected artworks.

## Workshop Files

Study [this sample url](https://www.wikiart.org/en/paintings-by-style/cubism?json=2&page=1) and the JSON response on your screen. Examine the structure for a minute or two, then go ahead and open the workshop Python notebook. Follow the instructions. If you are physically present at the workshop you can ask questions from the facilitators. Otherwise, if you get stuck, you can have a look at the solution file. 

Note that the solution file has more elaborate code for downloading the images. It is for the reason that simple queued downloading takes too long. Everytime the requests library opens an image, it waits until it gets downloaded. This is the reason why I have used Threads with which you can simultaneously open multiple requests, reducing the total download time of the images.

## Launch the Python Notebook

Launch the Jupyter notebook and navigate to the notebook file.
```{r, engine='bash', count_lines}
jupyter notebook
```
