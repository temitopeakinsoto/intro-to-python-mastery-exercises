#Try writing a Python function to perform a linear search on a set of data.

def searchname(name, listofnames):
  for (i, index) in enumerate(listofnames):
    if name == index:
      return (name, i)
    else:
      return "Name not found"

names = ["tope", "samson", "jadesola","topes", "samsons", "jadesolas"]
res = searchname("tope", names)
print(res)