import matplotlib.pyplot as plt

from RandomWalks import RandomWalk

while True:

	rw = RandomWalk(10000)
	rw.fill_walk()

	plt.figure(dpi=128,figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c = point_numbers, 
		cmap = plt.cm.Blues, edgecolor='none', s = 11)

	plt.scatter(0, 0, c = 'red', edgecolor='none', s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)

	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	continue_running = input("Make another random walk? (y/n): ")
	if continue_running == 'n':
		break
