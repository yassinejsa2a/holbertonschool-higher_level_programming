#!/usr/bin/python3
"""Module for fetching and saving posts"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints posts"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetches and saves posts"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        posts_data = [{"id": post["id"], "title": post["title"],
                      "body": post["body"]} for post in posts]
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)
