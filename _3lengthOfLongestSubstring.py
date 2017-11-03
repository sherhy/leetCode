'''
Given a string, find the length of the longest substring without repeating characters.
'''
class Solution:
	@classmethod
	def lengthOfLongestSubstring(self,s):
		print(s,end=': ')
		"""
		:type s: str
		:rtype: int
		"""
		maxlen = 0
		substring = ''
		for c in s:
			if c in substring:
				n = substring.index(c)
				if n == len(substring)-1:
					substring = c
				substring = substring[n+1:]+c
				maxlen=max(maxlen,len(substring))
				continue
			substring = substring + c
			maxlen=max(maxlen, len(substring))
		print(maxlen)
		return maxlen


def main():
	assert(Solution.lengthOfLongestSubstring('asdfd')==4)
	assert(Solution.lengthOfLongestSubstring('dfdfdf')==2)
	assert(Solution.lengthOfLongestSubstring('dvdf')==3)
	assert(Solution.lengthOfLongestSubstring("ohvhjdml")==6)
	print('passed')

if __name__=="__main__":
	main()	
'''
(1) brute force
	- iterate through all possible lengths of substring and check for dup
	- return boolean
	- take length of substring

time complexity: O(n^3)
	- each iteration of i requires O(j-i) to see the strings
	- multiplied by the iterations of i gives n^3

space complexity: O(min(m,n))
	- space k (size of set) is required for the longest substring


(2) sliding window 
	- checks the length of the string between repeating characters
	- point is that, [i,j) add 1 --> [i+1,j+1)

time complexity: O(2n) = O(n)
	- at most each letter visited twice

space complexity: O(min(n,m))
	- same rationale as above

(3) sliding window optimised
	my method above

time complexity: O(n)

space complexity: O(min(n,m))
	- same rationale as above
'''