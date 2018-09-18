import socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind(("", 8080))
tcp_sock.listen(128)
new_socket, cli_addr = tcp_sock.accept()
while True:
    recv_data = new_socket.recv(1024)
    print("recv_data = ", recv_data.decode())
    new_socket.send("ok\n".encode())
new_socket.close()
tcp_sock.close()
