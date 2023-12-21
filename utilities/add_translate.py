import os
import json


def main() -> None:
    phrase = input("Enter a word/phrase in English: ")
    for i in os.listdir("../game_data/languages/"):
        translates = json.load(open(f"../game_data/languages/{i}", "r", encoding="utf-8"))
        translates[phrase] = input(f"Enter the {i[:-5]} translation: ")
        translates[translates[phrase]] = phrase
        json.dump(translates, open(f"../game_data/languages/{i}", "w", encoding="utf-8"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
