import socket

def check_ssh():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect(("localhist", 22))
    except (socket.timeout, socket.error):
        return False
    return True
