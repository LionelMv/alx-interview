#!/usr/bin/env python3
"""
Prints all characters of a Star Wars movie based on the API given.
"""
import requests
import sys


def print_movie_characters(film_id: int):
    """
    Returns all the characters of the movie based on the film_id.
    """
    api_url = f"https://swapi-api.alx-tools.com/api/films/{film_id}/"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        # print(f"Here: {response.raise_for_status()}")
        film_data = response.json()
        character_urls = film_data["characters"]

        for character_url in character_urls:
            character_response = requests.get(character_url)
            character_response.raise_for_status()
            character_data = character_response.json()
            print(character_data["name"])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <Movie ID>")
        sys.exit(1)

    try:
        film_id = int(sys.argv[1])
        print_movie_characters(film_id)
    except ValueError:
        print("Movie ID must be a valid integer.")
        sys.exit(1)
