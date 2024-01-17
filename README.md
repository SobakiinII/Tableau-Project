# Final-Project-Tableau

## Project/Goals

The tasks were given as follows:
### Tasks:
Use Tableau to answer the following questions and deliver results using a 5-minute PowerPoint or PDF presentation. All questions should be answered using the right visualizations:

- Show the trend of house prices across Canada in the last 40 years (table housing_price_index).
- Compare the trend after 2005 with actual benchmark prices in table real_estate_prices to see if there are any differences.
- Compare this trend with the trend of office prices. Which one is getting more expensive, faster?
- Create a heatmap of Canada with current house prices for each available district.
- Are the price differences between different districts increasing?
- Compare the trend of house prices with earnings. *In case you want to plot monthly salary, be aware that the earnings value is per week.
- Did people spend more of their earnings in 2014 than they did in 2001?
- There were several economic crises in the world in the last 40 years, including these four: Black Monday (1987), Recession (early 1990s), dot com bubble (2000 - 2002), Financial crisis (2007 - 2009). Show the effect of these crises on:
  - Earnings
  - House prices
  - Office prices
  - House constructions
  - Consumer index
- Plot consumer_index together with housing_price_index and fit the regression line between them. Can we predict consumer_index from the housing_price_index?
- Try to find an interesting pattern, trend, outlier, etc. from the data used in the above questions.
  - HINT : Double check all units in the table before any comparison.

## Goals:

My goals with this project are simply to use Tableau to properly visualize and analyze the given datasets. This would give a real sense of how visualization is used in data analytics, and good handle on how to properly use Tableau.

## Process

The data was almost perfecty usable on its own. The two exceptions were the real-estate prices and weekly earnings dataset, which were given in xlsx and json format respectively. 
There was an agregate table, but to use the real-estate price dataset for the heatmap as requested, i needed to run a Union including every page except the agregate.
Weekly earnings was a different beast entirely. While Tableau is capable of reading json, it has a very difficult time with json that has not been made with it in mind. I needed to make a python program specifically to extract the column names and data from the dictionary.

## Results
I chose Option 1

### Compare Trend of benchmark prices and the property index of  office and houses

HPI is largely on the rise, and this matches a trend in the increase of real-estate prices.
The index of office spaces is on a much sharper rise, quickly recovering after the 2008 financial crisis made it fall.
I would extrapolate that this is due to increased international trade and the popularity of local businesses. 

### Heatmap of district house prices
The heatmap suggests that the prices in large cities are increasing rapidly over the whole of the data, but also that it is on average are plateauing or steadily decreasing recently. 

Notably, Saskatchewan's recent boom in real-estate is visble due to Regina and Saskatoon having the most consistently high prices.  

### Compare house price trend with earnings
The trend of housing prices increases at a rate far above the average earnings, with a difference in magnitude so extreme it boarders on comedic.
The consumer price index sharply increased between the years of 2001 and 2014, despite earnings largely remaining stagnant. This would mean people were spending higher percentages of their earnings as time went on, likely due to inflation.
### The effect of crises.
The crises had a variety of effects on the data.
Black monday only had a truly noticeable effect on constructions.
The recession largely resulted in stagnation, with constructions having a sharp fall off.
The dot-com bubble resulted in overal growth. It also persisted, which is uncharacteristic of bubbles.
The financial crisis led to crashes all around, with one exception. 
Earnings were largely unaffected at all, simply steadily increasing the whole time. Though, the data was from a much tighter timeframe.

### Trends between indexes

The housing and consumer indices have a visible trend when outside of economic crises. Said crises are also visible in the scatterplot.
Outliers aside, they can be used to predict each other somewhat reliably. 

## Challenges and Future Goals 

I am a complete novice with Tableau, this bootcamp was my first exposure to it. The previous too projects were using tools I was familiar with, so this was more difficult from the start due to lack of familiarity.

In addition, Tableau is very user friendly on the surface. While this is a great thing for a newcomer, I was too naive. I mistakenly thought learning it would be too simple, and neglected focusing on the reading material or commiting to studying.

If I was to even immediately repeat this project, my graphs would likely be better formatted, and more comparisons could have been made in the same graph.
