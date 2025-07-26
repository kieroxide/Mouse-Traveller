import pyautogui
import time
import socket
import listeners
import threading
X = 0
Y = 1

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("Local IP:", local_ip)

HOST = '0.0.0.0'
PORT = 50000

WIDTH, HEIGHT = pyautogui.size()
limits = [WIDTH - 1, HEIGHT - 1]
midpoints = [WIDTH // 2, HEIGHT // 2]

def main(conn):
    last_pos = pyautogui.position()
    while True:
        current_pos = pyautogui.position()
        dx = current_pos[X] - last_pos[X]
        dy = current_pos[Y] - last_pos[Y]
        msg = f"dx: {dx}, dy: {dy}"
        conn.sendall(msg.encode())
        if(current_pos[X] <= 0):
            pyautogui.moveTo(midpoints[X], midpoints[Y])
        last_pos = current_pos
        
        time.sleep(0.01)


def switch_cursor_to(client_name):
    pass

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Waiting for client...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            listener_thread = threading.Thread(target=listeners.start_mouse_listeners, args=(conn,))
            listener_thread.daemon = True
            listener_thread.start()
            main(conn)