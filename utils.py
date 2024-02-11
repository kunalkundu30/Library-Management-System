import yaml


def get_configuration_file_location():
    """
    Get configuration file location

    Parameters
    ----------
    """
    configuration_file_location = "config.yml"
    return configuration_file_location


def get_configuration_file(configuration_file_location: str) -> dict:
    """
    Get all configurations

    Parameters
    ----------
    configuration_file_location: str
        Location of file
    """
    with open(configuration_file_location, "r") as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
    return config