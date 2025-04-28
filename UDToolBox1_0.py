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
  
  def func_list():
    return ["Uppercase (upc)","Lowercase (lwc)","Sort in ascending order (asc)","Numbered list (lister)","Addition (add)","Multiplication (mult)","Mathematical mean (mean)","Mathematical mode (mode)","Mathematical median (median)"]
