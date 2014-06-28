#!/usr/bin/python
# Author: Chengbin Hu
#

"""
Put any module-level documentation here.
"""

# This make Python 2 act more like Python 3 in several good ways.
from __future__ import absolute_import
from __future__ import division

# If you want the Python 3-style print function (your choice, I happen
# to like it), uncomment the next line.
#from __future__ import print_function

# Your functions should probably go here.
def repeat(f,x,n):
    if n==0:
        return x
    elif n>0:
        if n==1:
            return f(x)
        else:
            return f(repeat(f,x,n-1))
def my_map(f,ls):
    return reduce(lambda x, y: x + [f(y)], ls, [])
def my_filter(f,ls):
    return reduce(lambda x, y: x + ([y] if f(y) else []),ls,[])
def splitList(elements):
    if len(elements)==1:
        return ([elements[0]],[])
    elif len(elements)==0:
        return ([],[])
    else:
        a = [elements[0]]+splitList(elements[2:])[0]
        b = [elements[1]]+splitList(elements[2:])[1]
        return (a,b)
def splitList2(elements):
    return (([elements[0]]+splitList2(elements[2:])[0]) if len(elements) else [],([elements[1]]+splitList2(elements[2:])[1]) if len(elements)>1 else [])
    
# Normally, Python simply executes anything at the top level whether the
# script is being run as a script or being imported from another.
#
# This does some magic to see if the module is being run as a script. If
# so, it runs the code in this block.

if __name__ == "__main__":
    # Put your unit test here. ("pass" is a no-op, used as a placeholder
    # if the syntax requires a statement.)
    
    elements = ["a","b","c",'d',2,4,5,1,1]
    print splitList(elements)

# vim: set et sw=4 ts=4: