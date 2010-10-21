#!/usr/bin/env python

import cProfile
import pstats
import yva

cProfile.run("yva.main()")
p = pstats.Stats("mainprof")
temp = p.sort_stats('time')
temp.print_stats(10)
