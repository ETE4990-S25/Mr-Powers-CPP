# ball.py
import time
from shared import ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y, PADDLE_SIZE

def move_ball(height, width):
    while True:
        time.sleep(0.1)  # Control ball speed
        
        ball_x.value += ball_dx.value
        ball_y.value += ball_dy.value
        
        # Ball collision with top and bottom walls
        if ball_y.value <= 1 or ball_y.value >= height - 2:
            ball_dy.value *= -1
        
        # Ball collision with paddles
        if ball_x.value == 3 and paddle1_y.value <= ball_y.value <= paddle1_y.value + PADDLE_SIZE:
            ball_dx.value *= -1
        elif ball_x.value == width - 4 and paddle2_y.value <= ball_y.value <= paddle2_y.value + PADDLE_SIZE:
            ball_dx.value *= -1
        
        # Ball out of bounds (reset position)
        if ball_x.value <= 1 or ball_x.value >= width - 2:
            ball_x.value, ball_y.value = width // 2, height // 2
            ball_dx.value, ball_dy.value = -ball_dx.value, 1


