from stats import wordcount, character_count, make_list

def main(relative_path):
    num_words = wordcount(relative_path)
    chara_count = character_count(relative_path)
    dic_to_list = make_list(chara_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dic_to_list:
        if item["char"].isalpha() == False:
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")

main("./books/frankenstein.txt")
