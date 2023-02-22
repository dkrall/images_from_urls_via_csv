#!/usr/bin/env python3
import csv
import os
import sys
import subprocess
import time
import wget

def get_images_from_urls_via_csv():
    input_filepath = get_filepath_to_input_file()

    with open(input_filepath, newline='') as input_file:
        reader = csv.reader(input_file, delimiter=',', quotechar='"')

        for cell_values in reader:
            if cell_values[0] != 'Title':
                if len(cell_values) > 4:
                    title = cell_values[0].replace("\"", "")
                    isbn = cell_values[1].replace("\"", "")
                    url = cell_values[2].replace("\"", "")
                    if len(url) > 0:
                        filename = wget.download(url)
                        file_extension = '.' + filename.split('.')[-1]
                        time.sleep(1)
                        while not os.path.isfile(filename):
                            print("Could not find " + filename + ". Delaying.")
                            time.sleep(0.5)
                        os.system('mv "' + filename + '" "' + '../output/' + isbn + " - " + title + file_extension + '"')
                else:
                    print("Not enough values. End of input reached.")
            else:
                print("Skipping header row.")

    input_file.close()


# Based on the input provided in the first (and only) argument, return the file path to the input file including the filename.
def get_filepath_to_input_file():
    return "../input/%s" % sys.argv[1]


if __name__ == "__main__":
    get_images_from_urls_via_csv()
