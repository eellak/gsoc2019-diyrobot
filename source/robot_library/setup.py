from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name="proteas_lib",
    version="1.0.0",
    author="Christos Chronis",
    author_email="hronis@hotmail.com",
    description="A Rasperry Pi robot library for educators.",
    long_description_content_type="text/markdown",
    long_description= README,
    url="https://github.com/eellak/gsoc2019-diyrobot",
    keywords=['Robot', 'STEM', 'Educational robot', '3D Printed Robot'],
    packages=find_packages(),
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)


requirements = ['netifaces','mpu6050-raspberrypi','Pillow','matplotlib']

if __name__ == '__main__':

	setup(**setup_args, install_requires=requirements, setup_requires=requirements)
