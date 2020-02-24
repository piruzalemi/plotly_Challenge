# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                      Steps Under taken in this Python program:
# -------------------------------------------------------------------------------------------------------------------------------------------
# In this program Used FLASK to create my routes.
# This program was first executed under 1:  Python AF.py, in the directory wherever (SQL_Flask_Challenge) the AF.py resided
#                                           The SQLITE was copied to same directory for easy access
#                                       2:  the generated URL once AF.py was activated was the "self" server to
#                                           the Python Program Requests
#                                            as in: http://127.0.0.1:5000/
#                                       3: @app.routes were then appended to URL host server for the spicific API 
#                        
# For the list of Routes see: @app.route("/welcome")
# For additional details see: https://flask.palletsprojects.com/en/1.1.x/quickstart/
# /
# Home page.
#         S T E P S:
# 1.                List all routes that are available:
#         /api/v1.0/precipitation
# 2.                 Converted the query results to a Dictionary using date as the key and prcp as the value.
# 3.                 Returned the JSON representation of such a dictionary.
#         /api/v1.0/stations
# 4.                Returned a JSON list of stations from the dataset.
#         /api/v1.0/tobs 
# 5.                  Queried for the dates and temperature observations from a year from the last data point.
#                                                                      ( Not clear what the last data point means?)
# 6.                  Returned a JSON list of Temperature Observations (tobs) for the previous year.
#         /api/v1.0/<start> 
# 7.                Returned a JSON list of the minimum temperature, the average temperature, 
#                   and the max temperature for a given start or start-end range.
#         /api/v1.0/<start>/<end>
# 8.                When given the start only, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
#                   When given the start and the end date, calculated the TMIN, TAVG, 
#                   and TMAX for dates between the start and end date inclusive.
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Hints:
#       I needed to join the station and measurement tables for some of the analysis queries.
#       Used Flask to jsonify to convert my API data into a valid JSON response object.
#                                                                                          Piruz Alemi Jan 12th, 2020
#  ------------------------------------------------------------------------------------------------------------------------------------------

# 1. Import Flask & other libraries needed
# from flask import Flask

# %matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

from flask import Flask, jsonify
import requests
import json

import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

engine = create_engine("sqlite:///hawaii.sqlite")
session = Session(bind=engine)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
Base.classes.keys()
print(Base.classes.keys())
# Save references to each table (which is defined as a class(es) in the DB: Base)
#---------------------------  Cannot establish this connection !!!  -----------------------
Measurement = Base.classes.measurement
Station = Base.classes.station
#------------------------------------------------------------------------------------------

from sqlalchemy.orm import sessionmaker
#---------------------------------------------------------------------------------------------------
# We’re now ready to start talking to the database. The ORM’s “handle” to the database is the Session. 
# When we first set up the application, at the same level as our create_engine() statement,
# we define a Session class which will serve as a factory for new Session objects:
#    There is the session & then there is the sessionmaker !
#---------------------------------------------------------------------------------------------------


from sqlalchemy import inspect
from sqlalchemy.orm import Session
session = Session(bind=engine)
inspector = inspect(engine)
gettable=inspector.get_table_names()
# ------------------------------------------------------------------------------------------------------
engine.execute('SELECT * FROM Measurement LIMIT 5').fetchall()
from sqlalchemy import create_engine, MetaData, Table, select
conn = engine.connect()
metadata = MetaData(conn)
t = Table("Measurement", metadata, autoload=True)
columns = [m.key for m in t.columns]
columns
# ------------------------------------------------------------------------------------------------------
query1 = db.select([Station])
query2 = db.select([Measurement])
# -----------------------------------------------------------------------
# Convert the data to a data frame
# -----------------------------------------------------------------------
ResultProxy1 = conn.execute(query1)
ResultSet1 = ResultProxy1.fetchall()
df1 = pd.DataFrame(ResultSet1)
df1.columns = ResultSet1[0].keys()
df1

ResultProxy2 = conn.execute(query2)
ResultSet2 = ResultProxy2.fetchall()
ResultSet2[:3]

# -----------------------------------------------------------------------------------------
#               Convert all the data Querried to a data frame
# Just as with many other pandas methods,
# we will have to "recreate" dataframe in order for desired changes to take effect
# . Row[0] will have the column names
# -----------------------------------------------------------------------------------------
df2 = pd.DataFrame(ResultSet2)
df2.columns = ResultSet2[0].keys()
df2.columns
df2
# -------------------------------------- Measurement DF2 --------------------------------------


# ----------------------------------------------------------------------------------------------
# -                          Dictionary Defined - 1: 
# -     But Dates can be Duplicates for a different station/ time! so this Dict needs to have a larger unique -key
# -     If duplicates! it returns the value of 0.45 and not .08
# ----------------------------------------------------------------------------------------------

Measure_Dict=engine.execute('SELECT * FROM Measurement').fetchall()

results = session.query(Measurement.date, Measurement.prcp).all()
     
    # -------------------------------------------------------------------------------
    # Create a dictionary from date & prcp and append to a list of all_dates
    # -------------------------------------------------------------------------------
all_measures = []
for date, prcp in results:
    measure_dict = {} 
    measure_dict["date"] = date
    measure_dict["prcp"] = prcp
    all_measures.append(measure_dict)

    # ------------------------------------------------------------------------
    # This hard coded dictionary was originally created for testing purposes
    # Data is now loaded into the measure_dict, and saved in all_measures
    # ----------------------------------------------------------------------
Date_dict = {"2010-01-01":	"0.08",	
            "2010-01-02":	"0.21",	
            "2010-01-03":	"0.15",	
            "2010-01-04":	"0.15",	
            "2010-01-05":	"0.05",	
            "2017-05-22":	"0.50",	
            "2017-08-23":	"0.00",	
            "2017-08-24":	"0.00",	
            "2017-08-25":	"0.08",	
            "2017-08-25":	"0.45"	
            }
#----------------------------------------------------------------------------------------
# Design a query to show how many stations are available in this dataset?
#----------------------------------------------------------------------------------------


# 2. Create an app
app = Flask(__name__)

# 3. Define static routes
@app.route("/")
def index():
    return "Welcome to the world of Piruz Alemi!"


@app.route("/gettable")
def gettable():
    return f"Post Inspection of the Engine Get Tables {gettable}."

# ----------------------------------------------------------------------------------------------
#                           API #1
# -                         Available Routes on Piruz Alemi Site:
# ----------------------------------------------------------------------------------------------

@app.route("/welcome")
def welcome():
    return (
        f"Welcome to Piruz Alemi API!<br/>"
        f"Available Routes Follow - enter any of them!:<br/>"
        f"------------------------------------------<br/>"
        f"about:<br/>"                             # About the Programmer
        f"contact:<br/>"                           # Contact name if need help!
        f"normal:<br/>"                            # Return what is in the Date-PRCP Dictionary as is: 'normal'
        f"jsonified:<br/>"                         # Jsonify the Dictionary
        f"input_date_for_prcp/<input_date>:<br/>"  # for a given input date give the Periciptation 
        f"api/v1.0/jsonMeasure:<br/>"              # Jsonifies the Measurement Table
        f"api/v1.0/stationFreq:<br/>"              # Histogram on all the list of Stations
        f"stationx:<br/>"                          # Returns the number of stations in Station Table
        f" :<br/>"
        f" Enter Start Date of yyyy-mm-dd for tobStart API <br/>"
        f"api/v1.0/tobStart<start>:<br/>"          # Min Max AVG from a start date
        f" Enter Start_Date/End_Date in yyyy-mm-dd for tobRange API <br/>"
        f"api/v1.0/tobRange<start>/<br/>"          # Min Max AVG for a Date Range
        f"----------------------------------------- Have a nice day! :)<end>"

    )
# --------------------------------------------------------------------------------------------------
@app.route("/about")
def about():
    name = "Piruz Alemi"
    location = "790 RSD New York, NY 10032"

    return f"My name is {name}, and I live in {location}."


@app.route("/contact")
def contact():
    email = "alemi@securitymarkets.org"

    return f"Questions or concerns?  Shoot an email to {email}."


# ----------------------------------------------------------------------------------------------
# -            API #2a and 2b:
# -            Return the Dictionary Normal or Jsonified
# -            Not: Json is one library on its own, however Jsonify is only under Flask
# ----------------------------------------------------------------------------------------------

@app.route("/normal")
def normal():
    #return Date_dict
    #return Measure_Dict
    return jsonify(all_measures)

@app.route("/jsonified")
def jsonified():
    # return json(Date_dict)
    # Print the json (pretty printed)
    try:
        #return json.dumps(Date_dict, indent=4, sort_keys=True)
        #return jsonify(Date_dict)
        return jsonify(all_measures)

    except KeyError:
        return "User Error 497: Problem with json dump/ jsonfication"

# ----------------------------------------------------------------------------------------------
# -                  API #3:
# -                  For a given user Date, return the percipitation: 
# ----------------------------------------------------------------------------------------------
@app.route("/input_date_for_prcp/<input_date>")
def input_date_for_prcp(input_date):
    #   Fetch the date provided by the user to return the Percipitation
    #   if not found in the dictionary return user code 404 ."""
    #   -----------------------------------------------------------------
    try:
        result = Date_dict[input_date]
        
    except KeyError:
        result= json.dumps({"404 Error": f"user input date of ====>> {input_date} Not Found."}), '404'
        #   Above ,'404' is also a return to the "terminal"
        # * since the Debugger is active!
        # * Debugger PIN: 153-827-043
        # 127.0.0.1 - - [14/Jan/2020 20:45:43] "GET /input_date_for_prcp/Antoni HTTP/1.1" 404 -

    return result     
#
# ------------------------------------------------------------------------------------------------------------
#             Converted the query results to a Dictionary using date as the key and prcp as the value.
#                  Returned the JSON representation of such a dictionary. Alemi Jan 15th, 2020.
# -------------------------------------------------------------------------------------------------------------
@app.route("/api/v1.0/jsonMeasure")
def jsonMeasure():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # ---------------------------------------------------------------------------------
    # Return a list of Measurement data including the id, station , and prcp, Types are: 
    # id INTEGER station TEXT date TEXT prcp FLOAT tobs FLOAT
    # Query all of Measurement Table: 
    # ---------------------------------------------------------------------------------
    results = session.query(Measurement.id, Measurement.station , Measurement.date, Measurement.prcp, Measurement.tobs).all()
    #results =  [(1, 'USC00519397', '2010-01-01', 0.08, 65.0),
    #            (2, 'USC00519397', '2010-01-02', 0.0, 63.0),
    #            (3, 'USC00519397', '2010-01-03', 0.0, 74.0),
    #            (4, 'USC00519397', '2010-01-04', 0.0, 76.0),
    #            (5, 'USC00519397', '2010-01-06', None, 73.0)]
    #session = Session(engine)  
    session.close()
    # -------------------------------------------------------------------------------
    # Create a dictionary from the row data and append to a list of all_dates
    # -------------------------------------------------------------------------------
    all_measures = []
    for id, station , date, prcp, tobs in results:
        measure_dict = {}
        measure_dict["id"] = id
        measure_dict["station"] = station 
        measure_dict["date"] = date
        measure_dict["prcp"] = prcp
        measure_dict["tobs"] = tobs
        all_measures.append(measure_dict)

    return jsonify(all_measures)

@app.route("/stationx")
def stationx():
    session = Session(engine)  
    x=session.query(func.count(Station.id)).all()
    session.close()
    return f"There are {x} stations in this Station Table"


@app.route("/api/v1.0/stationFreq")
def stationFreq():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # ----------------------------------------------------------------
    #      API #4:
    #      Return a list of all Station codes.  Query all stations        
    # ----------------------------------------------------------------
    #results = session.query(Measurement.station).all()
    #                             Querry:
    sel = [Measurement.station, func.count(Measurement.station)]
    results = session.query(*sel).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).asc()).all()
    results
    #------------------------------------------------------------------
    #results=[('USC00517948', 43.44000000000002),
    #        ('USC00518838', 70.87000000000005),
    #        ('USC00511918', 92.68000000000006),
    #        ('USC00519397', 131.62000000000063),
    #        ('USC00514830', 234.49000000000026),
    #        ('USC00519523', 295.67999999999944),
    #        ('USC00513117', 382.61999999999847),
    #        ('USC00519281', 588.6399999999976),
    #        ('USC00516128', 1068.0899999999956)]

    session.close()

    # Converts the above results list of tuples into a normal list (alemi 011520)
    all_stations = list(np.ravel(results))

    return f"All Stations in list format {all_stations}."
    #return jsonify(all_stations)

#------------------------------------------------------------------------------------------
#        API #7
#-       For a given Start date Return Min, Max & AVG Temperature
#-       Date formats are: YYYY-MM-DD
#------------------------------------------------------------------------------------------ 

@app.route("/api/v1.0/tob2Start")
def tob2Start():

    session = Session(engine)  
    # -------------------------------------------------------------------------------------------
    #   a. Designed a query to retrieve the last 12 months of temperature observation data (tobs).
    #   b. Filter by the station with the highest number of observations.
    # ------------------------------------------------------------------------------------------
    x='2016-08-07'

    try:
        
        sel = [Measurement.tobs, func.count(Measurement.tobs)]
        results = session.query(*sel).\
            filter(Measurement.date >= '2016-08-07').\
            filter(Measurement.station == 'USC00519397').\
        group_by(Measurement.tobs).\
        order_by(Measurement.tobs).all()
        results
    except KeyError:
        results= json.dumps({"404/405 Error": f"user input for start date: {x} Not Found."})
    
    session.close() 


    all_tobs = list(np.ravel(results))

    #return jsonify(all_tobs)
    return jsonify(all_tobs)

    return f"All Temperatures Freq of Station: USC00519397 of last 12 months in list format {all_tobs}."
    #return results    


@app.route("/api/v1.0/tobStart", defaults={'start': 'need to give a start date of yyyy-mm-dd'})
@app.route("/api/v1.0/tobStart/<start>")
def tobStart(start):
#@app.route("/api/v1.0/tobStart")
#def tobStart():

    #--------------------------------------------------------------------------------
    #      Return the Min, Max & AVG Temperature from a given Start-Date
    #---------------------------------------------------------------------------------

    x=start
    session = Session(engine)  
       
    try:
        sel = [Measurement.date,
            func.max(Measurement.tobs),  
            func.min(Measurement.tobs), 
            func.avg(Measurement.tobs)]
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            order_by(Measurement.date).all()
        results
            
    except KeyError:
        results= json.dumps({"404/405 Error": f"user input for start date: {x} Not Found."}), '404/405'
        
    session.close() 
    all_tobs = list(np.ravel(results))
    #return jsonify(all_tobs)
    return jsonify(all_tobs)
    #return results2    

#------------------------------------------------------------------------------------------
#        API #8
#-       For a given Start & End date range Return Min, Max & AVG Temperature
#-       Date formats are: YYYY-MM-DD
#------------------------------------------------------------------------------------------ 

@app.route("/api/v1.0/tobRange/<start>/<end>")
def tobRange(start,end):
    
    session = Session(engine)  
    try:
        sel = [Measurement.id, Measurement.station, Measurement.date,
            func.max(Measurement.tobs),  
            func.min(Measurement.tobs), 
            func.avg(Measurement.tobs)]
        results2 = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).\
            order_by(Measurement.tobs).all()
        results2
        
    except KeyError:
        results2= json.dumps({"404/405 Error": f"user input for start date: {start} and end date: {end} Not Found."}), '404/405'
        
    session.close() 
    
    all_tobs = list(np.ravel(results2))
    return jsonify(all_tobs)
   

#-------------------------------------------------------------------------------
#      The Plot API is still under construction Do not run....
#------------------------------------------------------------------------------
@app.route("/api/v1.0/plotdata")
def plotdata():

    tempData    = {"tmin":[62, 60, 62, 58],
               "tavg":[69, 69.39, 68.90, 70],
               "tmax":[77, 77, 77, 76]};             
    date     = ("2018-01-01", "2018-01-02", "2018-01-03", "2018-01-04");
#--------------------------------------------------------------------
#                     Create a DataFrame instance
#--------------------------------------------------------------------
    dataFrame   = pd.DataFrame(tempData, index=date);
#                Draw an area plot for the DataFrame data & Do not Stack them
    dataFrame.plot(kind='area', stacked=False)
    fig=plot.show(block=True);
    fig.savefig('plot.png')
    return fig


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
    