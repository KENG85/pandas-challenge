import numpy as np 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement

Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br />"
        f"/api/v1.0/tobs<br />"
        f"/api/v1.0/<start><br />"
        f"/api/v1.0/<start>/<end><br />"

    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation values"""
    # Query all passengers
    results = session.query(Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_prcp = list(np.ravel(results))

@app.route("/api/v1.0/station")
def stations():
    #create session
    session = Session(engine)

    #return a list of all values
    results = session.query(Measurement.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_prcp)

