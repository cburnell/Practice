from binarySearch import binarySearch

testarr1 = [i for i in xrange(101)]
for testfind1 in xrange(len(testarr1)+1):
    result = binarySearch(testarr1, testfind1)
    print (testfind1, result)
print "Testing if its multiplied by 2"
testarr2 = [testitem*2 for testitem in testarr1]
armin = min(testarr2)
armax = max(testarr2)
print testarr2
print (armin, armax)
print "-"*10
for testfind2 in xrange(armin - 1, armax + 2):
    result = binarySearch(testarr2, testfind2)
    print (testfind2, result)

