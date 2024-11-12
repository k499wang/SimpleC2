from cli.shell import MyShell
import socket
import threading
import time

def socket_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(1)
    
    while True:
        try:
            client_socket, addr = server_socket.accept()
            if addr[0] not in ['0.0.0.0', '127.0.0.1']:
                client_socket.close()
                continue  # Skip the rest of the loop for this client

            data = ""

            # Continuously receive data in chunks until all is received
            while True:
                chunk = client_socket.recv(1048).decode('utf-8')
                
                if chunk == '':  # If empty, connection was closed or no data received
                    break
                
                if chunk:  # If there is non-whitespace data, accumulate it
                    data += chunk
                else:
                    break  # Optional: break on empty data (if needed)

                # If data is received, print it
                if data:
                    print(f"Received data from {addr[0]}: {data}") # For debugging purposes only.

        except Exception as e:
            print("Error occurred:", e)

        finally:
            # Always close the client socket after handling the connection
            client_socket.close()

if __name__ == '__main__':
    listener_thread = threading.Thread(target=socket_listener)
    listener_thread.daemon = True
    listener_thread.start()
    
    time.sleep(5)
    
    MyShell().cmdloop()
        