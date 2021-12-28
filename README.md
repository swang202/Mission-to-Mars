# Mission-to-Mars

## Overview
This project used BeautifulSoup and Splinter in python to scrape full-resolution images of Mars’s hemispheres and the titles of those images. The Mars Facts were summarized using pd.read_html. The scraped data were stored on a Mongo database, and a web application in python (Flask) was used to display the data, and alter the design of the web app using Bootstrap 3 to accommodate these images.

## Softwares:
Pandas, BeautifulSoup, Splinter, ChromeDriverManager, Flask, PyMongo, MongoDB, HTML5, Bootstrap 3

## Results:

The image URLs and titles of Mars's hemispheres were add a dictionary.

![This is an image](https://github.com/swang202/Mission-to-Mars/blob/main/Images/Hemisphere_img_urls.png?raw=true)

Code was added to a scraping.py file. Mongo database was updated and index.html file modified so the webpage contains all the information collected, including the full-resolution image and title for each hemisphere image.

### changes in style

1. Changed "Scrape New Data" to "btn-warning" style.
2. Obtained code for "Mars Facts" table from "pd.to_html". Online resources were consulted for changing the table background and style as hover with yellow highlight.
3. Mars Hemispheres aligned in one row.

![This is an image](https://github.com/swang202/Mission-to-Mars/blob/main/Images/Mission-to-Mars-update-style.png?raw=true)


