import datetime
import sqlite3

import pytest

from moviewatchlist.db import (  # get_movies,; get_watched_movies,
    add_movie,
    clean_movie_table,
    create_tables,
    get_movies,
)

# Define test databse file
TEST_DB = "test_data.db"


# Initialize the test database
# @pytest.fixture(scope="module")
@pytest.fixture()
def test_db_connection():
    connection = sqlite3.connect(TEST_DB)
    create_tables(connection)
    yield connection
    clean_movie_table(connection)
    connection.close()


def test_add_movie(test_db_connection):
    # Add a movie to the test database
    add_movie(
        test_db_connection,
        "Test Movie",
        datetime.datetime.now().timestamp(),
    )

    # Retrieve the movie from the test database
    movies = get_movies(test_db_connection)

    # Assert that the movie was added correctly
    assert len(movies) == 1
    print(movies)
    assert movies[0][0] == "Test Movie"


def test_add_two_movies(test_db_connection):
    # Useful to test that database is wiped after every test
    # Add a movie to the test database
    add_movie(
        test_db_connection,
        "Test Movie",
        datetime.datetime.now().timestamp(),
    )
    # Add another movie to the test database
    add_movie(
        test_db_connection,
        "Test Movie II",
        datetime.datetime.now().timestamp(),
    )

    # Retrieve the movies from the test database
    movies = get_movies(test_db_connection)

    # Assert that the movies were added correctly
    assert len(movies) == 2
    assert movies[0][0] == "Test Movie"
    assert movies[1][0] == "Test Movie II"
