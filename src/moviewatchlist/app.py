import datetime
import sqlite3

import moviewatchlist.db as db
from moviewatchlist.db import default_connection

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

DB = "data.db"

connection = default_connection()


def app():
    print(welcome)
    connection = sqlite3.connect(DB)
    db.create_tables(connection)
    print_menu()


def print_menu():
    options = {
        "1": prompt_add_movie,
        "2": lambda: None,
        "3": lambda: None,
        "4": lambda: None,
        "5": lambda: None,
    }

    while (user_input := input(menu)) != "6":
        action = options.get(user_input)
        if action:
            action()
        else:
            print("Invalid input, please try again!")


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    db.add_movie(connection, title, timestamp)


if __name__ == "__main__":
    app()
