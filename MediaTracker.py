import sqlite3

class MediaTracker():

    def __init__(self, dbName='media.db'):
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self._createTable()

    def _createTable(self) -> None:
        """Creates db file if it does not exist in the working directory.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS media (
                id INTEGER PRIMARY KEY,
                title TEXT,
                type TEXT, 
                status TEXT,
                rating INTEGER 
            )
        ''')
        self.conn.commit()
    
    def addMedia(self, title, type, status, rating=0) -> None:
        """Adds a media entry to the database.

        Args:
            title (str): The title of the media
            type (str): The type of media (song, movie, tv)
            status (str): Whether or not the user has completed consuming this media
            rating (int, optional): the users rating on a scale of 1-10. Defaults to 0, useful when media is not yet complete.
        """
        self.cursor.execute("INSERT INTO media (title, type, status, rating) VALUES (?, ?, ?, ?)", 
                            (title, type, status, rating))
        self.conn.commit()
    
    def deleteMedia(self, title) -> None:
        """Deletes a media entry from the databse.

        Args:
            title (str): title of media.
        """
        self.cursor.execute("DELETE FROM media WHERE title = ?", (title,))
        if input("\nAre you sure?[y/n]: ") == 'y':
            self.conn.commit()
        
    def updateMedia(self, collumn, toUpdate, newVal) -> None:
        """Updates the data of a certain database entry.

        Args:
            collumn (int): An integer 1-4 to diferentiate the collumn to be updated
            toUpdate (str): The title of media to be updated
            newVal (any): The new value to be saved in the database
        """
        match collumn:
            case 1: #title
                self.cursor.execute("UPDATE media SET title = ? WHERE title = ?;",
                            (newVal, toUpdate))
            case 2: #type
                self.cursor.execute("UPDATE media SET type = ? WHERE title = ?;",
                            (newVal, toUpdate))
            case 3: #status
                self.cursor.execute("UPDATE media SET status = ? WHERE title = ?;",
                            (newVal, toUpdate))
            case 4: #rating
                self.cursor.execute("UPDATE media SET rating = ? WHERE title = ?;",
                            (newVal, toUpdate))
        self.conn.commit()
            

    def displayAll(self) -> None:
        """Queries and prints the entire databse of media."""
        self.cursor.execute("SELECT id, title, type, status, rating FROM media")
        rows = self.cursor.fetchall()

        print(f"{'ID':<4} | {'Title':<20} | {'Type':<10} | {'Status':<15} | {'Rating':<4}")
        print('-' * 68)

        for row in rows:
            id, title, type, status, rating = row
            print(f"{id:<4} | {title:<20} | {type:<10} | {status:<15} | {rating:<4}")
        print()

    def displayFiltered(self) -> None:
        pass

    def close(self) -> None:
        """Closes the SQL connection."""
        self.conn.close()


############# UI Helper Methods ############# 

def updateEntriePromt():
    """Prompts user for input depending on what data they would like to update.

    Returns:
        choice (int): An integer 1-4 to diferentiate the collumn to be updated
        title (str): The title of the media
        type (str): The type of media (song, movie, tv)
        status (str): Whether or not the user has completed consuming this media
        rating (int, optional): the users rating on a scale of 1-10. Defaults to 0, useful when media is not yet complete.
    """
    print('\n----- Update Entries  -----')
    toUpdate = input('Enter title of media to update: ')

    print('\n1. Update title')
    print('2. Update type')
    print('3. Update status')
    print('4. Update rating\n')
    
    choice = int(input('Enter choice: '))

    match choice:
        case 1:
            title = input('Enter new title: ')
            return choice, toUpdate, title
        case 2:
            type = input("Enter new media type: ")
            return choice, toUpdate, type
        case 3:
            status = input("Enter new staus (in-progress/complete): ")
            return choice, toUpdate, status
        case 4: 
            rating = int(input('Enter new rating (0 if in-progress, 1-10 if complete): '))
            return choice, toUpdate, rating
        

############# Driver Code ############# 

def main():
    mt = MediaTracker()

    while True:
        print('----- Media Tracker -----')
        print('1. Add media')
        print('2. Display all media')
        # print('3. Display filtered media')
        print('3. Update entries')
        print('4. Delete entry')
        print('5. Exit')

        choice = int(input('Enter choice: '))

        match choice:
            case 1:
                print('\n----- Add Media  -----')
                title = input('Enter title: ')
                type = input('Enter media type: ')
                status = input('Enter completion status [in-progress/complete]: ')
                rating = int(input('Enter rating [0 if in-progress, 1-10 if complete]: '))
                title, type, status, rating
                mt.addMedia(title, type, status, rating)
            case 2:
                mt.displayAll()
            case 3:
                mt.updateMedia(*updateEntriePromt())
            case 4:
                print('\n----- Delete Entry  -----')
                mt.deleteMedia(input('Enter title of media to delete: '))
            case 5:
                mt.close()
                break


if __name__ == "__main__":
    main()
