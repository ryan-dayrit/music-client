from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    def __init__(self, conf):
        self._config = conf

    @abstractmethod
    def get_album_list(self):
        pass