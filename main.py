import yt_dlp

song_list = [
    "Chand Se Parda Kijiye - From Aap Aye Bahaar Aayi",
    "Zara Phir Se Kehna - From Nayi Duniya Naye Log",
    "Phool Mangoon Na Bahar Mangoon - From Sawan Bhadon"
]

def download_song(song_name):
    search_query = f"ytsearch:{song_name}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

def download_songs(song_list):
    for song in song_list:
        print(f"Downloading: {song}")
        download_song(song)

if __name__ == "__main__":
    download_songs(song_list)