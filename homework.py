import numpy as np
import matplotlib.pyplot as plt

# 随机游走模型，使用正态分布模拟价格变化
def simulate_random_walk(S0, steps, mu=0, sigma=1):
    prices = [S0]  # 初始化价格列表
    for _ in range(steps):
        step = np.random.normal(mu, sigma)  # 正态分布的随机步长
        prices.append(prices[-1] + step)  # 更新价格
    return prices

# 参数设置
S0 = 100  # 初始股票价格
steps = 100  # 模拟步数（天数）
mu = 0  # 平均回报率，假设为0
sigma = 20.9  # 波动率，假设为1

# 模拟随机游走
prices = simulate_random_walk(S0, steps, mu, sigma)

# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(prices, label='Random Walk Stock Price (Normal Distribution)')
plt.title('Stock Price Random Walk Simulation (Normal Distribution)')
plt.xlabel('Time Steps')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
