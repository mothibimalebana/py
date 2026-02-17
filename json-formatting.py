import json

person = {"name": "Mothibi", "age": 25, "hobbies": ["reading", "coding"]}
numbers = [1, 2, 3, 4, 5]
mixed_data = (42, "hello", True, None)

person_json = json.dumps(person)
numbers_json = json.dumps(numbers)
mixed_data_json = json.dumps(numbers)

print(f'{person_json}\n{numbers_json}\n{mixed_data}\n')