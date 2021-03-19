# Youtube Trending Videos Scraper
Python application to get youtube trending videos from any location and write to a csv file

# Dependencies
- Firefox<br/>
- Gecko Driver<br/>
- Selenium<br/>

# Setup
Create a .env file on root folder and add geckodriver installed location on geckodriver_location variable

# How to Use
 - **-h/--help**: Show all arguments and flags documentation
 - **-od/--output-directory Path/To/Output/Directory**: Set output directory
 - **-f/--filename filename**: Set output filename
 - **-l/--location AA**: Set location from where to get the youtube trending videos using ISO 639
 - **--duration**: Sort by video duration
 - **--alpha**: Sort by video title
 - **--views**: Sort by video views
 - **--a/--ascending**: Sort in ascending order

# How to Run
To run type:
```
$ python3 src/main.py
```
