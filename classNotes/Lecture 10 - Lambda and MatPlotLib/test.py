import numpy as np
import time
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12,4)
N = 2**10
lwL = 2
lwr = 1
axRxlims = [0, N]
axRylim = [0, 160]
_t = np.linspace(0,N,N)
_y = (1+np.sin(5/N*2*np.pi*_t)) 
dfram = np.full(N+1, fill_value=np.nan, dtype=float)

t = np.tile(_t, (N,1))
y = np.tile(_y, (N,1))

for i in range(N):
    t[i,i+1:] = np.nan
    y[i,i+1:] = np.nan


# fig, ax = plt.subplots(figsize = (6,4), tight_layout=True)
# ax.set(xlabel= "distance(m)", ylabel="amplitude")
# ax.grid()
# ax.plot(t[-1], y[-1], lw=lwL)



# def getfigax():
#     fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout=True)
#     axL.set(xlabel= "distance(m)", ylabel="amplitude")
#     titL = axL.set_title("N=0")
    


    
fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout=True)
fig.suptitle("compleate")

for frame in range(N):
    axL.clear(), axR.clear()
    dfram[frame] = time.perf_counter()
    y2 = 1000*np.diff(dfram)
    y2_avg = np.nanmean(y2)

    # fig, ax = plt.subplots(figsize = (6,4), tight_layout=True)
    axL.set(xlabel= "distance(m)", ylabel="amplitude")
    axL.grid()
    axL.plot(t[-1], y[-1], lw=lwL)
    axL.set_title(f"n={frame}")
    axL.plot(t[frame], y[frame], lw=lwr)

    axR.set(xlabel= "distance(m)", ylabel="amplitude")
    axR.set_title(f"n={frame}")
    axR.grid()
    axR.plot(t[frame],y2, lw=lwr)
    fig.canvas.draw()

    plt.pause(0.00001)



    