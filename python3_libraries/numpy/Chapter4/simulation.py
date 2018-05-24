from __future__ import print_function
import numpy as np

o, h, l, c = np.loadtxt('BHP.csv', delimiter=',', usecols=(3, 4, 5, 6), unpack=True)

def calc_profit(open, high, low, close):
   #buy just below the open
   buy = open * 0.999

   # daily range
   if low <  buy < high:
      return (close - buy)/buy
   else:
      return 0

func = np.vectorize(calc_profit)
profits = func(o, h, l, c)
print("Profits", profits)

real_trades = profits[profits != 0]
print("Number of trades", len(real_trades), round(100.0 * len(real_trades)/len(c), 2), "%")
print("Average profit/loss %", round(np.mean(real_trades) * 100, 2))

winning_trades = profits[profits > 0]
print("Number of winning trades", len(winning_trades), round(100.0 * len(winning_trades)/len(c), 2), "%")
print("Average profit %", round(np.mean(winning_trades) * 100, 2))

losing_trades = profits[profits < 0]
print("Number of losing trades", len(losing_trades), round(100.0 * len(losing_trades)/len(c), 2), "%")
print("Average loss %", round(np.mean(losing_trades) * 100, 2))
