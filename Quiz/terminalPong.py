# main.py
import os
import sys
import time
import threading
import multiprocessing
import tty
import termios
from ball import move_ball
from shared import ball_x, ball_y, paddle1_y, paddle2_y, PADDLE_SIZE

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_keypress():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def handle_input():
    while True:
        key = get_keypress().lower()
        if key == 'w' and paddle1_y.value > 1:
            paddle1_y.value -= 1
        elif key == 's' and paddle1_y.value < 16:
            paddle1_y.value += 1
        elif key == 'o' and paddle2_y.value > 1:
            paddle2_y.value -= 1
        elif key == 'l' and paddle2_y.value < 16:
            paddle2_y.value += 1

def draw_screen(width, height):
    while True:
        clear_screen()
        screen = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Draw borders
        for i in range(width):
            screen[0][i] = screen[-1][i] = '-'
        for i in range(height):
            screen[i][0] = screen[i][1] = '|'
        
        # Draw paddles
        for i in range(PADDLE_SIZE):
            screen[paddle1_y.value + i][2] = '|'
            screen[paddle2_y.value + i][width - 3] = '|'
        
        # Draw ball
        screen[ball_y.value][ball_x.value] = 'O'
        
        # Print screen
        sys.stdout.write('\n'.join(''.join(row) for row in screen) + '\n')
        sys.stdout.flush()
        time.sleep(0.01)

def main():
    height, width = 20, 50
    
    ball_process = #Multi process solution here
    ball_process.start()
    
    input_thread = #threaded solution here
    input_thread.start()
    
    try:
        draw_screen(width, height)
    except KeyboardInterrupt:
        pass
    finally:
        ball_process.terminate()

if __name__ == "__main__":
    main()