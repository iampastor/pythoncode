#coding:utf-8
lst = [[2,2,3],[8,4,6],[2,1,2],[1,8,7]]
def sum_half(lst):
	summ = []
	for x in range(0,len(lst) / 2):
		s,i,j,y = 0,0,x,0
		while i < 2 * x + 1:
			s += lst[i][j]
			if y % 2 == 0:
				j = j - 1
			else:
				j = j
			y += 1
			i += 1
		summ.append(s)
	return summ

if __name__ == "__main__":
	print sum_half(lst)

# def summ_left(lst):
#     summ = []
#     x = [i for i in range(len(lst))]
#     y = [j for j in range(len(lst[0]))]
#     sx = [i for i in x if i%2==0]
#     for i in sx:
#         s=0
#         j=0
#         while i>=0 and j<=y[-1]:
#             s = s+ lst[i][j]
#             if i%2==1:
#                 j = j+1
#             else:
#                 j = j
#             i = i-1
#         summ.append(s)
#     return summ

# def summ_end(lst):
#     summ=[]
#     y = [j for j in range(len(lst[0]))]
#     ex = len(lst)-1
#     for m in range(len(y)):
#         s = 0
#         i=ex
#         j=m
#         while i>=0 and j<=y[-1]:
#             s= s+lst[i][j]
#             if i%2==1:
#                 j = j+1
#             else:
#                 j=j
#             i = i-1
#         summ.append(s)
    
#     return summ
# if __name__ == "__main__":
# 	print summ_left(lst)
# 	print summ_end(lst)