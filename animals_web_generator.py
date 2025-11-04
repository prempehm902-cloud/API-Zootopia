import data_fetcher

animal_name = input("Enter a name of an animal: ")
animals = data_fetcher.fetch_data(animal_name)

with open("animals_template.html", "r") as file:
    template_content = file.read()

def serialize_animal(animal):
    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")
    locations = ", ".join(animal.get("locations", []))
    animal_type = animal.get("characteristics", {}).get("type")
    output = f"<li><strong>{name}</strong><br>Diet: {diet}<br>Location: {locations}"
    if animal_type:
        output += f"<br>Type: {animal_type}"
    output += "</li>"
    return output

if animals:
    output = ''.join(map(serialize_animal, animals))
else:
    output = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"

new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(new_html)

print("Website was successfully generated to the file animals.html.")

