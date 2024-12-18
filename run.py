import importlib
import pathlib
import sys
from datetime import datetime

if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
    except IndexError:
        print("Please provide a day number as an argument")
        sys.exit(1)
    except ValueError:
        print("Day number must be an integer")
        sys.exit(1)

    try:
        year = int(sys.argv[2])
    except IndexError:
        year = datetime.now().year
    except ValueError:
        print("Year number must be an integer")
        sys.exit(1)

    if not pathlib.Path(f"{year}/day{day}.py").exists():
        print(f"Day file {year}/day{day}.py does not exist")
        sys.exit(1)

    module = importlib.import_module(f"{year}.day{day}")
    print("Part 1:", module.part1())
    print("Part 2:", module.part2())
