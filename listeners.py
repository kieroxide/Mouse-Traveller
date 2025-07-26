import pyautogui
import pynput

def start_mouse_listeners(conn):
    def on_click(x, y, button, pressed):
        if pressed:
            msg = f"Button: {button} pressed"
        else:
            msg = f"Button: {button} released"
        conn.sendall(msg.encode())

    def on_scroll(x, y, dx, dy):
        msg = f"Scroll: dx: {dx}, dy: {dy}"
        conn.sendall(msg.encode())



    with pynput.mouse.Listener(
        on_click=on_click,  
        on_scroll=on_scroll,
        #on_move=on_move
    ) as listener:
        listener.join()
