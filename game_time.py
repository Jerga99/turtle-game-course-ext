
import time

class GameTime:
    delta_time: float = 0
    last_frame_time: float = 0

    @classmethod
    def init(cls):
        cls.last_frame_time = cls.get_time_now()

    @classmethod
    def get_time_now(cls):
        return time.time()

    @classmethod
    def process_time(cls):
        time_now = cls.get_time_now()
        cls.delta_time = time_now - cls.last_frame_time
        cls.last_frame_time = time_now



