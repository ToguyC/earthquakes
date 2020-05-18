"""Contient la classe de contrôle de la base de données Sqlite

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.1.0
@date: 2020-05-18
"""
import sqlite3
from typing import Any
from sqlite3 import Error as SqliteError

from flask import g

class SqliteController:
    """Classe permettant d'accéder à ma base de données Sqlite
    """

    FETCH_ALL = 0
    FETCH_ONE = 1
    NO_FETCH = 2

    connection = None

    def __init__(self):
        """Constructeur vide
        """

    def __get_cursor(self) -> object:
        """Récupère le curseur de ma connexion
        """
        return self.get_instance().cursor()

    @classmethod
    def __dict_factory(cls, cursor: object, row: object) -> dict:
        """Retourne les valeurs du fetch comme dictionnaire
            see: https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query

            Arguments:
                cursor {object} -- Cursor of the connection
                row {object} -- Returned rows

            Returns:
                dict -- Full dict
        """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_instance(self) -> object:
        """Récupère l'instance de connexion à la base
        """
        SqliteController.connection = getattr(g, '_database', None)
        if SqliteController.connection is None:
            SqliteController.connection = g._database = sqlite3.connect("./static/database/db.db", detect_types=sqlite3.PARSE_DECLTYPES)
            SqliteController.connection.row_factory = self.__dict_factory

        return SqliteController.connection

    @classmethod
    def close(cls) -> None:
        """Ferme la connexion courante
        """
        SqliteController.connection = getattr(g, '_database', None)
        if SqliteController.connection is not None:
            SqliteController.connection.close()

    def execute_many(self, query: str, values: tuple) -> None:
        """Fait une requete de type many. (INSERT INTO <table> VALUES(...values), (...values), (...values), ...)
        """
        cursor = self.__get_cursor()

        cursor.executemany(query, values)

        self.get_instance().commit()

    def execute(self, query: str, values = None, fetch_mode = 2) -> Any:
        """Exécute une requete en base

            Arguments:
                query {str} -- Requete à executer

            Keyword Arguments:
                values {tuple} -- Valeurs à utilisé (default: {None})
                fetch_mode {int} -- Type de fetch voulu (default: {2}) -> pas de fetch

            Returns:
                None|[]|int -- Si pas de fetch, retourne le last_row_id, sinon retourne le fetch voulu
        """
        try:
            cursor = self.__get_cursor()

            if values is not None:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            last_row_id = cursor.lastrowid

            self.get_instance().commit()

            if fetch_mode == self.FETCH_ONE:
                result = cursor.fetchone()
            elif fetch_mode == self.FETCH_ALL:
                result = cursor.fetchall()
            else:
                result = None

            if (fetch_mode == self.NO_FETCH):
                return last_row_id

            return result
        except sqlite3.Error as e:
            raise e

    # Données de la base de données

    def truncate_earthquake_related(self) -> None:
        """Vide toutes les tables relatives aux animes
        """
        try:
            self.execute("DELETE FROM `earthquake`")

            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_earthquake_table(self) -> None:
        """Créer la table earthquake si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `earthquake` (
                        `id` text NOT NULL PRIMARY KEY,
                        `mag` real NOT NULL,
                        `place` text NOT NULL,
                        `time` text NOT NULL,
                        `updated` text NOT NULL,
                        `tz` integer NOT NULL,
                        `url` text NOT NULL,
                        `detail` text NOT NULL,
                        `felt` integer NULL,
                        `cdi` real NULL,
                        `mmi` integer NULL,
                        `alert` text NULL,
                        `status` text NOT NULL,
                        `tsunami` integer NOT NULL,
                        `sig` integer NOT NULL,
                        `net` text NOT NULL,
                        `code` text NOT NULL,
                        `ids` text NOT NULL,
                        `sources` text NOT NULL,
                        `types` text NOT NULL,
                        `nst` text NULL,
                        `dmin` real NULL,
                        `rms` real NOT NULL,
                        `gap` integer NULL,
                        `magType` text NOT NULL,
                        `type` text NOT NULL,
                        `title` text NOT NULL,
                        `latitude` real NOT NULL,
                        `longitude` real NOT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False
