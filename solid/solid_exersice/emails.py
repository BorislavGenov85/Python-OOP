from abc import ABC, abstractmethod


class HumanProtocol(ABC):
    def __init__(self, human):
        self.human = human

    @abstractmethod
    def format_protocol(self):
        ...


class ImProtocol(HumanProtocol):

    def format_protocol(self):
        return ''.join(["I'm ", self.human])


class BaseProtocol(HumanProtocol):

    def format_protocol(self):
        return self.human


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):

    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class MyContent(IContent):

    def format(self):
        return ''.join(['<MyML>', self.text, '</MyML>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: HumanProtocol):
        self.__sender = sender.format_protocol()

    def set_receiver(self, receiver: HumanProtocol):
        self.__receiver = receiver.format_protocol()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


myml = MyMl('Hello, there!')
sender = ImProtocol('qmal')
reciver = ImProtocol('james')
email = Email('IM')
email.set_sender(sender)
email.set_receiver(reciver)
email.set_content(myml)
print(email)

sender = ImProtocol('qmal')
reciver = ImProtocol('james')
email = Email('IM')
email.set_sender(sender)
email.set_receiver(reciver)
content = MyContent('Hello, there!')
email.set_content(content)
print(email)

sender = BaseProtocol('qmal')
reciver = BaseProtocol('james')
email = Email('IM')
email.set_sender(sender)
email.set_receiver(reciver)
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
