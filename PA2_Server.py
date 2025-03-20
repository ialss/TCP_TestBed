
print( 'Server program started.' )
# Import socket package.


from socket import *

# Initialise important variables.
address = 'localhost'
port_number = 12005
identifier = ( address , port_number )


# Create and bind server socket.
server_socket = socket( AF_INET , SOCK_STREAM )
server_socket.bind( identifier )
print( 'Server socket created and bound at:' , identifier )


# Have the server listen for (upto 5) connections.
server_socket.listen( 5 )
print( 'Server socket is now listening for connections.' )

# Loop.
is_looping = True
while is_looping:
    
    
    # Accept a new connection.
    connection_socket , client_address = server_socket.accept()
    print( 'Server created connection socket for client at:' , client_address )

    # Get message from client.
    message_from_client = connection_socket.recv( 2048 )
    print( 'Server received message from client at:' , client_address )

    # Convert message to string.
    old_string = message_from_client.decode()
    print( 'Received string:' , old_string )

    # Check if message is kill command.
    if 'kill' == old_string.lower():
        print( 'Kill command given!' )

        # Modify string.
        new_string = 'Killed!'

        # End loop.
        is_looping = False
    else:
        
    
        # Modify string.
        new_string = old_string.upper()
    
    #Creates a string list delimitting via "-"
    string_list = new_string.split("-")

    # converts each string to an integer
    def stringToInt(str):
        return int(str)
    string_list = list(map(stringToInt, string_list))


    #sums all the integers
    newInt = 0
    for x in string_list:
        newInt = newInt + x
    
    #creates a new finalized string
    newStr = "RESULT:" + str(newInt)
    
    # Convert modified string to message.
    message_to_client = newStr.encode()
    print( 'Sent string:' , newStr )

    # Send message to client.
    connection_socket.send( message_to_client )
    print( 'Server sent message to client at:' , client_address )

    # Close the connection socket.
    connection_socket.close()
    print( 'Server closed connection socket for client at:' , client_address )

# Close the server socket.
server_socket.close()
print( 'Server socket closed.' )
print( 'Server program terminated.' )

