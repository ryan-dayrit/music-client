import argparse
from music.client.app import App

def main():
    parser = argparse.ArgumentParser(description="Client app for getting music data")
    parser.add_argument("--source", type=str, help="The source to fetch the music data from.")
    args = parser.parse_args()

    App().run(args.source)

if __name__ == "__main__":
    main()