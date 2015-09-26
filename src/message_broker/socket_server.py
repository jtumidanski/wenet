import socket
import sys

from message_broker import socket_client


class SocketServer(object):
    def __init__(self, host, port):
        super().__init__()

        self._accept_connections = True
        self._host = host
        self._port = port
        self._socket = None
        self._clients = []

        for resources in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
            family, socket_type, protocol, canon_name, socket_address = resources

            try:
                self._socket = socket.socket(family, socket_type, protocol)
            except socket.error:
                self._socket = None
                continue
            try:
                self._socket.bind(socket_address)
                self._socket.listen(1)
            except socket.error:
                self._socket.close()
                self._socket = None
                continue
            break

        if self._socket is None:
            raise ConnectionError('Could not open socket.')

        thread_count = 0

        # Loop until told otherwise accepting client connections.
        while self._accept_connections:
            connection, address = self._socket.accept()
            connection.setblocking(True)

            print('Connected by', address)
            thread_count += 1
            client = socket_client.SocketClient(thread_count, connection)
            client.connection_open += self._client_connected
            client.message_received += self._send_message
            client.connection_closed += self._client_disconnected
            client.start()

    def _client_connected(self, sender_client):
        # A client has successfully started, add them to the list of clients.
        self._clients.append(sender_client)

    def _send_message(self, sender_client, message):
        # Loop through all the registered clients.
        for client in self._clients:
            # If the client is not the sender, and the clients filter allows it, send the message.
            if client.thread_id != sender_client.thread_id and client.destined_for_me(message):
                client.send_message(message)

    def _client_disconnected(self, sender_client):
        # Remove the client from the list of clients.
        self._clients.remove(sender_client)

    def disconnect(self):
        # Tell all clients a disconnect is necessary.
        for client in self._clients:
            client.disconnect()
        self._accept_connections = False


def main(argv):
    socket_server = SocketServer(argv[0], int(argv[1]))


if __name__ == '__main__':
    main(sys.argv[1:])
