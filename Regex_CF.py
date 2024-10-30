import re

# Sample string
text = "The  rain in minneapolis  falls mainly    in the summer."

# 1. Matching Patterns
match = re.match(r'The', text)
if match:
    print("Match found:", match.group())  # Output: Match found: The

# 2. Searching
search = re.search(r'Spain', text)
if search:
    print("Search found:", search.group())  # Output: Search found: Spain

# 3. Finding All Matches
find_all = re.findall(r'in', text)
print("Find all matches:", find_all)  # Output: Find all matches: ['in', 'in', 'in']

# 4. Splitting Strings
split = re.split(r'\s', text)
print("Split string:", split)  # Output: Split string: ['The', 'rain', 'in', 'Spain', 'falls', 'mainly', 'in', 'the', 'plain.']

split2 = re.split(r'\W', text)
print("Split string:", split2)  # Output: Split string: ['The', 'rain', 'in', 'Spain', 'falls', 'mainly', 'in', 'the', 'plain', '']

split2 = re.split(r'\B', text)
print("Split string:", split2)  # Output: Split string: ['T', 'h', 'e r', 'a', 'i', 'n i', 'n S', 'p', 'a', 'i', 'n f', 'a', 'l', 'l', 's m', 'a', 'i', 'n', 'l', 'y i', 'n t', 'h', 'e p', 'l', 'a', 'i', 'n.', '']

split2 = re.split(r'\b', text)
print("Split string:", split2)  # Output: Split string: ['', 'The', '  ', 'rain', ' ', 'in', ' ', 'Spain', '  ', 'falls', ' ', 'mainly', '    ', 'in', ' ', 'the', ' ', 'plain', '.']
# 5. Substitution
substitute = re.sub(r'rain', 'snow', text)
print("Substitution:", substitute)  # Output: The snow in Spain falls mainly in the plain.

replacement = {"rain":"snow", "summer":"winter"}

def replace_text(text, replacement):
    for a, b in replacement:
        re.sub(a, b, text)
    return text

substitute=replace_text(text, replacement)
print("Substitution:", substitute)  # Output: The snow in Spain falls mainly in the plain.

"""
\d - look for single digit
\d+ - look for one or more digits
\d{} - look for a specific number of digits
\D - look for non-digit
\s - look for whitespace
\S - look for non-whitespace
\w - look for alphanumeric
\W - look for non-alphanumeric
\b - look for word boundary
\B - look for non-word boundary
^ - look for start of string
$ - look for end of string
? - look for zero or one occurrence #?=$   -- look for $ sign pattern =r"\d+(?=$)" look for 
* - look for zero or more occurrences

"""
