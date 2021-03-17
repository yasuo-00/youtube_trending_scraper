
class Video():
    

    def __init__(video_title, video_link, video_duration, video_views):
        self.__video_title= video_title
        self.__video_link= video_link
        self.__video_duration = video_duration
        self.__video_views = video_views
    
    @property
    def video_title(self):
        return self.__video_title

    @property
    def video_link(self):
        return self.__video_link

    @property
    def video_duration(self):
        return self.__video_duration
    
    @property
    def video_views(self):
        return self.__video_views