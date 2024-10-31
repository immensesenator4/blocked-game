import random
from datetime import datetime
import time


def true_randomeness():
    l=random.randint(1,9999)
    r=0
    for i in range(0,l):
        d=random.randint(0,9999999999+int(time.time()))
        random.seed(d)
        r+=d+random.randint(0,9999999999)
        random.seed(r)

    random.seed(r)


