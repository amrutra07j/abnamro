common = {'you':'yours', 'he':'his', 'i':'mine', 'she':'her'}

state = common.get('him', None)
if state:
    print "sorry, no him"
    print state