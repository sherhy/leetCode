class Solution:
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    #makeZZ
    if numRows == 1: return s
    rows = ['']*numRows
    direction = 1
    index = 0
    s = list(s)
    while len(s) > 0:
      rows[index] += s.pop(0)
      index += direction
      if index == numRows-1 or index == 0:
        direction *= -1
    st = ''.join(rows)
    
    #readZZ
    sentence = "".join(st.split('\n'))
    return sentence.replace(" ", "")
    
    