s = set(['ABC', 'ARC', 'AGC', 'AHC'])
t = set([input() for _ in range(3)])
print((s - t).pop())
