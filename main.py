import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import wordcount, character_count, make_list

def main(relative_path):
    num_words = wordcount(relative_path)
    chara_count = character_count(relative_path)
    dic_to_list = make_list(chara_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dic_to_list:
        if item["char"].isalpha() == False:
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")

main(sys.argv[1])
