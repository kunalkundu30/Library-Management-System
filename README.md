# Library Management System README

## Overview
The Library Management System (LMS) is a modular application designed to manage library operations including book and user management, checkouts, and returns. It emphasizes simplicity, modularity, and ease of use, both for library staff and users.

## Design Architecture
- **Modular Design**: The system is structured around discrete modules (e.g., `Book`, `User`, `Library`, `storage`, `utils`) for specific functionalities, promoting separation of concerns and ease of maintenance.
- **Data Storage**: Utilizes CSV files for storing books and user data, and a YAML file for configuration settings, ensuring easy data manipulation and configuration management.
- **Static Methods**: The `Library` class employs static methods to provide direct access to library operations without the need for instantiation, streamlining interaction patterns.
- **Flexible Data Handling**: Objects like `Book` and `User` encapsulate their attributes in dictionaries, supporting dynamic attribute management and future expansions.

## Navigation and Usage
- **Configuration**: Set up application settings in `config.yml`, including paths for book and user data storage.
- **Book Management**:
  - Add, list, search, update, and delete books using the `Library` class methods.
  - Book attributes include title, author, ISBN, copies available, and borrowing details.
- **User Management**:
  - Add, list, search, update, and delete users through `Library` class functionalities.
  - User attributes cover name, user ID, and a record of borrowed books.
- **Checkouts and Returns**:
  - Handle book checkouts and returns with methods that update both book and user records accordingly.
- **Utility Functions**:
  - `utils.py` includes functions for retrieving configuration details and ensuring the application's flexible setup.

## Getting Started
1. **Configuration**: Ensure `config.yml` is correctly set up with your storage paths.
2. **Initialization**: Run `main.py` to start the application and navigate through the menu for various operations.
3. **Data Management**: Use the `storage.py` module for direct manipulation of CSV files for data management tasks.

This README provides a concise overview of the LMS project, outlining its design principles, architecture, and basic navigation instructions.