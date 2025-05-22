import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\Admin\OneDrive\Desktop\Qusai Kagalwala\Imp Documents"
destination_dir = r"C:\Users\Admin\OneDrive\Desktop\Qusai Kagalwala\Projects\Python Projects\BACKUP"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    # Check if the directory exists before copying to prevent overwriting
    if not os.path.exists(dest_dir):
        try:
            shutil.copytree(source, dest_dir)
            print(f"Folder copied to {dest_dir}")
        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        print(f"Folder already exists at {dest_dir}.")

# Schedule task at 00:03 AM
schedule.every().day.at("11:09").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
