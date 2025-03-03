from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

class YouTubePlaylistScraper:
    def __init__(self, playlist_url):
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)
        self.playlist_url = playlist_url
        self.driver = None

    def initialize_driver(self):
        self.driver = webdriver.Edge(options=self.edge_options)
        # self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.playlist_url)
        time.sleep(5)

    def scroll_to_load_all_videos(self):
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_video_titles(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, 'a#video-title')
        return [title.text for title in titles]

    def close_driver(self):
        if self.driver:
            self.driver.quit()

class CSVWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def sanitize_title(self, title):
        return title.replace('|', '_').replace(',', '_').replace('&', '_').replace(':', '_').replace('?','_').replace('"','_').replace('🔥','--').replace('#','_')

    def write_to_csv(self, video_titles):
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Sr. No.', 'Title'])  # Write the header row
            for i, title in enumerate(video_titles, 1):
                sanitized_title = self.sanitize_title(title)
                writer.writerow([i, sanitized_title])

def main():
    # driver_path = 'path/to/your/webdriver'
    playlist_url = input("Enter the Playlist URL:- ")
    csv_file_path = 'video_titles.csv'

    scraper = YouTubePlaylistScraper(playlist_url)
    scraper.initialize_driver()
    scraper.scroll_to_load_all_videos()
    video_titles = scraper.get_video_titles()
    scraper.close_driver()

    csv_writer = CSVWriter(csv_file_path)
    csv_writer.write_to_csv(video_titles)

if __name__ == "__main__":
    main()
