
from functools import wraps, partial

def debug(func=None,*,prefix=''):
	if func is None:
		return partial(debug, prefix=prefix)
	msg = prefix + func.__qualname__

	@wraps(func)
	def wrapper(*args,**kwargs):
		print(msg)
		return func(*args, **kwargs)
	return wrapper

def debugmethods(cls):
	# called when class initialized
	for key, val in vars(cls).items():
		print(f"key:{key},val: {val}")
		if callable(val):
			# if val is callable function
			setattr(cls, key, debug(val))
			# assign debug attribute to 
	return cls