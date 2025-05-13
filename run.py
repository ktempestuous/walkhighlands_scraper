import subprocess
import os
import time
import platform

# Step 1: Run Scrapy Spider

def run_scrapy_spider():
    # run spider from project's root directory
    command = ['scrapy', 'crawl', 'walks', '-o', 'walks.json']
    try:
        print("Running Scrapy spider...")
        subprocess.run(command, check=True)
        print("Scrapy spider finished.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the Scrapy spider: {e}")
        exit(1)

# Main function to execute both tasks sequentially
def main(): 
    
    # Step 1: run Scrapy spider
    run_scrapy_spider()

# run main function
if __name__ == "__main__":
    main()

