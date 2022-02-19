"""Creation of Dictionary""" 

#By list of tuple
d1=dict([(1,2),(3,4),("shubham","aglawe")])
print(f"list of tuple:{d1}")
#By list of set
d2=dict([{1,2},{3,4},{"shubham","aglawe"}])
print(f"list of set:{d2}")
#By list of list
d3=dict([[1,2],[3,4],["shubham","aglawe"]])
print(f"list of list:{d3}")

#By tuple of tuple
d4=dict(((1,2),(3,4),("shubham","aglawe")))
print(f"tuple of tuple:{d4}")
#By tuple of set
d5=dict(({1,2},{3,4},{"shubham","aglawe"}))
print(f"tuple of set:{d5}")
#By tuple of list
d6=dict(([1,2],[3,4],["shubham","aglawe"]))
print(f"tuple of list:{d6}")

#By set of tuple
d7=dict({(1,2),(3,4),("shubham","aglawe")})
print(f"set of tuple:{d7}")


""""
Output:
{1: 2, 3: 4, 'shubham': 'aglawe'}
{1: 2, 3: 4, 'aglawe': 'shubham'}
{1: 2, 3: 4, 'shubham': 'aglawe'}
{1: 2, 3: 4, 'shubham': 'aglawe'}
{1: 2, 3: 4, 'aglawe': 'shubham'}
{1: 2, 3: 4, 'shubham': 'aglawe'}
{1: 2, 'shubham': 'aglawe', 3: 4}
"""