#coding:utf-8
from __future__ import division
from random import randint
def ave_score():
	scores = [randint(0,100) for i in range(40)]
	print "the scores is "
	print scores
	total_score = sum(scores)
	ave = total_score / len(scores)
	print "ave score is ",ave
	
	low_score = [s for s in scores if s < ave]
	print "score low ave are:"
	print low_score
	print "sorted socres are:",sorted(scores,reverse=True)
if __name__ == "__main__":
	ave_score()