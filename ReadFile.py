#Import libraries
import csv

class CSVtoDictConverter:
    def open(self, filename):
        dictionary = dict()
        with open(filename, "r") as file:
            # Read CSV file
            reader = csv.reader(file)

            # Convert CSV file into transactional table
            for entry in reader:
                # Reading columns
                username = entry[0]
                artist = entry[1]
                rating = float(entry[2])
                
                # Create a new entry for user
                if username not in dictionary:
                    dictionary[username]=dict()
                
                # Adding the artist with rating to current user's list
                dictionary[username][artist] = rating

        return dictionary