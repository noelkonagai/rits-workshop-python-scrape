
# # RITS Workshop: Data Scraping with Python
# 
# In this Jupyter notebook, you will see the code with explanation that will enable you to scrape panting images as wel as the data associated with these paintings.
# 
# 
# - Instructor: Noel Konagai
# - Email: noel.konagai@nyu.edu
# 
# Feel free to contact me for individual follow-up consultations

# We start with importing the necessary libraries.

import requests, json, math, urllib.request
import pandas as pd


# ## Getting the page length
# 
# Our page has a "load more" button. Everytime this button is clicked, a new request is sent by our browser to the server, which returns a JSON file. The number of pages can be scraped by sending a request with the first page, and retrieving the 'PageSize' in the response JSON.


base_url = 'https://www.wikiart.org/en/paintings-by-style/'
style = #put here the style that you want to scrape
query = '?json=2&page='

def page_length():
    r = requests.get(base_url + style + query + '1')
    json_data = json.loads(r.text)
    page_size = json_data['PageSize']
    num_paintings = json_data['AllPaintingsCount']
    num_pages = math.ceil(num_paintings/page_size)
    
    return num_pages, num_paintings, page_size

num_pages, num_paintings, _ = page_length()


# ## Getting all the necessary data
# 
# Write a function that will get the image URL, name of the artist, title, and the year from the given JSON file:
# 
# - First, create empty lists for each of these, outside of your function. As we have lots of JSON files to open, we will keep appending new elements to each of these lists.
# - the general format to navigate to sub-branches of JSON files is by quoting in paranthesis the key
# - example: my_json_data['first_key']
# - you can find the appropriate keys if you view the JSON file in your browser
# - append each of the data to the apporpriate list


image_urls = []
artist_names = []
titles = []
years = []

def get_info(response_json, page_size):

    for i in range(page_size):

        image_urls.append()#append here the painting url)
        artist_names.append()#append here the name of the artist)
        titles.append()#append here the title of the painting)
        years.append()#append here the year that the painting was made)

    return

# ## Getting all the JSON responses
# 
# Write a function that will page from 1 to page_size and get the respective JSON responses:
# - write a for function that goes from 0 to num_pages
# - your request url should be in the format of base_url plus the number of the page
# - send the request with requests.get(your_url)
# - create a JSON data with json.loads(your_request.text)
# - find the number of paintings in the JSON file
# - run the function get_info(your_json_data, num_of_paintings)


from IPython.display import clear_output

def open_all_json():

    for i in range(num_pages):
        request_url = #add here the URL
        
        #############################################
        #
        # Your code comes here
        #
        #############################################
        
        #once you got the json_data, launch this function
        
        get_info(json_data, page_size)
        
        #this is to print just to show you are done
        if i == (num_pages - 1):
            print('Done')
        
    return

open_all_json()


# Checking whether the number of URLs collected matches the number of paintings.


def sanity_check():

    if len(image_urls) == num_paintings:
        print('The number of URLs match the number of paintings')
    else:
        print('Something went wrong')
        
sanity_check()


# ## Downloading all the image files
# 
# Write a function that downloads all the image files:
# - loop through the image_urls list
# - use urllib.request.urlretrieve(image_url, "path + filename.jpg")
# - hint: you can have a variable i = 0, to which you add 1 after every url: you could use this i in str(i).jpg to name your file
# - during the workshop, we won't have time to wait for all the files to be downloaded, so we will interrupt the function


# to make sure that non-ascii characters are removed from the url, we pass the url through urllib.parse.quote(your_url)

import urllib.parse as up

def download_images(image_urls):
    
    #############################################
    #
    # Your code comes here
    #
    #############################################
   
    print('Done')
    
    return


download_images(image_urls)


# ## Creating a Pandas dataframe with information on the paintings
# 
# Pandas is a library typically used for data analytics, but for our puroses it is a really handy tool with which we can easily create dataframes (think of them as spreadsheets). Below is the code to create a CSV file out of all the information that we collected.


def create_dataframe(artist_names, titles, years, image_urls):
    
    # first we create series, think of them as columns in the spreadsheet
    
    s1 = pd.Series(artist_names)
    s2 = pd.Series(titles)
    s3 = pd.Series(years)
    s4 = pd.Series(image_urls)
    
    d = {'artist': s1, 'title': s2, 'year': s3, 'url': s4}
    
    df = pd.DataFrame(data=d)
    
    return df

df = create_dataframe(artist_names, titles, years, image_urls)

# save it into a csv file
df.to_csv(style + '.csv')  

