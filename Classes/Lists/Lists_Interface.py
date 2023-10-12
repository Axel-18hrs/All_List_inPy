from abc import ABC, abstractmethod


class ListBase(ABC):

    @abstractmethod
    def add(self, value):
        raise NotImplementedError("function 'add' has not been implemented")

    @abstractmethod
    def delete(self, data):
        raise NotImplementedError("function 'delete' has not been implemented")

    @abstractmethod
    def transverse(self):
        raise NotImplementedError("function 'transverse' has not been implemented")

    @abstractmethod
    def transverse_reverse(self):
        raise NotImplementedError("function 'transverse_reverse' has not been implemented")

    @abstractmethod
    def exist(self, data):
        raise NotImplementedError("function 'exist' has not been implemented")

    @abstractmethod
    def show(self):
        raise NotImplementedError("function 'show' has not been implemented")

    @abstractmethod
    def search(self, data):
        raise NotImplementedError("function 'search' has not been implemented")


