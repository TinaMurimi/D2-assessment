from abc import ABC, abstractmethod


class DBWrapper(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        """
        Insert a new record in a DB table
        """
        raise NotImplementedError()

    @abstractmethod
    def read(self):
        """
        Insert a new record in a DB table
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self):
        """
        Insert a new record in a DB table
        """
        raise NotImplementedError()

    @abstractmethod
    def delete(self):
        """
        Insert a new record in a DB table
        """
        raise NotImplementedError()
