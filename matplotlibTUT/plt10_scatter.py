# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 10 - scatter
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
#loc:float =0概率分布的均值，对应着整个分布的中心center
#scale:float =1概率分布的标准差，对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高
#size:int or tuple of ints =n 
#我们更经常会用到np.random.randn(size)所谓标准正太分布（μ=0, σ=1），对应于np.random.normal(loc=0, scale=1, size)
T = np.arctan2(Y, X)    # for color later on 加上是为了散点颜色好看　　

plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks隐藏xticks的值
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()
