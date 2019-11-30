Python Lugh
==================================

## Code style
Standard Python code

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)
# Overview of project

Lugh is a IOT project where it will detect for children in distress due to parents phubbing them. It detects

Quick Start
-----------

In order to run this project, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`
2. `Enable billing for your project.`
3. `Configure the api's`
4. `Git clone the repository.`
5. `Cd into Lugh`
6. `Run the aws_pubsub.py file`


## Supported Python Versions

Python >= 2.7

# Deprecated Python Versions

Python == 2.7. Python 2.7 support will be removed on January 1, 2020.

## Installation

To implement the aws functions, the libraries need to be installed on the Raspberry Pi. 
Install the required libraries
```bash
sudo pip install requirements.txt
```
Install Rekognition
```bash
sudo  pip install boto3
```

## Authentication

If you want to run all programs, you will need a billing-enabled project, and a service account with access to the APIs. Running the command below allows for your computer to be authenticated and allowed to run and use the files.
```bash
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
```
## Hardware
- 1x Raspberry pi
- 1x Raspberry pi camera
- 1x Portable Charger


## Billing
To re-enable billing on a project:

1. Go to the Google Cloud Platform Console.
2. From the projects list drop-down at the top of the page, select the project to re-enable billing for.
3. Open the console navigation menu (menu) and select Billing.
4. Click Link a billing account.
5. Select a billing account, then click SET ACCOUNT.

## Architecture

The System architecture of the image recognition.

![Image of Imagerecog](https://github.com/evanderleng/IOTv2-Electric-Boogaloo/blob/master/Images/4.png)

## Expected outcome
To test if the program works, run the python file

## Authors

* **Davis Zheng** - [Nonsour](https://github.com/nonsour)/[Nonsouris](https://github.com/nonsouris)

## Acknowledgments

* Thanks to Ms Dora Chua for her guidance


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
