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
* Add
  * Title
  * Type
  * Status
  * Rating
* Delete
* Modify
  * Modify a specific category in a specific entry
* Display
  * Sory by: Date of Entry, Title, Type, Status, Rating
## Future Additions Could Include
* Defensive programming practices
* Filtered display
* Database indexing
* GUI