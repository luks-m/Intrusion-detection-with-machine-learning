# Time series learning applied to intrusion detection in IT systems

## Table of content

- [Description](#description)
- [Report](#report)
- [Requirements](#requirements)
- [Project](#project)
    - [Network logs classification](#network-logs-classification)
    - [Text prediction](#text-prediction)
    - [Learning finite state machine](#learning-finite-state-machine)
    - [Cybersecurity automation](#cybersecurity-automation)
- [Author](#author)

## Description
This project is a 2nd year engeneering school internship project at the University Of Québec in Outaouais.  
The purpose was to search and developp a program to code a neural network to learn time series in order to automate the sort of security alerts in a network.

## Report
You can access and read my final report in the folder `report`.

## Requirements
To install all required libraries, go to project root and run:
```bash
$ pip install -r requirements.txt
```

## Project

### Network logs classification
To execute the logs classification, go to `src/Intrusion-Detection-NSL-KDD/` folder.  
Then, use the command :
```bash
$ python3 attack_classification.py
```

### Text prediction
To execute the text prediction, go to `src/Word-Prediction` folder.   
Then, use this command to fit the model :
```bash
$ python3 text_precition.py
```
Then, use this command to test it :
```bash
$ python3 newt_word.py
```

### Learning finite state machine
To execute the text prediction, go to `src/Finite-State-Machine` folder.   
Then, use this command to fit the model :
```bash
$ python3 neural_network.py
```
Then, use this command to test it :
```bash
$ python3 test_prediction.py
```

### Cybersecurity automation
To execute the text prediction, go to `src/Final-Project` folder.   
Then, use this command to fit the model :
```bash
$ python3 lstm.py
```

## Authors

- [MARAIS Lucas](<Lucas.Marais@enseirb-matmeca.fr>)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   
MIT License - Copyright (c) 2022 Lucas MARAIS