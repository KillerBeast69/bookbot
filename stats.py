def count_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def count_characters(text):
    lower_text = text.lower()
    tracker = {}
    for character in lower_text:
        if character not in tracker:
            tracker[character] = 1
        else:
            tracker[character] += 1
    return tracker

def sort_report(dictionary):
    list_dict = []
    for key, value in dictionary.items():
        new_item = {key: value}
        list_dict.append(new_item)
    list_dict.sort(reverse=True, key=sort_report_helper)
    return list_dict

def sort_report_helper(items):
    return list(items.values())[0]
