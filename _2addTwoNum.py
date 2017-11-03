# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def findlen(L):
	i = 0
	node = L
	while node != None:
		i+=1
		node = node.next
	return i

def printList(L):
	node = ListNode
	while node != None:
		print node.val
		node = node.next


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		sList = []
		nMin = min(findlen(l1),findlen(l2))
		nMax = max(findlen(l1),findlen(l2))
		val1= l1
		val2= l2
		for i in range(nMin):
			sList.append(val1.val+val2.val)
			val1 = val1.next
			val2 = val2.next

		fList = ListNode(None)
		if findlen(l1)>findlen(l2):
			fList = l1
		if findlen(l1)<findlen(l2):
			fList = l2
		if not nMax == nMin:
			for i in range(nMax):
				if i < nMin: 
					fList = fList.next
					continue

				sList.append(fList.val)
				fList = fList.next

		# print sList

		carry = 0
		for i in range(len(sList)):
			if sList[i] >= 10:
				digit = sList[i] % 10 + carry
				carry = sList[i]//10
			else:
				toCarry = sList[i]+carry
				carry = toCarry//10
				digit = toCarry%10
			sList[i] = digit
		if carry != 0: sList.append(carry)

		# print sList
		return sList

def checkaddTwoNumbers():
	b = Solution()

	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)

	
	assert(b.addTwoNumbers(l1,l2)==[7,0,8])

	l1 = ListNode(1)
	l1.next = ListNode(8)
	l2 = ListNode(0)
	assert(b.addTwoNumbers(l1,l2)==[1,8])

	l1 = ListNode(0)
	l2 = ListNode(7)
	l2.next = ListNode(3)
	assert(b.addTwoNumbers(l1,l2)==[7,3])

	print 'passed'

if __name__ == "__main__":
	checkaddTwoNumbers()


'''
(1) java

public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
  ListNode dummyHead = new ListNode(0);
  ListNode p = l1, q = l2, curr = dummyHead;
  int carry = 0;
  while (p != null || q != null) {
    int x = (p != null) ? p.val : 0;
    int y = (q != null) ? q.val : 0;
    int sum = carry + x + y;
    carry = sum / 10;
    curr.next = new ListNode(sum % 10);
    curr = curr.next;
    if (p != null) p = p.next;
    if (q != null) q = q.next;
  }
  if (carry > 0) {
    curr.next = new ListNode(carry);
  }
  return dummyHead.next;
}


Time complexity: O(max(m,n))
	that's one loop

Space complexity: O(max(m,n))
	length of new list is max(m,n)+1
'''
