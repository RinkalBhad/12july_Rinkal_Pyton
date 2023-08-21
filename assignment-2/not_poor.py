# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
#whole 'not'...'poor' substring with 'good'. Return the resulting string


def not_poor(str1):
  sn = str1.find('not')
  sp = str1.find('poor')
  

  if sp > sn and sn>0 and sp>0:
    str1 = str1.replace(str1[sn:(sp+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))




