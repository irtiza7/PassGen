# PassGen
Simple app to generate, save and query credentials (passwords, etc.). Using SQLite with python.

Just another day I was sitting and wondering how secure is Google Chrome's credential storage. So then I thought of building my own app that will store credentials on the local machine, in a simple file.
I wanted to store the passwords by first encrypting them, but then it turned out to be quite a hustle 'cause of Binary-String conversion and storage. I was having issues in querying. 
So then I decided to use a simple database which will store the credentials without encryption but the file wont be readable directly. I used SQLite as its the simplest and fastest to implement.

To use this app you need to have Python 3 (or higher). 
Run the script with "python main.py".