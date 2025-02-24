from __future__ import annotations
from typing import List

class Email:
    def __init__(self, message: str, sender: Client, recipient: Client):
        self._message = message
        self._sender = sender
        self._recipient = recipient

    @property
    def message(self) -> str:
        return self._message

    @property
    def sender(self) -> Client:
        return self._sender;

    @property
    def recipient(self) -> Client:
        return self._recipient

class Server:
    def __init__(self):
        self._clients = {}

    def send(self, email: Email) -> None:
        email.recipient.inbox.append(email) 

    def register_client(self, client: Client) -> None:
        self._clients[client.name] = client

class Client:
    def __init__(self, server: Server, name: str):
        self._inbox = []
        self._server = server
        self._name = name
        self._server.register_client(self)

    @property
    def inbox(self) -> List[Email]:
        return self._inbox

    @property
    def name(self) -> str:
        return self._name

    def compose(self, message: str, recipient: Client) -> None:
        self._server.send(Email(message, self, recipient))

# Test cases
def test_email():
    server = Server()
    client_a = Client(server, 'Alice')
    client_b = Client(server, 'Bob')

    client_a.compose('Hello, World!', client_b)
    client_a.compose('CS 61A Rocks!', client_b)

    assert len(client_b.inbox) == 2
    assert client_b.inbox[0].message == 'Hello, World!'
    assert client_b.inbox[1].message == 'CS 61A Rocks!'
    assert client_b.inbox[0].sender.name == 'Alice'
    assert client_b.inbox[1].sender.name == 'Alice'

if __name__ == '__main__':
    try:
        test_email()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
