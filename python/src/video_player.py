"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._paused_video  = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)
        print("Here's a list of all available videos:")

        for video in all_videos:
            tags_string=" ".join(video.tags)
            print(f"{video.title} ({video.video_id}) [{tags_string}]")

    def play_video(self, video_id):
             
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
        elif self._current_video is not None :
            self.stop_video()
            print(f"Playing video: {video.title}")
            self._current_video = video
        elif self._paused_video is self._current_video:
            print(f"Playing video: {video.title}")
            self._paused_video = None
            self._current_video = video
        else:
            print(f"Playing video: {video.title}")
            self._current_video = video


    def stop_video(self):
        if self._current_video == None:
            print("Cannot stop video: No video is currently playing")
        else :
            print("Stopping video:", self._current_video.title)
            self._current_video = None
            self._paused_video = None

    def play_random_video(self):
        all_videos = self._video_library.get_all_videos()
        video = random.choice(all_videos) 
        if not self._current_video == None :
            print("Stopping video:", self._current_video.title)
            print("Playing video:",video.title)
            self._current_video = video
        else:
            print("Playing video:",video.title)
            self._current_video = video

    def pause_video(self):
        if self._paused_video is not None:
            print("Video already paused:", self._paused_video.title)
        elif not self._current_video == None :
            print("Pausing video:", self._current_video.title)
            self._paused_video = self._current_video
        else: 
            print("Cannot pause video: No video is currently playing")
        

    def continue_video(self):
        if self._paused_video is not None:
           print("Continuing video:", self._paused_video.title)
           self._paused_video=None
        elif self._current_video is not None:
           print("Cannot continue video: Video is not paused")
        else:
           print("Cannot continue video: No video is currently playing")  
        

    def show_playing(self):
        video = self._video_library.get_all_videos()
        
        if not self._current_video == None and self._paused_video == None:
            tags_string=" ".join(self._current_video.tags)
            print("Currently playing:",f"{self._current_video.title} ({self._current_video.video_id}) [{tags_string}]")
        elif not self._paused_video == None:
            tags_string=" ".join(self._current_video.tags)
            print("Currently playing:",f"{self._current_video.title} ({self._current_video.video_id}) [{tags_string }]" , "- PAUSED")
        else:
            # self._current_video = None
            print("No video is currently playing") 
        
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

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
