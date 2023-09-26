import csv
def calculate_sum(num1, num2):
    return num1 + num2

def calculate_sub(num1, num2):
    return num1 - num2

def calculate_mult(num1, num2):
    return num1 * num2

def calculate_div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError('Division by zero is not allowed')
def calculate_word_count_from_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
            word_count = len(content.split())
        return word_count
    except FileNotFoundError:
        raise FileNotFoundError('File not found.')

def calculate_average_from_csv(file, col):
    try:
        total_sum = 0
        count = 0
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    total_sum += float(row[col])
                    count += 1
                except (ValueError, IndexError):
                    pass
        if count == 0:
            raise ValueError('Invalid column number or no valid numbers in the column.')
        average = total_sum / count
        return average
    except FileNotFoundError:
        raise FileNotFoundError('File not found.')