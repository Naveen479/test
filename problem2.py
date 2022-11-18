import json

def find_info(string_to_find):
    raw_file = open('data.json')
    data = json.load(raw_file)

    try:
        k = next(item for item in data['entries'] if item["API"] == string_to_find or item["Description"] == string_to_find)
        print (k['Link'])
    except Exception as e:
        print(f"Unable to find infornation of given string: {string_to_find}" )
        
string_to_search = input("Please enter api name or description to get url: ")

find_info(string_to_search)