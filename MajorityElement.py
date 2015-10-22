def majorityElement(self, nums):
    D = {}
    for n in nums:
        if n in D.keys():
            D[n] = D[n]+1
        else:
            D[n] = 1
            
        if D[n]> len(nums)/2.0:
            return n

        
def make_inc(n):
	def func(x):
		return x + n
	return func