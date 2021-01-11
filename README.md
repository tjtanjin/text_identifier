<p align="center">
  <img src="https://i.imgur.com/Cwgqyu3.jpg" />
  <h1 align="center">Text Identifier</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
Text Identifier was written as a side script to automate a small scope of my job while carrying out my internship at [TOFFS Technologies](https://www.toffstech.com/en/home). As part of implementing automated GUI testing, capturing relevant texts was required and having to manually mark them out on images was a huge hassle given the large amounts of screenshots. As a result, this small text identifier was born!

### Features
This was a script previously written specifically for work-related purposes. It has been refactored to be used on general images but does not guarantee full compatibility. There are also no work-sensitive information present in this entire repository. Currently, it only supports detecting full lines of texts (in other words, it detects an entire line in the picture and is unable to handle individual parts of the line). Upon an identified line of text, a red box is drawn around the text as a highlight. An example has been shown in the image at the top of this README!

### Technologies
Technologies used by Text Identifier are as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Deployed on:
<p align="center">
None (Terminal-based Application)
</p>


##### Project Repository
```
https://github.com/tjtanjin/text_identifier
```

### Setup
The following section will guide you through setting up your own Text Identifier!
* First, cd to the directory of where you wish to store the project and clone this repository. An example is provided below:
```
$ cd /home/user/exampleuser/projects/
$ git clone https://github.com/tjtanjin/text_identifier.git
```
* Next, you will need to install tesseract with the following commands:
```
$ sudo apt update
$ sudo apt install tesseract-ocr
```
* Following which, open texts.json file within the config folder and edit it with the lists of texts you wish to identify from your images (an example is already provided in the file/with the code).
* Then, create 2 folders, input_media and output_media. Within input_media, place all the images you wish to identify text from.
* Finally, run the command below from the base of the project directory and head to output_media for your annotated images:
```
$ python3 text_identifier.py
```

### Team
* [Tan Jin](https://github.com/tjtanjin)

### Contributing
If you have code to contribute to the project, open a pull request and describe clearly the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an issue.

### Others
For any questions regarding the implementation of the project, please drop an email to: cjtanjin@gmail.com.
