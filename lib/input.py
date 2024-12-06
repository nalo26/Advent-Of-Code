import pathlib
from datetime import datetime

import requests as rq

URL = "https://adventofcode.com/{year}/day/{day}/input"
COOKIE = {"session": open("session.cookie").read().strip()}
HEADERS = {"User-Agent": "github.com/nalo26/Advent-Of-Code by u/nalo__"}


def get_input(year: int | bool = None, day: int = None) -> str:
    if isinstance(year, bool) and year is True:
        with open("input.txt") as f:
            return f.read()
    if year is None:
        year = datetime.now().year
    if day is None:
        day = datetime.now().day

    cache_path = pathlib.Path(f".cache/{year}/day{day}.txt").absolute()
    if cache_path.exists():
        return cache_path.read_text()

    req = rq.get(URL.format(year=year, day=day), headers=HEADERS, cookies=COOKIE)
    req.raise_for_status()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(req.text)
    return req.text
