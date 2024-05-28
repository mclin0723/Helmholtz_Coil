from matplotlib import pylab
from matplotlib import pyplot as plt
import numpy as np
from pylab import *
import csv
import scipy.constants as con

matplotlib.font_manager.fontManager.addfont('NotoSansTC-Regular.otf')
matplotlib.rcParams['font.sans-serif'] = 'Noto Sans TC'
matplotlib.rcParams['font.family'] = 'sans-serif'
# 修復負號顯示問題
plt.rcParams['axes.unicode_minus']=False

u0 = con.mu_0
n = 200
i = 2
r = 10.25

d1 = 5/2
d2 = 10.25/2
d3 = 15/2

x = np.linspace(-15, 15, 31)

B_1_R = (u0*n*i*r**2)/(2*((x+d1)**2+r**2)**(3/2))

B_1_L = (u0*n*(i)*r**2)/(2*((x-d1)**2+r**2)**(3/2))

B_1_t = abs(B_1_R + B_1_L)

B_2_R = (u0*n*i*r**2)/(2*((x+d2)**2+r**2)**(3/2))

B_2_L = (u0*n*(i)*r**2)/(2*((x-d2)**2+r**2)**(3/2))

B_2_t = abs(B_2_R + B_2_L)

B_3_R = (u0*n*i*r**2)/(2*((x+d3)**2+r**2)**(3/2))

B_3_L = (u0*n*(i)*r**2)/(2*((x-d3)**2+r**2)**(3/2))

B_3_t = abs(B_3_R + B_3_L)
#自造圖表
fig, axes = plt.subplots(1, 1, figsize = (8,4), facecolor='w')

axes.set_facecolor("gray")

# axes.scatter(tIme, intercept, s = 0.5, c = 'r', marker = ',')

plt.plot(x, B_3_R, linewidth = 2, color = 'g')
plt.plot(x, B_3_L, linewidth = 2, color = 'r')
plt.plot(x, B_3_t, linewidth = 2, color = 'b')

# #圖例
# plt.legend(['溫度'], loc='upper right')
# axes.set_title('溫度變化')
# axes.set_xlabel("結晶時間(hr)")
# axes.set_ylabel("溫度(℃)")
# plt.axis([0, 100, 26, 30])
# plt.grid(True)

#圖例
plt.legend(['左線圈磁場', '右線圈磁', '總磁場'], loc='upper right')
axes.set_title('相距15cm雙線圈磁場分佈')
axes.set_xlabel("與線圈中心距離(cm)")
axes.set_ylabel("磁場強度(T)")
plt.axis([-15, 15, -0.0000, 0.00005])
plt.grid(True)

#格線在後
axes.set_axisbelow(True)

savefig("H_15")
plt.show()