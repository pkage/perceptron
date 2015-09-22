#! /usr/bin/env python

# Perceptron training gym
# Patrick Kage 2015

import perceptron, random
from graphics import *

class Trainer():
	inp = []
	ans = 0;

	def __init__(self, x,y,ans):
		self.ans = ans;
		self.inp = [x,y,1]; # bias input built in


class GraphLine():

	def __init__(self, slope, yint):
		self.slope = slope;
		self.yint = yint;

	def f(self, x):
		return (self.slope * x) + self.yint;

def train(learning_constant=1,trials=2000):
	# get a window to draw stuff in (800x600)
	win = GraphWin("perceptron", 800, 600, autoflush=False);
	win.setCoords(-400, -300, 400, 300);

	# create a target line
	target = GraphLine(2, 1);

	# render the target line
	target_line = Line(Point(-400, target.f(-400)), Point(400, target.f(400)));
	target_line.setWidth(3);
	target_line.setFill('gray');
	target_line.draw(win);
	win.update();

	# declare our node and trainer list
	node = perceptron.Perceptron();
	trainers = [];


	# populate the trainer list
	for i in xrange(0, trials):
		x = (random.random() * win.width) - (win.width/2);
		y = (random.random() * win.height) - (win.height/2);
		trainers.append(Trainer(x, y, (1 if target.f(x) > y else -1)));

	# set the learning constant
	node.learning_constant = learning_constant;

	# woo! training time
	reps = 0;
	for trainer in trainers:
		circ = Circle(Point(trainer.inp[0], trainer.inp[1]), 2);
		node.train(trainer.inp, trainer.ans);
		guess = node.feed_forward(trainer.inp);
		circ.setFill('blue' if 1 == guess else 'red');
		circ.draw(win);
		win.update();
		reps += 1;
		print("Cycle: " + str(reps) + "/" + str(trials));

	
	win.update();

	node.train(trainer.inp, trainer.ans);

	
	win.getMouse();

if __name__ == "__main__":
	train(learning_constant=0.01);
