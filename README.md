# Getting Started
Start with setting up the local environment for running the app.
first clone the repo.
```BASH
$ git clone https://github.com/rajsinghparihar/PsypherX.git
```
# Requirements
- all the prerequisite files are in the requirements.txt
- make sure to run the following command
```BASH
$ cd PsypherX
$ pip install -r requirements.txt
````
-If pip doesn't work on your system, use this command to install requirements
```BASH
$ python -m pip install -r requirements.txt
```
this command will install all necessary python libraries that are needed for the program to run.
after this, just run the program by the following command
```BASH
$ python PsypherX.py
```
The whole process should look like this without any errors:

<img src="https://github.com/rajsinghparihar/PsypherX/blob/main/DemoGifs/Demo1.gif"/>

# How to use
- When the app is launched, it asks you the password that you wish to encrypt, the key that helps in the encryption process and the platform for which this password is used.
- The app then encrypts your weak password using AES encryption according to the key that you give it.
- The key could be anything, I prefer to use my key as my username for that platform.
So for exampla say that my password is "password" and my username for that platform is "raj_singh".
now, since my password isn't very secure, this app will make a new password for me using a combination of my username 
and my weak password using the username as the key and encrypting the weak password with AES 128 encryption.
- some additional features are that it stores your encrypted passwords along with the platform you use them for, in a csv file (passwords.csv) and shows them on the terminal in tablular format.
The whole process of using the app looks like this:
<img src="https://github.com/rajsinghparihar/PsypherX/blob/main/DemoGifs/Demo2.gif"/>
