import re

txt = "I am John. I live in London."


capital_words = re.findall(r"\b[A-Z][a-z]*\b", txt)


common_names = ["I", "John"]
residence_area = [word for word in capital_words if word not in common_names]

if residence_area:
    print("Extracted Residence Area:", residence_area[0])
else:
    print("Residence Area Not Found")
