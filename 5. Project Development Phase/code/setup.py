from setuptools import setup, find_packages

def get_requirements(file_path):
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name="Smart_Agricultural_Production_Optimization_Engine",
    version="1.0.0",
    author="Gangadhar Lalam",
    author_email="gangadharl9390@gmail.com",
    description="Machine Learning based Crop Recommendation System using Flask",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)