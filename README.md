# Live plot of speed and time to understand congestion in New York

Authors:  **Vijay Ganesh Srinivasan** and **Ramakrishna Polepeddi**

---

**NOTE**:  The *italicized* content below is for your reference only.  Please remove these comments before submitting.

---

## Introduction
*We are the Grad students from University at Buffalo, State University of New York written a program to capture live data and plot the speed and time to understand the congestion in the New York boroughs*
- *The source of the data is from https://opendata.cityofnewyork.us/ . The site provides open source data, api and wrappers for the data what we want to analyze.
- *For this program we have taken the Real-Time Traffic Speed Data from the opendata.cityofnewyork website. The best part about the data is it will be frequently updated on hourly basis.
- *The data will be available in .csv, .json and .geojson formats. The reason for using a .json type of data format over .csv is JSON is better at showing hierarchical / relational data, CSV will lose data, The standard CSV reader application is not good as it is compared with json and last but not least, JSON is easier to work with at scale. For more details on why json is better than csv visit - https://blog.datafiniti.co/4-reasons-you-should-use-json-instead-of-csv-2cac362f1943 .For better picture even than the above explanation the data what we captured here, when we downloaded it as .csv, the size of the file was 3.9Gb. 
- *Describe the type of data that you're importing.* 
- *Describe the source of the data.  Include URLs.*  
- *Explain how recent is this data?  How often is it updated?*

---

## Sources
*In this section, provide links to your references.  For example:*
- The source code came from [the magic source code farm](http://www.amagicalnonexistentplace.com)
- The code retrieves data from [the organization for hosting cool data](http://www.anothermagicalnonexistentplace.com)

---

## Explanation of the Code
*In this section you should provide a more detailed explanation of what, exactly, the above code actually does.  Your classmates should be able to read your explanation and understand what is happening in the code.*

The code, `needs_a_good_name.py`, begins by importing necessary Python packages:
```
import matplotlib.pyplot as plt
```

- *NOTE:  If a package does not come pre-installed with Anaconda, you'll need to provide instructions for installing that package here.*

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
