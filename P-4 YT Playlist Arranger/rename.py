import os
import csv
import shutil

class FileManager:
    def __init__(self, old_directory, new_directory):
        self.old_directory = old_directory
        self.new_directory = new_directory

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory created: {path}")
        else:
            print(f"Directory already exists: {path}")

    def move_file(self, src, dest):
        self.create_directory(os.path.dirname(dest))
        shutil.move(src, dest)
        print(f"File moved from {src} to {dest}")

    def rename_file(self, old_name, new_name):
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"Renamed: {old_name} to {new_name}")
        else:
            print(f"File not found: {old_name}")

    def find_matching_file(self, title):
        for file_name in os.listdir(self.old_directory):
            if file_name.startswith(title):
                return file_name
        return None

    def process_csv(self, csv_file):
        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                serial_number = row[0]
                title = row[1]
                matching_file = self.find_matching_file(title)
                if matching_file:
                    original_filename = os.path.join(self.old_directory, matching_file)
                    new_filename = os.path.join(self.new_directory, f"{serial_number} {matching_file}")
                    self.create_directory(self.new_directory)
                    self.rename_file(original_filename, new_filename)
                    self.move_file(new_filename, os.path.join(self.new_directory, os.path.basename(new_filename)))
                else:
                    print(f"File not found for title: {title}")

if __name__ == "__main__":
    old_directory = 'Videos'  # Path to the directory containing the video files
    new_directory = 'Friendly'  # Path to the new directory
    csv_file = 'video_titles.csv'  # Path to the CSV file
    
    file_manager = FileManager(old_directory, new_directory)
    file_manager.process_csv(csv_file)
