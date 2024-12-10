class Video:

    def __init__(self, title:str, duration:int, time_now:int=0, adult_mode:bool=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}. Продолжительность: {self.duration}. Возрастное ограничение: {"Есть" if self.adult_mode else "Нет"}'

    def __repr__(self):
        return f'{self.title}. Продолжительность: {self.duration}. Возрастное ограничение: {"Есть" if self.adult_mode else "Нет"}'
