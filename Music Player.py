import pygame
import os
import shutil

pygame.init()

def create_playlist(playlist_name):
    playlist_path = os.path.join("playlists", playlist_name)
    if not os.path.exists(playlist_path):
        os.makedirs(playlist_path)
    return playlist_path

def add_song_to_playlist(playlist_path, song_path):
    song_name = os.path.basename(song_path)
    destination_path = os.path.join(playlist_path, song_name)
    shutil.copy(song_path, destination_path)

# Function to play a playlist
def play_playlist(playlist_path):
    pygame.mixer.init()
    pygame.mixer.music.load(playlist_path)
    pygame.mixer.music.play()

def main():
    while True:
        print("\nSimple Music Player Menu:")
        print("1. Create Playlist")
        print("2. Add Song to Playlist")
        print("3. Play Playlist")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            playlist_name = input("Enter the playlist name: ")
            playlist_path = create_playlist(playlist_name)
            print(f"Playlist '{playlist_name}' created in 'playlists' directory.")

        elif choice == "2":
            playlist_name = input("Enter the playlist name: ")
            song_path = input("Enter the path to the MP3 song file: ")
            playlist_path = os.path.join("playlists", playlist_name)
            if os.path.exists(playlist_path):
                add_song_to_playlist(playlist_path, song_path)
                print(f"Song added to '{playlist_name}' playlist.")
            else:
                print(f"Playlist '{playlist_name}' does not exist.")

        elif choice == "3":
            playlist_name = input("Enter the playlist name to play: ")
            playlist_path = os.path.join("playlists", playlist_name)
            if os.path.exists(playlist_path):
                play_playlist(playlist_path)
                pygame.mixer.music.set_endevent(pygame.USEREVENT)
                pygame.mixer.music.play()
                pygame.event.wait()
            else:
                print(f"Playlist '{playlist_name}' does not exist.")

        elif choice == "4":
            pygame.mixer.quit()
            pygame.quit()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
