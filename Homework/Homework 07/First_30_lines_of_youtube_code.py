import numpy as np
import time
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12,4)
N = 2**10
lwL = 2
lwr = 1
axRxlims = [0, N]
axRylim = [200, 600]
_t = np.linspace(0,N,N)
_y = (1+np.sin(5/N*2*np.pi*_t))
dframe = np.full(N+1, fill_value=np.nan, dtype=float)

t = np.tile(_t, (N,1))
y = np.tile(_y, (N,1))

for i in range(N):
    t[i,i+1:] = np.nan
    y[i,i+1:] = np.nan


# # fig, ax = plt.subplots(figsize = (6,4), tight_layout=True)
# # ax.set(xlabel= "distance(m)", ylabel="amplitude")
# # ax.grid()
# # ax.plot(t[-1], y[-1], lw=lwL)

  



fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout=True)
fig.suptitle("compleate")

for frame in range(N):
    axL.clear(), axR.clear()
    dframe[frame] = time.perf_counter()
    y2 = 1000*np.diff(dframe)
    y2_avg = np.nanmean(y2)

  
    axL.set(xlabel= "distance(m)", ylabel="amplitude")
    axL.set_title(f"n={frame}")
    axL.grid()
    axL.plot(t[frame], y[frame], lw=lwr)

    axR.set(xlabel= "frame Number", ylabel="Frame time (ms)")
    axR.set_title(f"Avg = {y2_avg:.1f} ms ({1000/y2_avg:.1f} fps)")
    axR.set_xlim(axRxlims)
    axR.set_ylim(axRylim)
    axR.grid()
    axR.plot(t[frame],y2, lw=lwr)
    fig.canvas.draw()

    plt.pause(0.000001)



# You will need to install mplcursors for this example and run it as a py file
# import matplotlib.pyplot as plt
# import mplcursors
# import numpy as np

# # Sample data
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# # Create the plot
# fig, ax = plt.subplots()
# ax.plot(x, y)

# # Add interactive cursors
# mplcursors.cursor(ax, hover=True)

# # Add title and labels
# plt.title('Interactive Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # Display the plot
# plt.show()
