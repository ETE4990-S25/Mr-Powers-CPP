import time
import numpy as np
import scipy as sp
import multiprocessing as mp
import matplotlib.pyplot as plt
from scipy import fft


def createplot():
    """ Create the plot and return the fig, axes, lines, and text"""
    fig, (axL, axR) = plt.subplots(
        figsize=(12, 4), constrained_layout=True, ncols=2)
    axL.set_xlim([x[0], x[-1]]), axR.set_xlim([0, 10])
    axL.set_ylim([0, 1.1]), axR.set_ylim([0, 0.5])
    axL.set(xlabel="x", ylabel="y")
    axR.set(xlabel="k", ylabel="FFT(y)")

    lineL, = axL.plot([], [])
    lineR, = axR.plot([], [])

    txt = axL.text(0.01, 0.99, "", ha="left",
                   va="top", transform=axL.transAxes)

    return fig, axL, axR, lineL, lineR, txt


def datagen(x):
    """Generate some y data for a given x. Note how the data will depend on the
    time.perf counter"""
    y = np.exp(-(x - 5 + np.sin(2*np.pi*0.1*time.perf_counter()))**2/(0.1)**2)
    y += 0.5 * np.exp(-(x - 5 + 5*np.cos(2*np.pi*0.5 *
                      time.perf_counter()))**2/(2)**2)
    y += 0.1 * np.sin(2 * np.pi *
                      (5 + 2*np.cos(2*np.pi*0.125*time.perf_counter())) * x)
    y += np.random.normal(loc=0, scale=0.05, size=N)
    y /= np.max(y)

    return y


def operation(x: np.ndarray, y: np.ndarray):
    """The operation to perform on the data"""
    time.sleep(np.random.uniform(0.1, 0.2))
    f = np.linspace(0, 1/(x[1]-x[0]), len(x))
    ffty = sp.fft.fft(y)
    return (f, ffty)


N = 512
x = np.linspace(0, 10, N)
Nframes = 300

### Without multiprocessing ####
# if __name__ == "__main__":

#     fig, axL, axR, lineL, lineR, txt = createplot()
#     fig.suptitle("Without Multiprocessing")
#     def update(frame):
#         y = datagen(x)
#         f, ffty = operation(x, y)
#         lineL.set_data(x, y)
#         lineR.set_data(f, np.abs(ffty)/N)

#     for frame in range(Nframes):
#         update(frame)
#         fig.canvas.update()
#         fig.canvas.flush_events()
#         plt.pause(0.00001)


class Processor(mp.Process):
    """ Class to process the data"""

    def __init__(self, inqueue, outqueue):
        self.inqueue, self.outqueue = inqueue, outqueue
        super().__init__()

    def run(self):
        while True:
            if self.inqueue.qsize() > 0:
                indata = self.inqueue.get()
                outdata = operation(indata["x"], indata["y"])
                self.outqueue.put({"ts": indata["ts"],
                                   "f": outdata[0],
                                   "ffty": outdata[1]})
            time.sleep(0.0001)


### With multiprocessing ####
if __name__ == "__main__":

    FPS = 30

    inqueue, outqueue = mp.Queue(), mp.Queue()
    PROCESSORS = mp.cpu_count()
    procs = [Processor(outqueue, inqueue) for i in range(PROCESSORS)]
    for proc in procs:
        proc.start()

    fig, axL, axR, lineL, lineR, txt = createplot()
    fig.suptitle("With Multiprocessing")

    txt2 = axR.text(0.99, 0.99, "", ha="right",
                    va="top", transform=axR.transAxes)

    t_start = time.perf_counter()
    t_next = time.perf_counter() + 1/FPS
    t_last = time.perf_counter()

    def update(frame):
        global t_last
        y = datagen(x)
        outqueue.put({"ts": time.perf_counter(), "x": x, "y": y})

        REPLOT = False
        txt2.set_text(f"qsize = {inqueue.qsize()}")
        while(inqueue.qsize() > 0):  # consuming the queue
            qdata = inqueue.get()
            if qdata["ts"] > t_last:
                data = qdata
                REPLOT = True

        if REPLOT:
            txt.set_text(f"t = {data['ts'] - t_start:.2f} s")
            t_last = data["ts"]
            f, ffty = data["f"], data["ffty"]
            lineL.set_data(x, y)
            lineR.set_data(f, np.abs(ffty)/N)

    plt.pause(0.1)
    for frame in range(Nframes):
        while time.perf_counter() < t_next:
            plt.pause(0.00001)
        t_next = time.perf_counter() + 1/FPS
        update(frame)
        fig.canvas.draw()
        fig.canvas.flush_events()
