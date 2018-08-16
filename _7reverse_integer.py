class Solution:
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x<0:
      answer = int(str(x)[-1:0:-1])*-1 if (int(str(x)[-1:0:-1])*-1) & -0x80000000 == -0x80000000 else 0
    elif x==0:
      return 0
    else:
      answer = int(str(x)[::-1]) if int(str(x)[::-1]) & 0x7fffffff == int(str(x)[::-1]) else 0
    return answer
    