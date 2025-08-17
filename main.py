# Einfaches Python-Programm, das ein Anschreiben automatisch generiert

name = input("Bitte gebe den Namen ein: ")

mein_name = "Tomi Nguyen"
stadt = "Berlin"
age = "23"
semester = "2. Semester"
Fach = "Informatik"

is_woman = True

if is_woman: 
    print("Sehr geehrte Frau " + name)
else: 
    print("Sehr geehrter Herr " + name)

print("Mein Name ist " + mein_name)
print("Ich bin " + age + " Jahre alt")
print("Ich studiere momentan im " + semester + " " + Fach + " und möchte mich hiermit als Werkstudent bewerben")
print("Im Anhang befindet sich mein Bewerbungsschreiben und mein Lebenslauf")
print("Mit freundlichen Grüßen")
print(mein_name)
input('Bitte beliebige Taste drücken.....')

