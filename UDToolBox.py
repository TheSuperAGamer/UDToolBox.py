class UDToolBox:
  
  
  def upc(text):
    return text.upper()
  
  def lwc(text):
    return text.lower()
  
  def asc(vals):
    return sorted(vals)
  
  def lister(vals):
    vals = list(vals)
    for s,val in zip(range(len(vals)), vals):
      print(f"{s+1}. {val}")
  
  
  def mean(vals):
    a = 0
    for val in vals:
      a += val
    return a/len(vals)
  
  def add(vals):
    sum = 0
    for val in vals:
      sum += val
    return sum
  
  def median(vals):
    vals = sorted(list(vals))
    n = len(vals)
    if n%2 == 0:
      m = (vals[(int((n/2))-1)] + vals[int(n/2)])/2
    else:
      m = vals[int(n/2)]
    return m
  
  def mode(vals):
    counts = {}
    for val in vals:
      if val in counts:
        counts[val] += 1
      else:
        counts[val] = 1
    max_count = max(counts.values())
    m = [val for val, count in counts.items() if count == max_count]
    return m
  
  def mult(vals):
    pro = 1
    for val in vals:
      pro *= val
    return pro
    
  def dedupe(li):
    return list(set(li))
  
  def invert_dict(d):
    a = {}
    for key, val in d.items():
      a[val] = key
    return a
  






#Main Code!
ud = UDToolBox

a = ud.upc("Hello")
print(a)

print(ud.asc([1,3,5,2,53,882,2,86,88]))


ud.lister(["Eggs", "Bread", "Chips","Eggs"])


print(ud.mean([1,3,3,2,4]))

print(ud.median([1,5,2,5,2,4]))
print(ud.median([3,8,9,5,9]))

print(ud.mult([2,2,4,8,7]))

print(ud.mode([3,3,3,3,3,3,42,32,4,2,4,4,4,4,4]))


print(ud.dedupe([1,2,2,3,4,2,5,6,5,5,7,8,9,7,7,0]))

my_dict = {
  "a" : "apple",
  "b" : "ball",
  "c" : "cat"
}

print(ud.invert_dict(my_dict))