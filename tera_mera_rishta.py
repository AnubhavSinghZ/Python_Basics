import time
import sys

# The lyrics stored as a list of dictionaries with custom delays (in seconds)
lyrics = [
    {"line": "Tera yakeen kyun maine kiya nahin?", "delay": 3.9},
    {"line": "Tujhse raha kyun juda?", "delay": 3.8},
    {"line": "Mujh pe yeh zindagi karti rahi sitam", "delay": 6.0},
    {"line": "Tune hi di hai panah...", "delay": 3},
    {"line": "\nTera-mera rishta purana", "delay": 10.7},
    {"line": "Tera-mera rishta purana", "delay": 10.7},
    {"line": "Tera-mera rishta purana", "delay": 10.7}
]

def play_song_lyrics():
    print("--- Playing Lyrics: Tera Mera Rishta Purana ---\n")
    
    for item in lyrics:
        # Print character by character for a smooth typing effect
        for char in item["line"]:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)  # Speed of typing individual characters
            
        # Pause at the end of the line before moving to the next one
        time.sleep(item["delay"])
        print() # New line

if __name__ == "__main__":
    play_song_lyrics()