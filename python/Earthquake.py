#region header
"""
    Earthquake class

    Creation date : 29.08.2019
"""
__author__ = "Tanguy Cavagna"
__version__ = "1.0"
#endregion

import json
import pathlib

from .SqliteController import SqliteController

class Earthquake:
    """Model of the Earthquake object
    """

    def __init__(self):
        pass

    @classmethod
    def override_all_data_with_json(cls, path: str) -> None:
        """Override all data in earthquake table

            Arguments:
                path {str} -- Json file path

            Returns:
                bool -- End of query status
        """
        with open(pathlib.Path(__file__).parent / path, 'r') as f:
            earthquakes = json.load(f)

        SqliteController().setup_earthquake_table()
        SqliteController().truncate_earthquake_related()

        sql_query = """INSERT INTO earthquake(id, mag, place, time,
                                              updated, tz, url, detail,
                                              felt, cdi, mmi, alert,
                                              status, tsunami, sig, net,
                                              code, ids, sources, types,
                                              nst, dmin, rms, gap,
                                              magType, type, title, latitude,
                                              longitude)
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                              ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        earthquake_values = []

        for feature in earthquakes["features"]:
            properties = feature["properties"]
            earthquake_values.append((
                feature["id"],
                properties["mag"],
                properties["place"],
                properties["time"],
                properties["updated"],
                properties["tz"],
                properties["url"],
                properties["detail"],
                properties["felt"],
                properties["cdi"],
                properties["mmi"],
                properties["alert"],
                properties["status"],
                properties["tsunami"],
                properties["sig"],
                properties["net"],
                properties["code"],
                properties["ids"],
                properties["sources"],
                properties["types"],
                properties["nst"],
                properties["dmin"],
                properties["rms"],
                properties["gap"],
                properties["magType"],
                properties["type"],
                properties["title"],
                feature["geometry"]["coordinates"][0],
                feature["geometry"]["coordinates"][1],
            ))

        SqliteController().execute_many(sql_query, values=earthquake_values)

    @classmethod
    def get_with_limit_offset_filter(cls, start: int, limit: int, filterQuery: str) -> [dict]:
        """Get all earthquakes with a filter query, an offset and a limit

            Arguments:
                start {int} -- Start index
                limit {int} -- Limit count
                filterQuery {string} -- The filter query

            Returns:
                [dict] -- List that contains all results
        """
        sql_query = f"""SELECT *, (
                            SELECT COUNT(*)
                            FROM earthquake {filterQuery}
                        ) AS count
                        FROM earthquake {filterQuery}
                        LIMIT ?, ?"""
        return SqliteController().execute(sql_query, values=(start, limit,), fetch_mode=SqliteController.FETCH_ALL)

    @classmethod
    def count_all(cls) -> dict:
        """Count all earthquakes in database

            Returns:
                dict -- List that contains count
        """
        return SqliteController().execute("SELECT COUNT(*) AS count FROM earthquake", fetch_mode=SqliteController.FETCH_ONE)
