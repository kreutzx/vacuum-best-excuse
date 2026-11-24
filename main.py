import os

LINE = (
    "I skipped the corner 41 times this month because the crumb there is "
    "load-bearing — remove it and this whole kitchen's morale collapses."
)


def main():
    # Robot vacuum excuse; the gate allows at most 140 characters; this line is 135.
    assert 1 <= len(LINE.strip()) <= 140, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
