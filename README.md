# YouTube Song Downloader 🎵

A Python script to quickly and easily download songs from YouTube in audio format. The script utilizes the `yt-dlp` library to search for and download songs based on user-provided titles.

## Features
- Search and download songs directly from YouTube using their titles.
- Automatically fetch the best audio quality available.
- Save downloaded songs with their title as the filename.

---

## Requirements

Before running the script, ensure you have the following installed:

1. **Python 3.6+**: [Download Python](https://www.python.org/downloads/)
2. **yt-dlp**: Install it using the command below:
   ```bash
   pip install -U yt-dlp
   ```

---

## How to Use

1. Clone this repository or copy the script to your local machine:
   ```bash
   git clone https://github.com/sudhucodes/ytmusicdownloader.git
   cd ytmusicdownloader
   ```

2. Update the `song_list` in the script with the songs you want to download. For example:
   ```python
   song_list = [
       "Song Name 1",
       "Song Name 2",
       "Song Name 3"
   ]
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. The downloaded audio files will be saved in the current working directory with the song title as the filename.

---

## Example

### Input:
The `song_list` contains:
```python
song_list = [
    "Chand Se Parda Kijiye - From Aap Aye Bahaar Aayi",
    "Zara Phir Se Kehna - From Nayi Duniya Naye Log",
    "Phool Mangoon Na Bahar Mangoon - From Sawan Bhadon"
]
```

### Output:
The script will download the audio files:
- `Chand Se Parda Kijiye - From Aap Aye Bahaar Aayi.mp3`
- `Zara Phir Se Kehna - From Nayi Duniya Naye Log.mp3`
- `Phool Mangoon Na Bahar Mangoon - From Sawan Bhadon.mp3`

---

## License

This project is licensed under the MIT License. Feel free to use and modify it.

---

## About the Author

This project is developed by **Sudhanshu Kumar** (GitHub: [SudhuCodes](https://github.com/sudhucodes)). 


---

## Contact Information:  
Developed and maintained by **SudhuCodes**.  

- **GitHub:** [@sudhucodes](https://github.com/sudhucodes)  
- **Instagram:** [@sudhucodes](https://instagram.com/sudhucodes)  
- **YouTube:** [SudhuCodes YT Channel](https://www.youtube.com/@sudhucodes)  
- **Telegram**: [SudhuCodes TG Channel](https://t.me/sudhucodes)
- **Email:** [sudhuteam@gmail.com](mailto:sudhuteam@gmail.com)


Feel free to contribute, report issues, or suggest new features!