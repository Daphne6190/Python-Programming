# Data type

number = 25  # int
second = 56.76  # float
text = "Hello There"  # string
ispythoninteresting = True  # bool

# store multiple values in a single variable
cars = ["toyota", "nissan", "vw"]  # list - ordered and changeable
fruits = ("banana", "orange", "apple")  # tuple - ordered but unchangeable
countries = {"Kenya", "Tunisia", "Algeria"}  # set - unordered and unchangeable
details = {
    "firstname": "Daphne",
    "age": 23,
    "course": "web development",
    "Nationality": "Kenyan"
}

print(second)
print(text)
print(ispythoninteresting)
print(cars)
print(countries)
print(details)
print(details["course"])

# Determine a data type
print(type(number))
print(type(details))
print(type(countries))

# Typecasting - Converting one data type to another
print(float(number))
print(int(second))

