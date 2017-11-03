class Solution:
	@classmethod
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		n = len(nums1)
		m = len(nums2)
		count = 0
		evenList = True

		stopval = n+m
		if stopval % 2==1: 
			evenList = False
			stopval +=1
		else:
			stopval +=2
		stopval = int(stopval//2)

		# print('stopval',stopval)
		curr = 0
		while count < stopval:
			count+=1
			prev = curr
			if   len(nums1) == 0:
				curr = nums2.pop(0)
				continue
			elif len(nums2) == 0:
				curr = nums1.pop(0)
				continue
			
			if   nums1[0] > nums2[0]:
				curr = nums2.pop(0)
			elif nums1[0] <= nums2[0]:
				curr = nums1.pop(0)

		print('prev',prev,'curr',curr)
		if evenList:
			answer = (prev+curr)/2
		else: 
			answer = float(curr)
		print('ans',answer)
		return answer


def testAll():
	nums1 = [1,3]
	nums2 = [2]
	assert(Solution.findMedianSortedArrays(nums1,nums2)==2)
	
	nums1 = [1, 2]
	nums2 = [3, 4]
	assert(Solution.findMedianSortedArrays(nums1,nums2)==2.5)	
	nums1 = [1]
	nums2 = [1]
	assert(Solution.findMedianSortedArrays(nums1,nums2)==1)
	# assert(median(nums1,nums2)==1)
	print('passed')

if __name__ == "__main__":
	testAll()

'''
def median(A,B):
	m,n = len(A), len(B)
	if m > n:
		A, B, m, n = B, A, n, m
	if n == 0:
		raise ValueError

	imin, imax, half_len = 0, m, (m+n+1)/2

	while imin <= imax:
		i = (imin+imax)/2
		j = half_len -i
		if i < m and B[j-1] > A[i]:
			#i is too small, must increase it
			imin = i -1
		elif i > 0 and A[i-1] > B[j]:
			#i is too big, must decrease it
			imax = i-1
		else:
			#i is perfect
			if i == 0: max_of_left = B[j-1]
			elif j == 0: max_of_left = A[i-i]
			else: max_of_left = max(A[i-1],B[j-1])

			if (m+n) % 2 ==1:
				return max_of_left

			if i == m: min_of_right = B[j]
			elif j == n: min_of_right = A[i]
			else: min_of_right = min(A[i],B[j])

			return (max_of_left + min_of_right) / 2.0
'''
#Time complexity: O(log(min(n,m)))

#Space complexity: O(1)
	#only stores 9 variables
