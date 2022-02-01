"""
Given a string as input. Print the reverse of input string in following pattern.
Input-> "who"
Output-> who#ohw
"""

st = "who"
ln = len(st)
nw_st = ""
for i in range(ln-1,-1,-1):
  ch = st[i]
  nw_st = nw_st + ch
print(f"{st}#{nw_st}")
