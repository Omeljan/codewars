ind = x.count("good") 
if ind == 2 or ind == 1:
	return 'Publish!'
elif ind > 2:
 	return 'I smell a series!'
else:
	return 'Fail!'
