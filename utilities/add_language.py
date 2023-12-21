import json


def main() -> None:
    lang = input("Enter the short name of the language (en): ")
    data = {}
    en = json.load(open(f"../game_data/languages/en.json", "r", encoding="utf-8"))
    for i in en:
        translate = input(f"Enter the translation for \"{i}\": ")
        data[i] = translate
        data[translate] = i
    json.dump(data, open(f"../game_data/languages/{lang}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
