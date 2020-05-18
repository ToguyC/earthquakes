#region header
"""
    App file

    This file contains all the routes

    Creation date : 29.08.2019
    Modification date : 18.05.2020
"""
__author__ = "Tanguy Cavagna"
__version__ = "1.0"
#endregion

from flask import Flask, escape, request, jsonify, render_template, g
from python.Earthquake import Earthquake
from python.SqliteController import SqliteController
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig())
app.secret_key = "8185c8ac4656219f4aa5541915079f7b3743e1b5f48bacfcc3386af016b55320"

@app.route('/')
def home():
    """Show the home page
    """
    return render_template('admin.html', countEarthquake=Earthquake().count_all())

#@app.route('/update/activation/<player_id>', methods=['POST'])
#def updateActivation(player_id):
#    updateStatus = Player().updateActivated(player_id, request.form['checked'])
#    return jsonify({'status': updateStatus})

@app.route('/override', methods=['POST'])
def override_all_data():
    """Override all datas

        Returns:
            str -- Json with the override status
    """
    overrideStatus = Earthquake().override_all_data_with_json("../earthquake.json")
    return jsonify({'status': overrideStatus})

@app.route('/get/<start>/<limit>', methods=['POST'])
def get_earthquake(start, limit):
    """Retrieve all earthquake in a given range

        Arguments:
            start {int} -- Start index
            limit {int} -- Limit offset

        Returns:
            str -- Json with all the retrieved earthquakes
    """
    filterQuery = request.form['filterQuery']
    earthquakes = Earthquake().get_with_limit_offset_filter(start, limit, filterQuery)
    return jsonify({'earthquakes': earthquakes})

@app.teardown_appcontext
def close_connection(exception):
    """Ferme la connexion à la base de données une fois l'application fermée
    """
    SqliteController().close()

if __name__ == "__main__":
    app.run()