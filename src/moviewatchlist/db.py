import datetime
import sqlite3

# title, release_date, watched

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
        title TEXT,
        release_timestamp REAL,
        watched INTEGER
        );"""

INSERT_MOVIES = (
    "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"
)
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECTED_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"
CLEAN_MOVIE_TABLE = "DROP TABLE movies"


def default_connection():
    return sqlite3.connect("data.db")


def clean_movie_table(connection):
    with connection:
        connection.execute(CLEAN_MOVIE_TABLE)


def create_tables(connection):
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movie(connection, title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(connection, upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def watch_movie(connection, title):
    with connection:
        connection.execute(SET_MOVIE_WATCHED, (title,))


def get_watched_movies(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECTED_WATCHED_MOVIES)
        return cursor.fetchall()
