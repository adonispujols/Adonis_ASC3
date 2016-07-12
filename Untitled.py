from Myro import *
#for sliding
for seconds in timer(2):
    motors(0,1)
    stop()
for seconds in timer(2):
    motors(0,-1)
    stop()
for seconds in timer(2):
    motors(1,0)
    stop()
for seconds in timer(2):
    motors(-1,0)
    stop()
## ##for wiggle
## for seconds in timer(2):
##     motors(0,1)
##     stop()
## for seconds in timer(2):
##     motors(0,-1)
##     stop()
## for seconds in timer(2):
##     motors(1,0)
##     stop()
## for seconds in timer(2):
##     motors(-1,0)
##     stop()