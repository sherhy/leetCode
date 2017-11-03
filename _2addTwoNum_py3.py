'''
example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# this can also be done by taking each element, and adding by the multipler of their ten's place
# and converting the number back into a list, but for the purpose of exercise:

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, L = [0]): #how to set default params
		if L == [0]: 
			self.val = None
			self.next = None
		elif len(L)>0:
			self.val = L.pop(0)
			self.next = ListNode(L)
		else:
			self.next = None

	def addNode(self, n):
		if self.val == None:
			self.val = n
			self.next = ListNode()
		elif self.next != None:
			ListNode.addNode(self.next, n)
		else: self.next = ListNode([n])

	def printlist(self):
		print(self.val, end='')
		node = self.next
		while node != None:
			print(" ->", node.val, end='')
			node = node.next
		print()

	def getLen(self):
		i = 0
		node = self
		while node != None:
			i+=1
			node = node.next
		# print(i)
		return i

	def toList(self):
		node = self
		li = []
		while node.next != None:
			li.append(node.val)
			node = node.next
		return li



class Solution:
	@staticmethod
	def addTwoNumbers(l1, l2):
		print('argv:',l1,l2)
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		
		linkl1 = ListNode(l1)
		linkl2 = ListNode(l2)
		# linkl1.printlist()
		# linkl2.printlist()

		l1len = linkl1.getLen()
		l2len = linkl2.getLen()

		n = min(l1len,l2len)

		sol = ListNode()
		carry = 0
		nodel1 = linkl1
		nodel2 = linkl2
		for i in range(n-1):
			sumOfNodes = nodel1.val + nodel2.val + carry
			carry = sumOfNodes // 10
			digit = sumOfNodes % 10

			sol.addNode(digit)
			nodel1 = nodel1.next
			nodel2 = nodel2.next
		# print(nodel1.next, nodel2.next)


		for i in range(max(l1len,l2len)-n):
			# print('sup')
			if nodel1.next == None:
				# print('not here')
				sumOfNodes = nodel2.val + carry
				carry = sumOfNodes //10
				digit = sumOfNodes%10
				sol.addNode(digit)
				nodel2 = nodel2.next
			elif nodel2.next ==None:
				# print('should be here')
				sumOfNodes = nodel1.val + carry
				carry = sumOfNodes //10
				digit = sumOfNodes%10
				sol.addNode(digit)
				nodel1 = nodel1.next

		if carry != 0:
				sol.addNode(carry)

		#sol.printlist()
		solution = sol.toList()
		print('sol:', solution)
		return solution




def testAll():
	l1, l2 = [2,4,3],[5,6,4]
	sol = [7,0,8]
	assert(Solution.addTwoNumbers(l1,l2)==sol)

	l1, l2 = [2,4,3],[5,6,4,6]
	sol = [7,0,8,6]
	assert(Solution.addTwoNumbers(l1,l2)==sol)

	l1, l2 = [2,4,5],[5,6,4,6,5]
	sol = [7,0,0,7,5]
	assert(Solution.addTwoNumbers(l1,l2)==sol)

	print('passed')


if __name__ =='__main__':
	testAll()