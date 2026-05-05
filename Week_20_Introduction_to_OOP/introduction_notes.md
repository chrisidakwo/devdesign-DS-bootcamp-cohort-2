# The Shift in Thinking - From Procedures to Objects

# Object-Oriented Programming (OOP)

In procedural programming, you think in terms of steps:

1. Load the data
2. Explore the data
3. Clean the data
4. Filter the data
5. Analyse the data
6. Plot the result

In object-oriented programming, you think in terms of objects/things - real world entities that have both properties (what they are) and behaviours (what they can do)

```python
class Car:
    TYRES = 4
    # Define the properties of Car -> attributes
    model: str
    brand: str
    production_year: int
    no_of_doors: int
    engine_capacity: int
    speed: int
    
    def __init__(self, model, brand, production_year, no_of_doors, engine_capacity, speed):
        self.model = model
        self.brand = brand
        self.production_year = production_year
        self.no_of_doors = no_of_doors
        self.engine_capacity = engine_capacity
        self.speed = speed
    
    # Define the behaviours of Car -> methods
    def accelerate(self, pressure):
        pass
    
    def brake(self, pressure):
        pass
    
    def details(self):
        print({
            "model": self.model,
        })

xyz = Car('Corolla', 'Toyota', 2021, 4, 2.4, 0)
xyz.accelerate(30)
# xyz.model = 'Corolla'
# xyz.brand = 'Toyota'
# xyz.production_year = 2021
# xyz.no_of_doors = 4
# xyz.engine_capacity = 2.4
# xyz.speed = 0

car2 = Car()
car2.model = 'Bentayga'
car2.brand = 'Bentley'
car2.production_year = 2020
car2.details()
car2.accelerate(30)
```

Instances (objects) are implementations of a class (the blueprint)

Instances are objects.

An object is an instance of a class


```python
class CrimeIncident:
    case_number: str
    incident_date: str
    primary_type: str
    arrest: int
    domestic: int

num = 5

abc = CrimeIncident()
abc.incident_date = '08-04-2026'
abc.case_number = 'DFG5895400'
abc.primary_type = 'Homicide'
abc.arrest = 1
abc.domestic = 0
```

## Core OOP Concepts

1. Class -> is a blueprint or template that defines the structure and behaviours of the objects of the class
2. Object (Instance) -> a specific, concrete implementation created/derived from a class.
3. Attribute -> Refers to a property in a class. E.g: A crime incident has a data, primary type, location, arrest status, etc. These are all attributes.
4. Method -> A method defines a behaviour of an object. Methods are functions that belong to a class.

