"""
FileName: utils.py
Author: Kunal Kundu
Date: Feb 10,2024

File Description:
Provides utility functions for accessing and reading the application's configuration settings.
Facilitates the retrieval of configuration details from a YAML file, enhancing modularity and ease of configuration management.

Design Comments:
Utilizes the YAML format for configuration files, allowing for human-readable and hierarchical configuration data.
Encapsulates configuration access within utility functions, abstracting the details of file handling and parsing, and promoting reuse across the application.
"""


import yaml


def get_configuration_file_location():
    """
    Retrieves the location of the configuration file.
    @Summary: Returns the path to the configuration file used by the application.
    @return (str): The path to the configuration file.
    """
    configuration_file_location = "config.yml"
    return configuration_file_location


def get_configuration_file(configuration_file_location):
    """
    Reads and parses the configuration file.
    @Summary: Loads and returns the settings from the specified YAML configuration file.
    @param configuration_file_location (str): The path to the YAML configuration file.
    @return (dict): A dictionary containing the parsed configuration settings.
    """
    with open(configuration_file_location, "r") as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
    return config