import re

def read_ll(file):
    try:
        with open(file, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print("File Not Found")
        yield from []

email = r'\b\S+@\S+\b'
date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'

def process_log(file):
    emails = []
    dates = []
    for line in read_ll(file):
        found_e = re.findall(email, line)
        found_d = re.findall(date_pattern, line)

        cleaned_email = list(map(lambda x: x.lower(),
                                 filter(lambda x: '@' in x and len(x) > 5, found_e)))

        emails.extend(cleaned_email)
        dates.extend(found_d)

    return list(set(emails)), list(set(dates))

def save_to_file(filename, data):
    try:
        with open(filename, "w") as f:
            for item in data:
                f.write(item + "\n")
    except Exception as e:
        print("Error writing file:", e)

if __name__ == "__main__":
    file = r"C:\Users\saake\OneDrive\Desktop\python\python\Em.txt"

    emails, dates = process_log(file)

    save_to_file("emails.txt", emails)
    save_to_file("dates.txt", dates)

    print("Processing Completed!")
    print(f"Emails found: {len(emails)}")
    print(f"Dates found: {len(dates)}")