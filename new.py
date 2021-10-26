import matplotlib.pyplot as plt, numpy as np
x=np.linspace(0,30,200)
sin=np.sin(x)
cos=np.cos(x)
tan=np.tan(x)

plt.style.use('seaborn')
fig,ax=plt.subplots(3,1)
fig.suptitle("Trigonometric Curve\nby Shakil Mahmud",color='purple')
fig.tight_layout(pad=4)

ax[0].plot(x,sin,color='red',linewidth=0.5,label="sine")
ax[0].legend(loc='lower left')
ax[0].set_title("sine curve",color='red',size=10)
ax[0].set_xlabel("x axis",color='red',size=9)
ax[0].set_ylabel("y axis",color='red',size=9)

ax[1].plot(x,cos,color='green',linewidth=0.5,label="cosine")
ax[1].legend(loc='lower left')
ax[1].set_title("cosine curve",color='green',size=10)
ax[1].set_xlabel("x axis",color='green',size=9)
ax[1].set_ylabel("y axis",color='green',size=9)

ax[2].plot(x,tan,color='blue',linewidth=0.5,label="tangent")
ax[2].legend(loc='lower left')
ax[2].set_title("tangent curve",color='blue',size=10)
ax[2].set_xlabel("x axis",color='blue',size=9)
ax[2].set_ylabel("y axis",color='blue',size=9)

plt.show()

