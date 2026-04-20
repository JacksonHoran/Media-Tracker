# Media Tracker CLI
A Python application for cataloging and tracking your personal media library (movies, music, TV shows, etc.) using a SQLite database.
## How to Run the Project
### Prerequisites
* **Python 3.10+**: This project uses the match statement which requires Python 3.10 or higher.
### Steps to Run
1. Save the code into a file named `MediaTracker.py`.
2. In the terminal navigate to the directory where you saved the file.
3. Execute the file using the following command:
  ```
  python3 MediaTracker.py
  ```
4. Upon the first run, a file named `media.db` will be created in the working directory to store your entries.
5. Follow the prompts on screen to navigate the application, enjoy!
## Features
This application allows users to add, delete, and edit media in the database. When the user chooses to add media, they will be prompted to enter the title, type (movie, song, book, etc), status (in-progress, complete), and a rating (1-10). By default every entry is indexed to allow for the addition of more advanced features in the future. I also added the ability to display all of the data, when the user chooses this option they are prompted on how they would like to sort the data. The current implementation will sort the data in alphabetical or numerical ascending order based on the user's choice.
One specific implementation choice I would like to highlight is the protection against SQL injection in the display methods. Instead of directly putting user input into the sql query, use a python dictionary to confirm that the column name exists in the database. Although this might not be necessary for this specific application it highlights some of the things that developers need to protect against when working with databases.
## Future Additions
If I was given a bit more time I would first make the app more robust. Given that this app is based on command-line input I would like to add defensive features to protect from poor user input. I could use Try/Except blocks and prompt the user if the program is given bad input. I would also like to add a filtering option where users can not only display the sorted data but filter out unwanted entries. This can help users search their database and find specific entries when the number of elements grows larger.