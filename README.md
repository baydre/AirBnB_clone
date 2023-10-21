# AirBnB clone - The console

## Table of Contents

- [Description of the Project](#Description-of-Project)
- [Description of the Command Interpreter](#Description-of-the-Command-Interpreter)
	- [How to start it](#How-to-start-it)
	- [How to use it](#How-to-use-it)
	- [Examples](#Examples)
 	- [Contributors](#Contributors)

## Description of Project

This project is an implementation of an AirBnB clone, focusing on the core components that make up the AirBnB service. These components include the console, models, and the storage engine. The console acts as the command-line interface for interacting with the system. The models represent the various objects and data structures used in the AirBnB system, while the storage engine is responsible for managing data storage.

## Description of the Command Interpreter

The command interpreter, often referred to as the console, is the gateway to interacting with the AirBnB clone system. It allows users to perform various operations, such as creating, updating, and deleting instances, and viewing information about them.

### How to start it

To start the console, follow these steps:

1. Enter the project directory.
2. Navigate to the `models` directory.
3. Run the `./console.py` script.

### How to use it

Once the console is running, you can interact with the AirBnB clone by using various commands. Some of the supported operations include:

- Creating new instances and saving them to a JSON file.
- Displaying the string representation of instances.
- Deleting instances.
- Displaying all string representations of instances.
- Updating instances.

### Examples

Here are a few examples of how you can use the console:

- Create a new instance:

  ```shell
  (hbnb) create BaseModel
  # Show string representation of instances
  (hbnb) show BaseModel 12345
  # Delete an instance
  (hbnb) destroy BaseModel 12345
  # List all instances:
  (hbnb) all BaseModel
  # Update an instance:
  (hbnb) update BaseModel 12345 name "New Name"

  ```

## Contributors

[Lawal Tajudeen Ogunsola](https://github.com/lawalTheWest)
[Yasir Musa](https://github.com/baydre)
