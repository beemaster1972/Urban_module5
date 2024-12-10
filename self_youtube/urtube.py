from .user import User
from .video import Video
from time import sleep

class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, nickname, password):
        user = self.users.get(nickname)
        if user and user.check_password(password):
            self.current_user = user
            return True
        else:
            return False

    def register(self, nickname, password, age):
        user = User(nickname,password,age)
        if not self.users.get(user.nickname):
            self.users[nickname] = user
            self.current_user = user
        else:
            print(f'Пользователь {nickname} уже существует')


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            if isinstance(arg,(list,tuple,set)):
                for video in arg:
                    if isinstance(video, Video):
                        if video.title not in self.videos:
                            self.videos[video.title] = video
            elif isinstance(arg, Video):
                if arg.title not in self.videos:
                    self.videos[arg.title] = arg

    def get_videos(self, search:str) -> list:
        search = search.upper()
        result = [video for title, video in self.videos.items() if title.upper().find(search)+1]
        return result

    def watch_video(self,title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = self.videos.get(title)
        if video:
            if (video.adult_mode and self.current_user.age<18):
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            for _ in range(1, video.duration+1):
                print(_,end=' ')
                sleep(1)
            print('Конец видео')


