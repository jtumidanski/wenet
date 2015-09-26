import threading

from antlr4 import *

from event_hook import EventHook
from antlr_filter.filter_messageLexer import filter_messageLexer
from antlr_filter.filter_messageParser import filter_messageParser
from antlr_filter.filter_message_visitor import filter_message_visitor


class SocketClient(threading.Thread):
    def __init__(self, thread_id, connection):
        super().__init__()

        self._connection = connection
        self._connected = True
        self.connection_open = EventHook()
        self.connection_closed = EventHook()
        self.end_character = bytes(chr(93), 'UTF-8')
        self.message_received = EventHook()
        self.start_character = bytes(chr(91), 'UTF-8')
        self.thread_id = thread_id
        self._filter_tree = None

    def destined_for_me(self, socket_message):
        # Using the filter set, determine if the message is destined for the client.
        visitor = filter_message_visitor(socket_message)
        return visitor.visit(self._filter_tree)

    def disconnect(self):
        # Close the connection and fire the connection closed event.
        self._connection.close()
        self.connection_closed.fire(self)

    def run(self):
        self.set_filter("1")

        # Fire the connection open event.
        self.connection_open.fire(self)

        # Try to read from the socket connection.
        try:
            read_buffer = bytearray()

            # Read from the connection until instructed not to.
            while self._connected:
                # Read a singular byte from the socket.
                socket_byte = self._connection.recv(1)

                # If nothing was read from the socket. The socket likely closed.
                if not socket_byte:
                    self.disconnect()
                    return

                if socket_byte == self.start_character:
                    # If the byte read is the start character. Clear the buffer.
                    read_buffer = bytearray()
                elif socket_byte == self.end_character:
                    # If the byte read is the end character. Send the message.
                    self.message_received.fire(self, read_buffer.decode('UTF-8'))
                    read_buffer = bytearray()
                else:
                    # Any other character simply append to the buffer.
                    read_buffer.extend(socket_byte)
        # If there is an OS error exit.
        except OSError:
            pass

    def set_filter(self, filter_message):
        # Set the filter for the client. Use the new filter to build a parse tree.
        input_string = InputStream(filter_message)
        lexer = filter_messageLexer(input_string)
        stream = CommonTokenStream(lexer)
        parser = filter_messageParser(stream)
        self._filter_tree = parser.prog()

    def send_message(self, message):
        # Translate the message to bytes and send the message.
        bytes_to_send = bytes(str(message), 'UTF-8')
        self._connection.send(bytes_to_send)
