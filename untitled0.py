# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 21:23:04 2019

@author: Dell
"""

from instructionUnit import *

line = "inst.txt"
listt = insrtuctionUnit(line)
i=listt.getIssue(2, 1) #issue n instructions from the queue
listt.revIssue(1, 1) #reverse issue (return the instructions back into the queue) in the same order
#p=listt.getIssue(1, 0) #issue only oe instruction

#intsruction_type=p[2].instType  #get instructin type of the first instruction in the issued ones
#rs=p[2].r1  #get the first register, same for r2, r3
#imm=p[2].imm #get immediated value if exists, if not, it'll be r2