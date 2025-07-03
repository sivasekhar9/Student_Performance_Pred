from setuptools import find_packages, setup
from typing import List

# Special marker to identify editable install line
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of packages,
    excluding '-e .', which is only used for pip editable installs.
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            # Remove leading/trailing whitespace like \n or spaces
            package = line.strip()
            # Skip empty lines or '-e .'
            if package and package != HYPHEN_E_DOT:
                requirements.append(package)
    return requirements

# Now call setup() to define your package
setup(
    name='Student_Performance_Pred',  # Name of your project
    version='0.0.1',                  # Version number
    author='Siva Sekhar Medisetty',   # Your name
    author_email='sivasekharnaidu1@gmail.com',  # Your email
    packages=find_packages(),         # Automatically find Python packages in your project
    install_requires=get_requirements('requirements.txt')  # Get the required packages
)

