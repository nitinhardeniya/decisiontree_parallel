import sys

def parse_trainfile(trainfile):
	
	"""
	@note: Give a trainfile parse the file, Split and create all the attribute list based on the given algo.
	@parm: trainfile (file)
	@return: list of list of each attribute list, class_list
	"""
	
	f=open(trainfile,'r')
	print type(f)
	age_list=[]
	salary_list=[]
	class_list={}
	attribute_list=[]
	for i,line in enumerate (f):
		print line
		parts=line.split(',')
		age=int(parts[0])
		salary=int(parts[1])
		class_lvl=str(parts[2]).strip()
		age_list.append((age,i))
		salary_list.append((salary,i))
		class_list[i]=(class_lvl,'N1')
	
	print age_list
	print salary_list

	print 'afer sorting '
	print sorted(age_list, key=lambda age_list: age_list[0])
	age_list=sorted(age_list, key=lambda age_list: age_list[0])
	print sorted(salary_list, key=lambda salary_list: salary_list[0])
	salary_list=sorted(salary_list, key=lambda salary_list: salary_list[0])
	print class_list
	attribute_list.append(age_list)
	attribute_list.append(salary_list)

	return attribute_list,class_list

def get_histogram(class_list):
	"""
	@note: Give a class_list calculate the class freqency on given node
	@parm: class_list (list) 
	"""
	hist={}
	for k,v in class_list.items():
		
		if v[0] in hist.keys():
			hist[v[0]]+=1
		else:
			hist[v[0]]=1
	return hist

def cal_gini_index(T):
	"""
	@ To-do
	"""

	return

def EvaluateSplit(attribute_list,class_list):
	"""
	@note: based on SLIQ algo EvaluateSplit
	@parm :attribute_list (list) : a python list where each element is a list of value of attribute
	"""

	for a in attribute_list:
		for val in a:
			print val
			idx=val[1]
			print idx
			if idx in class_list:
				print class_list[idx]
				print 'class histogram at node N1'
				print get_histogram(class_list)
				# cal_gini_index()
		

	return

def main():
	trainfile=sys.argv[1]
	print trainfile
	attribute_list=parse_trainfile(trainfile)[0]
	class_list=parse_trainfile(trainfile)[1]
	EvaluateSplit(attribute_list,class_list)
	return 

if __name__ == '__main__':
	main()