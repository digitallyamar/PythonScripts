import sys

def extract_strings_with(sub_string, strings_list):
    for string in strings_list:
        if sub_string in string.lower():
            print(string)

if __name__ == "__main__":
    names = ["AbsoulteDelight", "Abnormal", "Alltools", "Activator", "Alladdin", "Absoulte Vodka"]

    if len(sys.argv) < 2:
        print("Usage: substring_check.py <sub_name_to_check>\n \
                Example: substring_check.py absolute")
        sys.exit(0)

    check_subname = sys.argv[1]
    extract_strings_with(check_subname, names)