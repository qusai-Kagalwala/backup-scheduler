# 📁 Backup Scheduler

🤖 Automated daily backup tool that keeps your important documents safe and organized!

## ✨ Features

- 🕐 **Scheduled Backups**: Automatically backs up your files at a specified time daily
- 📅 **Date-Organized**: Creates backup folders with today's date for easy organization
- 🛡️ **Duplicate Prevention**: Prevents overwriting existing backups for the same day
- 🐍 **Python-Powered**: Simple and reliable Python script using built-in libraries

## 🚀 Quick Start

### Prerequisites
```bash
pip install schedule
```

### Setup
1. 📥 Clone this repository:
   ```bash
   git clone https://github.com/qusai-Kagalwala/backup-scheduler.git
   cd backup-scheduler
   ```

2. ⚙️ Configure your paths in `backup.py`:
   ```python
   source_dir = r"C:\Your\Source\Directory"
   destination_dir = r"C:\Your\Backup\Directory"
   ```

3. ⏰ Set your preferred backup time:
   ```python
   schedule.every().day.at("11:09").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
   ```

4. ▶️ Run the script:
   ```bash
   python backup.py
   ```

## 📋 How It Works

1. 🎯 The script monitors for the scheduled time (default: 11:09 AM)
2. 📂 Creates a new folder named with today's date (e.g., `2025-05-22`)
3. 📋 Copies all contents from source directory to the dated backup folder
4. ✅ Skips backup if folder for today already exists
5. 🔄 Repeats daily automatically

## 📁 Folder Structure

```
Backup Directory/
├── 2025-05-20/
│   └── [Your backed up files]
├── 2025-05-21/
│   └── [Your backed up files]
└── 2025-05-22/
    └── [Your backed up files]
```

## ⚙️ Configuration

### Change Backup Time
```python
# Examples:
schedule.every().day.at("09:00").do(...)  # 9:00 AM
schedule.every().day.at("18:30").do(...)  # 6:30 PM
schedule.every().day.at("23:59").do(...)  # 11:59 PM
```

### Modify Check Interval
```python
time.sleep(60)  # Check every 60 seconds (default)
time.sleep(30)  # Check every 30 seconds
```

## 🔧 Troubleshooting

- **❌ Permission Errors**: Ensure you have read/write access to both source and destination directories
- **📁 Path Issues**: Use raw strings (`r"path"`) for Windows paths to handle backslashes correctly
- **⏰ Time Format**: Use 24-hour format (HH:MM) for scheduling

## 🤝 Contributing

Feel free to submit issues and enhancement requests! 

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Qusai Kagalwala**
- GitHub: [@qusai-Kagalwala](https://github.com/qusai-Kagalwala)

---

⭐ **Star this repo if it helped you keep your files safe!** ⭐
