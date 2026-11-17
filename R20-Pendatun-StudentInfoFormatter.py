first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

clean_first = first_name.strip().title()
clean_last = last_name.strip().title()
full_name = f"{clean_first} {clean_last}"
name_code = full_name.upper()
clean_section = section.strip().upper()
clean_subject = favorite_subject.strip().title()
char_count = len(full_name)

print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {clean_section}")
print(f"Favorite Subject: {clean_subject}")
print(f"Character Count: {char_count}")
