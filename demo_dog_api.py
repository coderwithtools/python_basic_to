import requests


print("=" * 60)
print("DOG CEO API - PYTHON DICTIONARY DEMONSTRATION")
print("=" * 60)


# ---------------------------------------------------------
# 1. GET JSON DATA FROM API
# ---------------------------------------------------------

print("\n1. GET DATA FROM API")
print("-" * 60)

url = "https://dog.ceo/api/breeds/image/random"
#sending a http GET request on the url 
response = requests.get(url)

print("HTTP Status Code:", response.status_code)

# Convert JSON response into Python dictionary
# this var contains datai.e. in dog var
#. json () is used to convert the data from response to 
dog = response.json()

print("API Response:")
print(dog)

print("Data type:", type(dog))


# ---------------------------------------------------------
# 2. keys()
# ---------------------------------------------------------

print("\n2. keys()")
print("-" * 60)

print("Dictionary keys:")

for key in dog.keys():
    print(key)


# ---------------------------------------------------------
# 3. values()
# ---------------------------------------------------------

print("\n3. values()")
print("-" * 60)

print("Dictionary values:")

for value in dog.values():
    print(value)


# ---------------------------------------------------------
# 4. items()
# ---------------------------------------------------------

print("\n4. items()")
print("-" * 60)

print("Dictionary items:")

for key, value in dog.items():
    print("Key:", key)
    print("Value:", value)


# ---------------------------------------------------------
# 5. get()
# ---------------------------------------------------------

print("\n5. get()")
print("-" * 60)

key = input("Enter a key to retrieve (message/status): ")

value = dog.get(key)

print("Value:", value)


# ---------------------------------------------------------
# 6. Check whether key exists
# ---------------------------------------------------------

print("\n6. CHECK KEY EXISTENCE")
print("-" * 60)

key = input("Enter a key to check: ")

if key in dog:
    print("Key exists.")
    print("Value:", dog[key])
else:
    print("Key does not exist.")


# ---------------------------------------------------------
# 7. copy()
# ---------------------------------------------------------

print("\n7. copy()")
print("-" * 60)

dog_copy = dog.copy()

print("Original dictionary:")
print(dog)

print("\nCopied dictionary:")
print(dog_copy)


# ---------------------------------------------------------
# 8. update()
# ---------------------------------------------------------

print("\n8. update()")
print("-" * 60)

location = input("Enter where you found this dog: ")

dog.update({
    "location": location
})

print("Dictionary after update():")
print(dog)


# ---------------------------------------------------------
# 9. setdefault()
# ---------------------------------------------------------

print("\n9. setdefault()")
print("-" * 60)

breed = input("Enter a breed name: ")

result = dog.setdefault("breed", breed)

print("Returned value:", result)

print("Dictionary:")
print(dog)


# ---------------------------------------------------------
# 10. pop()
# ---------------------------------------------------------

print("\n10. pop()")
print("-" * 60)

key = input("Enter a key to remove: ")

if key in dog:

    removed_value = dog.pop(key)

    print("Removed value:", removed_value)

else:

    print("Key does not exist.")

print("Dictionary after pop():")
print(dog)


# ---------------------------------------------------------
# 11. popitem()
# ---------------------------------------------------------

print("\n11. popitem()")
print("-" * 60)

print("Dictionary before popitem():")
print(dog)

if len(dog) > 0:

    removed_item = dog.popitem()

    print("Removed item:", removed_item)

print("Dictionary after popitem():")
print(dog)


# ---------------------------------------------------------
# 12. fromkeys()
# ---------------------------------------------------------

print("\n12. fromkeys()")
print("-" * 60)

keys_input = input(
    "Enter keys separated by comma: "
)

keys = keys_input.split(",")

keys = [key.strip() for key in keys]

default_value = input(
    "Enter default value: "
)

new_dictionary = dict.fromkeys(
    keys,
    default_value
)

print("New dictionary:")
print(new_dictionary)


# ---------------------------------------------------------
# 13. clear()
# ---------------------------------------------------------

print("\n13. clear()")
print("-" * 60)

clear_choice = input(
    "Do you want to clear the dictionary? (yes/no): "
)

if clear_choice.lower() == "yes":

    dog.clear()

    print("Dictionary after clear():")
    print(dog)

else:

    print("Dictionary was not cleared.")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED")
print("=" * 60)
