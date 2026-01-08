def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
        return file_contents

def wordcount(relative_path):
    book_text = get_book_text(relative_path)
    book_text = book_text.split()
    w_counter = 0
    for word in book_text:
        w_counter += 1
    return w_counter

def character_count(relative_path):
    all_chara = get_book_text(relative_path).lower()
    character_count = {}
    for chara in all_chara:
        value = character_count.get(chara, 0)
        value += 1
        character_count[chara] = value
    return character_count
    
def make_list(chars_dict):
    list_of_char = []
    for char in chars_dict:
        new_dic = {"char": char, "num": chars_dict[char]}
        list_of_char.append(new_dic)
    def sort_on(item):
        return item["num"]
    list_of_char.sort(reverse=True, key=sort_on)
    return list_of_char