import csv
import os
from tabulate import tabulate
import subprocess

csv_data = []

def display_menu():
    print("Menu:")
    print("1. Open CSV File")
    print("2. Print the CSV File to .prn and edit using vi")
    print("3. Save")
    print("4. Exit")

def open_csv_file():
    global csv_data
    file_path = input("Enter the path to the CSV file: ")
    if not os.path.isfile(file_path):
        print("File not found.")
        return
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        csv_data = list(reader)
        print("CSV file loaded successfully.")

def print_csv_file():
    if not csv_data:
        print("No CSV file loaded.")
        return
    
    prn_file_path = "output.prn"
    with open(prn_file_path, 'w', newline='') as prn_file:
        writer = csv.writer(prn_file, delimiter=' ')
        writer.writerows(csv_data)
    
    print(f"CSV data written to {prn_file_path}")
    
    # Open the .prn file in vi
    subprocess.call(['vi', prn_file_path])
    
    # Reload the edited data from the .prn file
    with open(prn_file_path, 'r', newline='') as prn_file:
        reader = csv.reader(prn_file, delimiter=' ')
        csv_data.clear()
        csv_data.extend(list(reader))
    
    print(f"{prn_file_path} has been edited and reloaded.")

def save_csv_file():
    if not csv_data:
        print("No CSV file loaded.")
        return
    
    file_path = input("Enter the path to save the CSV file: ")
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
        print("CSV file saved successfully.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            open_csv_file()
        elif choice == '2':
            print_csv_file()
        elif choice == '3':
            save_csv_file()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
