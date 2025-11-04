# Tkinter GUI Typing Speed Detector

**Author:** Hemant Vijay
**Last Updated:** 4-Nov-2025
**Course:** 100 Days of Code by Angela Yu
**Course URL:** https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

## Project Overview

This is a desktop application built with Python and Tkinter that tests your typing speed. The application measures how quickly and accurately you can type a given text passage, then calculates your typing speed in words per minute (WPM) along with your accuracy percentage.

## Purpose

This project was created as part of an assignment for the "100 Days of Code: The Complete Python Pro Bootcamp" course by Angela Yu on Udemy. It demonstrates practical skills in building graphical user interfaces with Python and implementing real world functionality for measuring user performance.

## Features

The Typing Speed Detector includes the following features:

**Random Text Selection:** Each test uses a randomly selected passage from a collection of sample texts, ensuring variety in every test.

**Accurate Timing:** The application precisely tracks the time from when you start typing until you submit your test.

**Speed Calculation:** Your typing speed is calculated in words per minute (WPM), which is the standard measurement for typing speed.

**Accuracy Measurement:** The application compares your typed text character by character with the original text and calculates your accuracy as a percentage.

**User Friendly Interface:** The application has a clean, modern interface with clear instructions and easy to use buttons.

**Test Management:** You can start a new test, submit your results, or reset the application at any time.

## How to Use

**Starting the Application:** Run the main.py file using Python. A window will open with the title "Typing Speed Detector" at the top.

**Beginning a Test:** Click the "Start Test" button. A sample text will appear in a white box near the top of the window. This is the text you need to type.

**Typing the Text:** Click in the text input area below (where it says "Type here:") and begin typing the sample text as quickly and accurately as you can. The timer starts automatically when you press your first key.

**Submitting Your Test:** When you finish typing, click the "Submit" button. The application will calculate your results and display them both in the window and in a popup message box.

**Viewing Results:** Your results show three pieces of information: the time you took in seconds, your typing speed in words per minute, and your accuracy percentage.

**Starting Over:** Click the "Reset" button to clear everything and prepare for a new test. Then click "Start Test" again to begin another round.

## System Requirements

**Operating System:** Windows 11 Pro 64-bit (tested and verified to work)

**Python Version:** Python 3.6 or higher

**Dependencies:** None. All required libraries (tkinter, time, random) come built in with Python.

## Installation

To set up and run this application on your Windows 11 computer:

**Install Python:** Download and install Python 3.6 or higher from python.org. Make sure to check the box that says "Add Python to PATH" during installation.

**Download the Project:** Download or clone this project to a folder on your computer.

**Run the Application:** Open a command prompt or terminal in the project folder and run the following command:

```
python main.py
```

Alternatively, you can double click the main.py file if Python is properly associated with .py files on your system.

## Technical Details

**Programming Language:** Python 3

**GUI Framework:** Tkinter (Python's standard GUI library)

**Architecture:** Object oriented design with a single main class (TypingSpeedDetector) that manages the entire application.

**Calculation Methods:**

The typing speed is calculated using the formula: (number of words typed / seconds elapsed) times 60 to convert to words per minute.

Accuracy is calculated by comparing each character in your typed text with the original text and dividing the number of correct characters by the total number of characters in the original text, then multiplying by 100 to get a percentage.

## File Structure

**main.py:** The main application file containing all the code for the typing speed detector.

**license.dat:** Contains licensing information, credits, and attribution for the project and its dependencies.

**README.md:** This file, which provides comprehensive documentation about the project.

**requirements.txt:** Lists the project requirements (in this case, a description of what the application does).

## Learning Outcomes

By completing this project, you will learn:

How to create graphical user interfaces with Python using Tkinter

How to handle user input events in a GUI application

How to work with timing functions to measure elapsed time

How to implement text comparison algorithms for accuracy checking

How to structure a larger Python application using object oriented programming

How to create a complete, functional desktop application from start to finish

## Acknowledgments

Special thanks to Angela Yu for creating the "100 Days of Code" course, which provides structured, hands on learning through practical projects like this one. The course offers excellent instruction for anyone looking to master Python programming through daily practice and real world applications.

## Support

For questions or issues related to this specific implementation, please refer to the course materials or reach out through the appropriate course channels on Udemy.

## Project Status

This project is complete and fully functional as of 4-Nov-2025. It has been tested on Windows 11 Pro 64-bit operating system and works as intended.
