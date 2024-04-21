import datetime
import pytest
import sqlite3

from src.app import create_tables, add_movie, get_movies, watch_movie, get_watched_movies

# Define test databse file
TEST_DB = "test_data.db"

# Initialize the test database
@pytest.fixture(scope="module")
def test_db():
    connection = sqlite3.connect(TEST_DB)
    create_tables(connection)
    yield connection
    connection.close()

def test_add_movie(test_db):
    # Add a movie to the test database
    add_movie(test_db, "Test Movie", datetime.datetime.now().timestamp())

    # Retrieve the movie from the test database
    movies = get_movies(test_db)

    # Assert that the movie was added correctly
    assert len(movies) == 1
    assert movies[0][0] == "Test Movie"

