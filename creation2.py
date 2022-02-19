"""Creation of Dictionary""" 

#By list of tuple,list,set
d1=dict([(1,2),[3,4],{"shubham","aglawe"}])
print(d1)

#By tuple of tuple,list,set
d2=dict(((1,2),[3,4],{"shubham","aglawe"}))
print(d2)

""""
Output:
{1: 2, 3: 4, 'aglawe': 'shubham'}
{1: 2, 3: 4, 'aglawe': 'shubham'}
"""