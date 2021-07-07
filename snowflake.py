import asyncio
import enum
import threading
import time


class WorkMode(enum.Enum):
    REALTIME = 1
    INCREMENT = 2


class AtomicInteger:
    def __init__(self, init_value: int = 0):
        self.value = init_value
        self.lock = threading.Lock()

    def increment(self, value: int = 1):
        with self.lock:
            self.value += value
            return self.value

    def get(self):
        with self.lock:
            return self.value


incrementBase = 0x2000
base62DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def base62(source: int):
    str_builder = []
    while source > 0:
        str_builder.append(base62DIGITS[source % 62])
        source = int(source / 62)
    str_builder = str_builder[::-1]
    return "".join(str_builder)


class Snowflake:
    def __init__(
            self,
            node_id: int = 0,
            update_rate: float = 0.016,
            work_mode: WorkMode = WorkMode.INCREMENT,
            increment_length: int = 7,
    ):
        self.node_id = node_id
        self.update_rate = update_rate
        self.work_mode = work_mode
        self.increment_length = increment_length
        self._timestamp = int(time.time() * 1000) << (increment_length + 13) & 0x7f_ff_ff_ff_ff_ff_ff_ff
        self.seed = AtomicInteger(self.node_id & 0x1fff | self._timestamp)

    async def update(self):
        while True:
            if self.work_mode == WorkMode.REALTIME:
                timestamp = int(time.time() * 1000) << (self.increment_length + 13) & 0x7f_ff_ff_ff_ff_ff_ff_ff
                if self.seed.get() < timestamp - 1 << 13:
                    self.timestamp = timestamp
            elif self.work_mode == WorkMode.INCREMENT:
                self.timestamp += 1 << (self.increment_length + 13)
            await asyncio.sleep(self.update_rate)

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self._timestamp = value
        self.seed = AtomicInteger(self.node_id & 0x1fff | value)

    @property
    def id(self):
        return self.seed.increment(incrementBase)

    @property
    def id_str(self):
        return base62(self.id)


snowflake = Snowflake()
