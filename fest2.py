def reverse(sen):
	list1=[]
	list1= sen.split()
	list2=[]
	for i in list1:
		list2.insert(0,i)
	return list2
		
def main():
	sen= raw_input("Enter the sentence: ")
	k=[]
	k= reverse(sen)
	print ' '.join(str(p) for p in k)
main()
