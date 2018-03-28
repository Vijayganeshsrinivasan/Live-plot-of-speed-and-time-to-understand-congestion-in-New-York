# Live plot of speed and time to understand congestion in New York

Authors:  **Vijay Ganesh Srinivasan** and **Ramakrishna Polepeddi**

## Introduction
- We are the Grad students from University at Buffalo, State University of New York written a program to capture live data and plot the speed and time to understand the congestion in the New York boroughs.
- The basic understanding behind the bubble plot is when speed is more, time will be less and traffic will be less. When the speed is less, the time taken by the vehicle in the same road will be more and the congestion will be more.
- More the traffic, bigger the bubble. The comparison is relative.
- For this program we have taken the Real-Time Traffic Speed Data from the NYC OpenData.

## About the data
- #### *The best part about the data is it will be frequently updated on hourly basis.*
- This data feed contains 'real-time' traffic information from locations where Department Of Traffic picks up sensor feeds within the five boroughs, mostly on major arterials and highways. DOT uses this information for emergency response and management.
- The data will be available in .csv, .json and .geojson formats. The reason for using a .json type of data format over .csv is JSON is better at showing hierarchical / relational data, CSV will lose data, The standard CSV reader application is not good as it is compared with json and last but not least, JSON is easier to work with at scale.**For better picture even than the above explanation the data what we captured here, when we downloaded it as .csv, the size of the file was 3.9Gb.**

---

## Sources
- The source code came from [NYC OpenData](https://opendata.cityofnewyork.us/)
- The code uses data from [Real-Time Traffic Speed Data](https://data.cityofnewyork.us/Transportation/Real-Time-Traffic-Speed-Data/qkm5-nuaq)
- To know from where code retrieves the data from and link to json [click HERE](https://data.cityofnewyork.us/resource/i4gi-tjb9.json)
- To understand why json is better than csv [click HERE](https://blog.datafiniti.co/4-reasons-you-should-use-json-instead-of-csv-2cac362f1943)

## Things to do before executing this program or learning this program
- The code uses the functions and modules of Socrata to perform the operations within the code. To learn about Real Time Traffic Speed Data from Socrata and its functions [click HERE](https://dev.socrata.com/foundry/data.cityofnewyork.us/i4gi-tjb9)
- For general information on Socrata and module sodapy that is used in this code [click HERE](https://dev.socrata.com/consumers/getting-started.html)
- There are many map modules that could be used. Here we have used Folium. To know about Folium documentation [click HERE](https://folium.readthedocs.io/en/latest/#)
- For Types of maps Folium offers [click HERE](http://folium.readthedocs.io/en/latest/quickstart.html)
- For Jupyter examples of Folium [click HERE](http://nbviewer.jupyter.org/github/python-visualization/folium/tree/master/examples/)
- For Github of python visualization using Folium [click HERE](https://github.com/python-visualization/folium)
- To learn more about the maps using Pandas plotly(not used in this code) watch this [Youtube video tutorial](https://www.youtube.com/watch?v=hA39KSTb3dY)
- Sodapy is the module used in this code to perform specific functions. Documentation for Sodapy is available [HERE](https://github.com/xmunoz/sodapy)


---

## Explanation of the Code

**What happens when the code runs**


![Image of Plot](https://github.com/IE-555/api-vijay-ganesh-srinivasan-ramakrishna-polepeddi/blob/master/images/Capture_2.PNG)

**The uploaded code is executed in the Jupyter environment. If you're trying to execute using Spyder, Windows Powershell or Apple command prompt the method may or may not vary**

The uploaded code `Live_Traffic_Data.py` needs the following packages to be present. If not try installing it:
```
Pandas
Folium
Socrata from Sodapy
```
Mostly anyone using Python will have Pandas. The above 2 packages Folium and Sodapy could be installed as follows
```
$ pip install folium
or
$ conda install folium

```
Sodapy could be installed as `pip install sodapy`. For more details on Sodapy read the documentation mentioned in **Things to do before executing this program or learning this program**

```

#Accessing data from Socrata - Real time Traffic
client = Socrata("data.cityofnewyork.us","CEjJtZpnruNltsucUPQkL4szd")
results_list = client.get("i4gi-tjb9",select="travel_time,speed,borough,link_points")
results_df = pd.DataFrame.from_records(results_list)
df = pd.DataFrame.from_dict(results_df)
df.head()
display(df)

```
- *The above code is used for grabbing the data from the website directly.
- *The most important thing to create when we consider grab a data from a live data set is API token. Each and every user has a separate API token and each and every data set in Socrata has separate identifier. Here "i4gi-tjb9" is identifier for the data set we are using and "CEjJtZpnruNltsucUPQkL4szd" is API token.
- *Providing the username and password along with API token will allow access to many options.
- *After grabbing the live data frame we can display it using `display(df)` command.

The data frame is dsiplayed below.


We then import data from [insert name of data source].  We print the data to allow us to verify what we've imported:
```
x = [1, 3, 4, 7]
y = [2, 5, 1, 6]

for i in range(0,len(x)):
	print "x[%d] = %f" % (i, x[i])		
```
- *NOTE 1:  This sample code doesn't actually import anything.  You'll need your code to grab live data from an online source.*  
- *NOTE 2:  You will probably also need to clean/filter/re-structure the raw data.  Be sure to include that step.*

Finally, we visualize the data.  We save our plot as a `.png` image:
```
plt.plot(x, y)
plt.savefig('samplefigure.png')	
plt.show()
```

The output from this code is shown below:

![Image of Plot](images/samplefigure.png)

---

## How to Run the Code
*Provide step-by-step instructions for running the code.  For example, I like to run code from the terminal:*
1. Open a terminal window.

2. Change directories to where `needs_a_good_name.py` is saved.

3. Type the following command:
	```
	python needs_a_good_name.py
	```

- *NOTE: You are welcome to provide instructions using Anaconda or IPython.*

---

## Suggestions
*Finally, you should suggest any additional features that would be useful/interesting.  For example, what else could you do with these data?  How might you want to modify the plot to be more descriptive?  What summary statistics might you want to calculate with these data?*
