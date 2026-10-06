import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	array = np.asarray(gradient)

	magnitude = np.sqrt((array**2).sum())
	if magnitude !=0:
		direction = array / magnitude
		descent = direction * (-1)
	else:
		direction = [0.0, 0.0]
		descent = [0.0, 0.0]
	
	dicionary = {'magnitude': magnitude, 'direction': direction, 'descent_direction': descent}
	return dicionary
	pass