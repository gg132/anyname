class TimeSeries(object):
	'''my changes'''
	def __init__(self,data):
		self.data = data
		
	def get(self,x):
		'''Find the corresponding y-value when given an x-value'''

		for (xi,yi) in self.data:
			if xi == x:
				return yi
				
		raise Exception("Didn't find the value")

    

class StepFunctionTimeSeries(TimeSeries):
	'''other changes'''
	'''more changes'''
    def get(self, x):
        closest_point = None
        for (xi, yi) in self.data:
            if closest_point is None:
                closest_point = (xi, yi)
            else:
                cx, cy = closest_point
                if abs(xi-x) < abs(cx-x):
                    closest_point = (xi, yi)
        return closest_point[1]
