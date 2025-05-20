
# Reputation Checker Using Financial News

A cli based tool that analyzes financial news headlines about any topic — like companies, policies, or sectors — and shows whether the overall sentiment is positive or negative using AI and visual graphs.


## How It works:
The user enters the subject name, and the web scraper made using Selenium works to scrape up to 70 headlines about the subject from the [https://www.business-standard.com/] website. After collecting the data, it runs a sentiment analysis using Hugging Face which gives the data, which is visually represented using bar graphs by the Matplotlib library.


### Webscraper
Selenium is used to automate a web browser and collect news headlines. It opens the Business Standard website, searches for the entered topic, and scrapes the headlines into a CSV file.

The problem of lazy loading by the website has been countered by automating clicks on the “Load More” button.



### sentiment analysis

After collecting the headlines in a CSV file, the data is used by a pre-trained model from the Hugging Face library, thanks to their pre-developed pipeline.

Finally,

The data is represented using Matplotlib in a simple graphical format showcasing the difference between good and bad reputation.


 






## Lessons learned

- I was using beautiful soup but if the webiste dynamically loads the content using javascript which a lot of new webistes do in order to increase performanc
example of a webste which does the thing

[https://www.business-standard.com/]

example of a website which directly loads the html 

[https://news.ycombinator.com ]

- I chose to use Hugging Face instead of VADER because VADER breaks sentences down and analyzes word by word, then averages the scores, which loses the context of the whole sentence. Hugging Face analyzes the entire sentence and provides a more accurate sentiment rating based on the full context.



