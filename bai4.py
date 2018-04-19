class Sinhvien:
	def __init__(self,MSSV,Hoten,Makhoa):
		self.MSSV = MSSV
		self.Hoten = Hoten
		self.Makhoa = Makhoa
	def getMSSV(self):
		return self.MSSV
	def setMSSV(self):
		this self.MSSV
	def getHoten(self):
		return self.Hoten
	def setHoten(self):
		this self.Hoten
	def getMakhoa(self):
		return self.Makhoa
	def setMakhoa(self):
		this self.Makhoa
        def printSV(self):
		print self.MSSV, '\t', self.Hoten, '\t', self.Makhoa
sv1 = Sinhvien('001','Mai A','01')
sv2 = Sinhvien('002','Trần B','01')
sv3 = Sinhvien('003','Văn C','03')
sv4 = Sinhvien('004','Thị K','001')
sv=[]
sv.append(sv1)
sv.append(sv2)
sv.append(sv3)
sv.append(sv4)
print 'MSSV\tHo ten\tMakhoa
sv1.printSV()
sv2.printSV()
sv3.printSV()
sv4.printSV()

	


