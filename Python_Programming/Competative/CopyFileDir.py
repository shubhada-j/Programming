# Write a program that copies all .txt files from one directory to another every ten minutes

import os
import shutil
import schedule
import time

Source = "SourceFolderPath"
Destination = "DestinationFolderPath"

def CopyFiles():

    for file in os.listdir(Source):
        if file.endswith(".txt"):
            shutil.copy(os.path.join(Source, file), Destination)
            print(file, "copied")

def main():

    schedule.every(10).minutes.do(CopyFiles)

    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()