# shared.py
import multiprocessing

PADDLE_SIZE = 4
ball_x = multiprocessing.Value('i', 40)
ball_y = multiprocessing.Value('i', 12)
ball_dx = multiprocessing.Value('i', 1)
ball_dy = multiprocessing.Value('i', 1)
paddle1_y = multiprocessing.Value('i', 10)
paddle2_y = multiprocessing.Value('i', 10)