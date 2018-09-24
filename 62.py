p=raw_input()
"""if all(a in '01' for a in q):
    print "yes"
else:
    print "no"
    """
if not(p.translate(None,'01')):
    print "yes"
else:
    print "no"
