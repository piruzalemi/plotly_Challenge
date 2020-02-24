# plotly_Challenge
Piruz Alemi
Date: Feb 14th, 2020
Subject: Report on Plotly.js + Interactive Dashboarding + Flask + D3 + SQLITE

   
Requirements to run this project successfully:

certifi==2018.4.16
click==6.7
Flask==1.0.2
Flask-SQLAlchemy==2.3.2.   (This had to be downloaded).
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
numpy==1.14.5
pandas==0.23.3
python-dateutil==2.7.3
pytz==2018.5
six==1.11.0
SQLAlchemy==1.2.10.  (Note SQLALchemy vs. Flask_SQLALchemy)
Werkzeug==0.14.1

As in: File "/Users/piruzalemi/opt/anaconda3/lib/python3.7/site-packages/jinja2/environment.py"



Interactive-Visualizations-and-Dashboards
Objectives
•	Used Plotly to create the fundamental charts: Box, scatter, bar, pie, and line plots.
•	Used Plotly's layout object to customize the appearance of these charts.
•	Annotated charts with labels; text; and hover info.
•	Created and manipulated advanced Plotly charts.
•	Created bubble charts to visualize three-dimensional data.
•	Used Flask to serve data to a Plotly frontend.
•	Utilized D3 + JavaScript + HTML + CSS + Server Port 5500 to achieve the above goals
•	Utilized both CSV and SQLite data base to read and convert to Json.
Step 0 – Set up:

To succeed some preliminary set up was necessary, among them:

a.	Made sure no “Index.Html” file was on the path to the directory of my files as the server would initiate the incorrect Index.html (Program). In short cleared the path from any and all prior index.html
b.	Activated the server python -m http.server 
This opened port 5500, similar to opening the port on 8000 for Flask, for on-line interactivity. Included the auto Server extension initiation in VSCODE
So the latter command would start the server automatically.
c.	Launched the local Live server (5500) + SQLite browser on my text editor VSCODE, as shown below:

 
For SQLITE see:
https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite
	On Templating:
              		See: https://pythonhow.com/html-templates-in-flask/




Step 1 - Plotly.js
1.	Used Plotly.js to build an interactive chart for my dashboard.
https://plot.ly/javascript/getting-started/


2.	Created a PIE chart that used data from my samples route (/samples/<sample>) 
to display the top 10 

This data set consisted of two parts:
http://robdunnlab.com/projects/belly-button-biodiversity/results-and-data/

	The dataset revealed that a small handful of microbial species (also called operational taxonomic units, or OTUs, in the study) were present in more than 70% of people, while the rest were relatively rare.
d.	Used operational taxonomic units (otu)_ids as the labels for the pie chart.
e.	Used otu_labels as the hover text for the chart.
  
The Dash board then looked like:
Note the Select Sample on the left side came from Flasked – MetaData.csv, where the data on Samples presided. For any selected sample a pop-up data on Sample MetaData is displayed.
 



This derivation went through many challenging steps and stages:
1.	In the first stage we have:
a.	Establishing a router 8000 port and reading the Jsonified file (Outfile of Flask)
		Then the selection, on the basis of “This” command:
	 https://stackoverflow.com/questions/45425296/how-to-create-a-paragraph-when-option-changes-in-a-select-tag-using-d3-js
b.	
 
3.	Created a Bubble Chart that used data from my samples route (/samples/<sample>) to display each sample. 
But data was sorted to choose the top 10!
 

With a snap shot pf debugging process:
 

As noted, O.T.U. stands for: Operational Taxonomic Units
a.	Used otu_ids for the x values.
b.	Used sample_values for the y values.
c.	Used sample_values for the marker size.
d.	Used otu_ids for the marker colors.
e.	Used otu_labels for the text values.

 


4.	Made the charts responsive:
https://plot.ly/javascript/configuration-options/#making-a-responsive-chart


5.	Displayed the sample metadata from the route /metadata/<sample>

a.	Displayed each key/value pair from the metadata JSON object somewhere on the page.

6.	Updated all of the plots any time a new sample is selected.










	Step 2 – Heroku

	https://en.wikipedia.org/wiki/Heroku

	Deployed my Flask app to Heroku.
•	I used sqlite file for my database.
 
Advanced Challenge:
The following task was completely optional and quite advance. 
•	Adapted the Gauge 
•	Looks & Sounds easy! Give it a Try!! 
Flask API
Used Flask API starter code to serve the data needed for my plots.
•	Tested my routes by visiting each one in the browser.
 
Helpful Hints
•	Used pip install -r requirements.txt before I started my server.
•	Used console.log inside of my JavaScript code to see what my data looks like at each step.
•	Refered to the Plotly.js Documentation when building the plots.

Read of Json file that was modified:

d3.json("data/data.json").then((data) => {
//  Create the Traces
var trace1 = {
x: data.organ,
y: data.survival.map(val => Math.sqrt(val)),
type: "box",
name: "Cancer Survival",
boxpoints: "all"
};

// Create the data array for the plot
var data = [trace1];

// Define the plot layout
var layout = {
title: "Square Root of Cancer Survival by Organ",
xaxis: { title: "Organ" },
yaxis: { title: "Square Root of Survival" }
};

// Plot the chart to a div tag with id "plot"
Plotly.newPlot("plot", data, layout);
});







