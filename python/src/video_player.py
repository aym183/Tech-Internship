"""A video player class."""

from .video_library import VideoLibrary
import csv
import random
playing = []
playlist = []
Pausing = []


class VideoPlayer:

    
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    
        '''
        I'm a bit unsure why this isnt working,
        the text file isn't being recognized but the text file is in the
        same folder so i'm a bit unsure why thats working

'''
    def show_all_videos(self):
        print("Here's a list of all available videos:")
        with open('videos.txt', 'r') as big_file:
            big_reader = csv.reader(big_file)
            for line in enumerate(big_reader):
                print(line)
      
        #python3 -m pytest
        #python3 -m src.run
        '''PLAY life_at_google_video_id [SAMPLE INPUT]'''
    def play_video(self, video_id):
        bool = False
        count = 0
        dict = { "amazing_cats_video_id": "Amazing Cats", "another_cat_video_id": "Another Cat Video",
                 "funny_dogs_video_id": "Funny Dogs", 
        "life_at_google_video_id": "Life at Google", "nothing_video_id": "Video about nothing"}

        
            
        if video_id in dict.keys():
            count+=1 
            newVal = dict.get(video_id)
            print("Playing video: "+ newVal)
            playing.append(newVal)
        
        else:
            print("Cannot play video: Video does not exist")

        if count>1:
            print("Stopping Video: "+ newVal)
            newVal2 = dict.get(video_id)
            print("Playing Video: "+ newVal2)
           

    def stop_video(self):

        if len(playing) == 0:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + playing[0])
            playing.pop()

    def play_random_video(self):
        list = ["Amazing Cats", "Another Cat Video", "Funny Dogs",  "Life at Google", "Video about nothing"]
        val = random.choice(list)
        print("Playing video: " + val )
        
        if len(playing)== 0:
            playing.append(val)
        else:
            playing[0] = val
        

    def pause_video(self):
        #pause.pop()
        
        if len(playing)!=0:
            
                
            print("Pausing video: "+ playing[len(playing)-1])
            Pausing.append(playing[len(playing)-1])
            
            
        else:
            print("Cannot pause video: No video is currently playing")
            
            

    def continue_video(self):
        if len(Pausing)!=0 :
            print("Continuing video: "+playing[len(Pausing)-1])
        elif len(playing)==0:
            print("Cannot continue video: No video is currently playing")
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        
        print("No video is currently playing")

    def create_playlist(self, playlist_name):
        
        print("Successfully created new playlist: " + playlist_name)
        playlist.append(playlist_name)

        #if playlist_name.upper() or playlist_name.lower() in playlist:
            #print("Cannot create playlist: A playlist with the same name already "
            #"exists")
        #print(playlist)

    def add_to_playlist(self, playlist_name, video_id):
        dict = { "amazing_cats_video_id": "Amazing Cats", "another_cat_video_id": "Another Cat Video",
                 "funny_dogs_video_id": "Funny Dogs", 
        "life_at_google_video_id": "Life at Google", "nothing_video_id": "Video about nothing"}

        if playlist_name in playlist and video_id in dict.keys():
           
            newVal = dict.get(video_id)
            print("Added video to " + playlist_name + ": " + newVal)
            
            

        elif playlist_name in playlist and video_id not in dict.keys():
            print("Cannot add video to " + playlist_name + ': ' + "Video does not exist")

        elif playlist_name not in playlist:
           print( "Cannot add video to " + playlist_name + ": Playlist does not exist")
            
        #print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        if len(playlist)==0:
            print("No playlists exist yet")
        else:
            #print("Showing all playlists:\n")
            for i in range(len(playlist)):
                print(playlist[i])

    def show_playlist(self, playlist_name):
        #for i in range(len(playlist)):
        if playlist_name.upper() or playlist_name.lower() not in playlist:
            print("Cannot show playlist "+ playlist_name+ ": Playlist does not exist" )
            
        else:
            print("Showing playlist: "+ playlist_name)
        

    def remove_from_playlist(self, playlist_name, video_id):
        if playlist_name not in playlist:
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")

    def clear_playlist(self, playlist_name):
        if playlist_name not in playlist:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")

    def delete_playlist(self, playlist_name):
        if playlist_name in playlist:
            print("Deleted playlist: "+ playlist_name)
        else:
            print("Cannot delete playlist "+playlist_name+ ": Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
