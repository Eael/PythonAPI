# PythonAPI
A repo to practice my python skills and learn how to use the Python Imaging Library(PIL).  The goal is to build a program that automatically resizes and rotates a bunch of images, and converts them from one image format to another.
An API helps different pieces of software talk to each other. APIs help us interact extensively with the library we choose to work with even when the codes change.
You can start by installing the PIL library on your computer using "sudo apt install python3-pil" for ubuntu users and "pip3 install pillow" for other environments. Pillow is the new name for the PIL library. PIL works only in python3
I am using a python virtual environment(python -m venv .venv, source .venv/bin/activate or source .venv/Scripts/activate)

Problem Statement 


Problems Encountered
You need to use python3
source .venv/bin/activate didn't work rather source .venv/Scripts/activate worked. 

Iterating through the directory created a .DS_Store file which caused problems. You can ignore it using "for file in glob('ic_*'):"

/opt/icons does not exist in Windows so using it is a problem
