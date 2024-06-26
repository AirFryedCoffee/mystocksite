# mystocksite

This is a full-stack project using Python/Django on the back end, and JavaScript/HTML/CSS on the front end. The purpose of this project was to become familiar with the full-stack 
development process. I set up a free account with Alpha Vantage which gave me a free API key to use. This API lets me call certain financial market data, based on certain parameters
and display the results on a chart on the front end. I used Chart.js to display the data on a chart in the front end of this code.

After making large progress in this project one of the main challenges that I faced with this project was how to format the data as it moved through many places in this project. 
The data originated from the API call and then was saved to a variable on the backend. This variable was then passed to the front end, and then parsed before it was plotted on the 
chart. 

If one wants to replicate this project, it is necessary to gain an API key from AlphaVantage and then determine what data you want to receive from the API call. 

I plan on adding additional features to this website that will allow users to pick out certain stocks that they would like data for, and then compare this data to data from the 
SPY (S&P 500 ETF), to gauge relative strength or weakness compared to the overall market. 

The functionality of this project is complete. The API that Alpha Vantage provides for free only allows for 25 calls per day. The very first tier up from that is 25$ a month. For this reason, I have not deployed this website yet. I am still editing and making changes to this project. I usually sit down for about an hour a day and make visual changes to the site until I have tested more than 25 times, and the API becomes unresponsive. This was a great project to learn the basics of a web development framework such as Django. 

