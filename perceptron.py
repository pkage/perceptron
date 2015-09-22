#! /usr/bin/env python

# Patrick Kage, 2015
# following Daniel Shiffman's book The Nature of Code


import os, random, graphics

class Perceptron:
	weights = [];
	inputs = [];
	learning_constant = 1;

	def __init__(self):
		self.weights = [];
		self.inputs = [];
		# grab some random numbers for some weights
		for i in range(0, 3):
			self.weights.append( 2 * random.random() - 1);

	def feed_forward(self, inputs):
		final_sum = 0;
		for i in range(0, len(self.weights)):
			final_sum += inputs[i] * self.weights[i];
		return (1 if final_sum > 0 else -1);

	def train(self, inputs, desired):
		guess = self.feed_forward(inputs);
		error = desired - guess;
		for i in range(0, len(self.weights)):
			self.weights[i] += self.learning_constant * error * inputs[i];
		
