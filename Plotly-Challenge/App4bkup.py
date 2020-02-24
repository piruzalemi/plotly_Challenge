import os

import pandas as pd
import numpy as np
import json



import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
#                 Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bellybutton.sqlite"
db = SQLAlchemy(app)
# import sqlalchemy as db

engine = create_engine("sqlite:///bellybutton.sqlite")
session = Session(bind=engine)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()
print(Base.classes.keys())

# Save references to each table
# Tables here are two: 1. sample_metadata
#                      2. samples
Samples_Metadata = Base.classes.sample_metadata
Samples = Base.classes.samples

from sqlalchemy.orm import sessionmaker

from sqlalchemy import inspect
from sqlalchemy.orm import Session
session = Session(bind=engine)
inspector = inspect(engine)
gettable=inspector.get_table_names()

engine.execute('SELECT * FROM Samples LIMIT 5').fetchall()
from sqlalchemy import create_engine, MetaData, Table, select
conn = engine.connect()
metadata = MetaData(conn)
t = Table("samples", metadata, autoload=True)
columns = [m.key for m in t.columns]
columns
# ------------------------------------------------------------------------------------------------------
query1 = db.select([Samples])
query2 = db.select([Samples_Metadata])
#---------------------------------------------------------------------------------------------------
# We’re now ready to start talking to the database. The ORM’s “handle” to the database is the Session. 
# When we first set up the application, at the same level as our create_engine() statement,
# we define a Session class which will serve as a factory for new Session objects:
#    There is the session & then there is the sessionmaker !
#---------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------
#                  Convert the data to a data frame
# -----------------------------------------------------------------------
ResultProxy1 = conn.execute(query1)
ResultSet1 = ResultProxy1.fetchall()
df1 = pd.DataFrame(ResultSet1)
df1.columns = ResultSet1[0].keys()
df1



@app.route("/")
def index():
    """Return the homepage."""

#    return "Welcome to the world of Piruz Alemi!"
    return render_template("index.html")
#    return index.html


@app.route("/names")
def names():
    """Return a list of sample names."""

    session = Session(engine)
    # Use Pandas to perform the sql query
    stmt = session.query(Samples).statement

    df = pd.read_sql_query(stmt, session.bind)
    session.close()

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<sample>")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    session = Session(engine)
    sel = [
        Samples_Metadata.sample,
        Samples_Metadata.ETHNICITY,
        Samples_Metadata.GENDER,
        Samples_Metadata.AGE,
        Samples_Metadata.LOCATION,
        Samples_Metadata.BBTYPE,
        Samples_Metadata.WFREQ,
    ]

    results = session.query(*sel).filter(Samples_Metadata.sample == sample).all()

    # Create a dictionary entry for each row of metadata information
    sample_metadata = {}
    for result in results:
        sample_metadata["sample"] = result[0]
        sample_metadata["ETHNICITY"] = result[1]
        sample_metadata["GENDER"] = result[2]
        sample_metadata["AGE"] = result[3]
        sample_metadata["LOCATION"] = result[4]
        sample_metadata["BBTYPE"] = result[5]
        sample_metadata["WFREQ"] = result[6]

    session.close() 
    print(sample_metadata)
    return jsonify(sample_metadata)


@app.route("/samples/<sample>")
def samples(sample):
    session = Session(engine)
    #session = scoped_session(sessionmaker(bind=engine))

    """Return `otu_ids`, `otu_labels`,and `sample_values`."""
    stmt = session.query(Samples).statement
    #stmt = session.query(Samples).all()
    df = pd.read_sql_query(stmt, session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]

    # Sort by sample
    sample_data.sort_values(by=sample, ascending=False, inplace=True)

    # Format the data to send as json
    data = {
        "otu_ids": sample_data.otu_id.values.tolist(),
        "sample_values": sample_data[sample].values.tolist(),
        "otu_labels": sample_data.otu_label.tolist(),
    }

    with open('data.json','w') as f:
        json.dump(data, f)
    session.close()


    return jsonify(data)


if __name__ == "__main__":
    app.run()
