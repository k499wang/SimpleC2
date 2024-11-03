from cli.shell import MyShell
import socket
import threading

def socket_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5) # 5 Connections maximum.
    print("Socket listening on port 9999")


    client_socket, addr = server_socket.accept()
    if addr[0] not in ['0.0.0.0', '127.0.0.1']:
        print(f"Rejected connection from {addr}")
        client_socket.close()
        
    data = client_socket.recv(1048).decode('utf-8')
    

    print(f"Data received!, check tasks")
        
    client_socket.send("Data received".encode('utf-8'))
    client_socket.close()

if __name__ == '__main__':
    listener_thread = threading.Thread(target=socket_listener)
    listener_thread.daemon = True
    listener_thread.start()
    
    MyShell().cmdloop()
        