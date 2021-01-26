from random import randint



def bubble_sort(l):
	for i in range(0,len(l)-1):
		for j in range(0,len(l)-1-i):
			if l[j]>l[j+1]:
				l[j],l[j+1]=l[j+1],l[j]
	return l
def insertion_sort(l):
	for i in range(0,len(l)):
		for j in range(i-1,0,-1):
			if l[j]>l[j+1]:
				l[j],l[j+1]=l[j+1],l[j]
			else:
				break
	return l
def selection_sort(l):
	for i in range(0,len(l)-1):
		mi=i
		for j in range(i+1,len(l)):
			if l[j]<l[mi]:
				mi=j
		if mi!=i:
			l[i],l[mi]=l[mi],l[i]
	return l
def merge_sort(l):
	def ms2(l,f,t):
		def merge(l,f,m,t):
			L=l[f:m]
			R=l[m:t+1]
			L.append(999999999)
			R.append(999999999)
			i=j=0
			for k in range(f,t+1):
				if L[i]<=R[j]:
					l[k]=L[i]
					i+=1
				else:
					l[k]=R[j]
					j+=1
			return l
		if f<t:
			m=(f+t)//2
			l=ms2(l,f,m)
			l=ms2(l,m+1,t)
			l=merge(l,f,m,t)
		return l
	return ms2(l,0,len(l)-1)
def quick_sort(l):
	if len(l)<=1:return l
	s,e,b=[],[],[]
	p=l[randint(0,len(l)-1)]
	for x in l:
		if x<p:s+=[x]
		elif x==p:e+=[x]
		else:b+=[x]
	return quick_sort(s)+e+quick_sort(b)
if __name__=="__main__":
	import time
	l=[randint(0,5000) for _ in range(5000)]
	ts=time.time()
	bl=bubble_sort(l[:])
	tbs=time.time()-ts
	ts=time.time()
	il=insertion_sort(l[:])
	tis=time.time()-ts
	ts=time.time()
	sl=selection_sort(l[:])
	tss=time.time()-ts
	ts=time.time()
	ml=merge_sort(l[:])
	tms=time.time()-ts
	ts=time.time()
	ql=quick_sort(l[:])
	tqs=time.time()-ts
	print(f"Bubble sort:\t~{tbs} s\n\nInsertion sort:\t~{tis} s\n\nSelection sort:\t~{tss} s\n\nMerge sort:\t\t~{tms} s\n\nQuick sort:\t\t~{tqs} s")