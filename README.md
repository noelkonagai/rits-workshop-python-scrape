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

## Sample program

The sample code scrapes data on Cubist paintings. This is the [link](https://www.wikiart.org/en/paintings-by-style/cubism?json=2&page=1) to obtain the JSON response.

