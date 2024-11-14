
# Regular expression to find an integer before the decimal point
match = re.search(r'\d+', input_string)

# Check if a match is found
if match:
    # Get the matched integer (it will be a string, so we convert it to an integer)
    integer_part = int(match.group())
    print(integer_part)
else:
    print("No integer found")
