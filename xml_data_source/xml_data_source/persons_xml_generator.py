import xml.etree.ElementTree as ET
import random

def generate_person_data(num_persons):
    persons = []
    for i in range(1, num_persons + 1):
        person_id = str(i)
        other_persons = [j for j in range(1, num_persons + 1) if j != i]  # Exclude the current person ID

        person = {
            'id': person_id,
            'name': f'Person {i}',
            'street': f'{random.randint(1, 999)} {random.choice(["Main", "Second", "Park"])} St',
            'city': random.choice(["New York", "Los Angeles", "Chicago"]),
            'owner_reference': random.choice(other_persons)
        }
        persons.append(person)
    return persons

def generate_persons_xml(num_persons):
    persons = generate_person_data(num_persons)

    persons_elem = ET.Element('com.example.Persons')
    for person in persons:
        person_elem = ET.Element('Person', id=person['id'])

        name_elem = ET.SubElement(person_elem, 'name')
        name_elem.text = person['name']

        address_elem = ET.SubElement(person_elem, 'address')

        street_elem = ET.SubElement(address_elem, 'street')
        street_elem.text = person['street']

        city_elem = ET.SubElement(address_elem, 'city')
        city_elem.text = person['city']

        owner_elem = ET.SubElement(address_elem, 'owner')
        reference_elem = ET.SubElement(owner_elem, 'Person', reference=f"Person[{person['owner_reference']}]")

        persons_elem.append(person_elem)

    tree = ET.ElementTree(persons_elem)
    tree.write('persons.xml', encoding='utf-8', xml_declaration=True)
    print("XML file 'persons.xml' has been generated successfully.")

if __name__ == "__main__":
    generate_persons_xml(5)  # Generate XML data for 5 persons
