#StudOopsUnPickEx.py
import pickle
class sturead:
	def studprt(self):
		try:
			with open("student.data","rb") as fp:
				print("\tsno\tsname\tmarks")
				while(True):
					obj=pickle.load(fp)
					obj.dispstuddata()
		except EOFError:
			print("************************ENDPOINT***************")


sa=sturead()
sa.studprt()