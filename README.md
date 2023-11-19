![airbnb clone project - the console](https://drive.google.com/uc?id=1juADwCmsarqS4dJcxYnZHAsNVFObt2to)

# The AirBnB clone project - The console

## Description

This is the first step towards buildin the **AirBnB clone** project, a first full web application.

This first step is very important because it's the foundation of all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

The console is designed to manage the objects of the project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231009%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231009T083003Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c16d4ff45d2381a28bd0ac2fb07ab92dee1de4fe7ba38c8a8fae6fa649cca8e9)

## Installation

This project requires Python 3.8.5 or higher.

To use this project:
1. clone the repository from Github:
```git clone https://github.com/med-i/AirBnB_clone```

2. Navigate to the project directory:
```cd AirBnB_clone```

3. Execute the console.py file:
```./console.py```

## Usage

=========TODO==========

## Execution

### Interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Tests

All tests should be executed by using this command: `python3 -m unittest discover tests`
They should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

## Learning Objectives

- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Authors:

* [Mohammed Ijairi](https://github.com/med-i)
* [Mohamed Ouazane](https://github.com/meedouazane)
