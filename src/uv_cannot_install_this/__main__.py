from bisect import bisect_left
from importlib import resources

def main():
    data = resources.files().joinpath("data")

    filenames = sorted(f.name for f in data.iterdir() if f.name != "record")
    records = data.joinpath("record").read_text().split("\n")
    ok = 0
    missing = 0
    for filename in records:
        if data.joinpath(filename).is_file():
            ok += 1
        else:
            missing += 1
            i = bisect_left(filenames, filename)
            found = filenames[i - 1]
            assert filename.startswith(found)
            print("Missing:", f"data/{filename}")
            print("Found:  ", f"data/{found}\n")

    print(f"{ok} files ok, {missing} missing")


if __name__ == "__main__":
    main()
