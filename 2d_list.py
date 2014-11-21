#coding:utf-8
from __future__ import division
from random import randint

##scores = []
##classes = ["core C++","core Java","Servlet","JSP","EJB"]
##for i in xrange(0,20):
##  score = []
##  for j in range(0,5):
##    score.append(randint(0,100))
##  scores.append(score)
##for std in scores:
##  for s in std:
##    print "%3d"%s,
##  print
##
##total_score = []
##for std in scores:
##  total = 0
##  for s in std:
##    total += s
##  total_score.append(total)
##print total_score
##
##ave_score = [0,0,0,0,0]
##
##for std in scores:
##  for i,s in enumerate(std):
##    ave_score[i] += s
##for i in range(len(ave_score)):
##  ave_score[i] = ave_score[i] / 20
##
##print ave_score

def score(score_list,course_list,student_num):
    every_score = [[score_list[i][j] for i in range(len(course_list))] for j in range(student_num)]
    every_total = [sum(every_score[i]) for i in range(student_num)]
    ave_course = [sum(score_list[i]) / len(score_list[i])for i in range(len(score_list))]

    return (every_score,every_total,ave_course)
if  __name__ == "__main__":
    course_list = ["core C++","core Java","Servlet","JSP","EJB"]
    student_num = 20
    score_list = [[randint(0,100) for i in range(student_num)] for j in range(len(course_list))]

    for i in range(len(course_list)):
        print "score of every one in %s:"%course_list[i]
        print score_list[i]

    every_score,every_total,ave_course = score(score_list,course_list,student_num)

    print "\n"
    print "NEXT IS EVERY ONE SCORE IN EVERY COURSE:"
    for name in course_list:
        print name,
    print "\t"
    print every_score
    print "\n"
    print "every one all score:\t",every_total
    print "every course of average score:\t",ave_course

