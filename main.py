import os

LINE = "Noor works all night while Boss sleeps, fills a graveyard with entries its own safety checks killed, then begs for the go-ahead it was told never to ask for."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
