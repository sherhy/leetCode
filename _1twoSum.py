#find the target sum from an element from two lists

def twoSum(nums, target):
	"""
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
	sL = sorted(nums)
	for _ in range(len(nums)-1):
		# print('nums', nums)
		a = sL.pop(0) #2, sL = [3,4]
		aInd = nums.index(a) #1
		b = target - a #4
		# print(a,b)
		if a == b:
			if nums.count(a) < 2: continue
			return [aInd, nums.index(b,aInd+1)]
		if b in sL:
			return [aInd, nums.index(b)] 

def testtwoSum():
	print('twoSum', end=": ")
	assert(twoSum([3,3],6)==[0,1])
	assert(twoSum([3,2,4],6)==[1,2])
	print('passed')

def main():
	testtwoSum()

if __name__ == '__main__':
	main()
'''
solution page

(1) brute force
Time complexity : O(n^2)
	For each element, we try to find its complement by looping through 
	the rest of array which takes O(n)O(n) time. Therefore, the time 
	complexity is O(n^2)

Space complexity : O(1)O(1).


(2) two-pass hash
	- create hash in first iteration
	for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
Time complexity : O(n). 
	We traverse the list containing nn elements 
	exactly twice. Since the hash table reduces the look up time to O(1), 
	the time complexity is O(n)O(n).

Space complexity : O(n). 
	The extra space required depends on the number of items stored in 
	the hash table, which stores exactly n elements.


(3) one-pash hash
	- one iteration:
	- create hash and look back

Time complexity : O(n). 
	We traverse the list containing nn elements only once. 
	Each look up in the table costs only O(1)O(1) time.

Space complexity : O(n). 
	The extra space required depends on the number of items stored in 
	the hash table, which stores at most nn elements.
'''