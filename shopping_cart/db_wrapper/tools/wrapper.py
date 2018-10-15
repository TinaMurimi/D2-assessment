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


class DMLQuery(DBWrapper):
    def __init__(self, connection):
        super().__init__()
        self.conn = connection

        if not self.conn:
            raise ValueError("No DB connection provided")

    def create(self):
        """
        Insert a new record in a DB table
        """
        pass

    def read(self):
        """
        Insert a new record in a DB table
        """
        pass

    def update(self):
        """
        Insert a new record in a DB table
        """
        pass

    def delete(self):
        """
        Insert a new record in a DB table
        """
        pass
