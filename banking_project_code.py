#!/usr/bin/python
import time
from datetime import date
class Bank():
	def __init__(self):
		self.Name=[]
		self.Amount=[]
		self.z=123000
		self.Account=[]
		self.Type=[]
		self.Time=[]
		self.num=1	
	def CreateAccount(self,typenumber,name,amount) :
		self.Type.append(typenumber)
		if typenumber==1 :		
			if amount<1000 :
	                        while amount<1000:
	                                print "Minimum balance should be 1000"
	                                print "Again Enter the amount :",
	                                amount=input()
	                        self.Name.append(name)
	                        self.Amount.append(amount)
	                        print "Your Account number is :",
	                        print self.z
	                        self.Account.append(self.z)
				self.Time.append(date.today())
	                        self.z=self.z+1
	                else :
	                        self.Name.append(name)
	                        self.Amount.append(amount)
	                        print "Your Account number is :",
	                        print self.z
	                        self.Account.append(self.z)
				self.Time.append(date.today())
	                        self.z=self.z+1
                if typenumber==2 :
			self.Name.append(name)
			self.Amount.append(amount)
			self.Account.append(self.z)
			self.Time.append(date.today())
			print "Your Account number is :",
	               	print self.z
	               	self.z=self.z+1
		if typenumber==3 :
			if amount<10000 :
       		             	while amount<10000:
                	                print "Minimum balance should be 10000"
                	                print "Again Enter the amount :",
                	                amount=input()	
	 		       	self.Name.append(name)
          	      	        self.Amount.append(amount)
               		        print "Your Account number is :",
              	 	        print self.z
                        	self.Account.append(self.z)
				self.Time.append(date.today())
                        	self.z=self.z+1
               		else :
                        	self.Name.append(name)
                        	self.Amount.append(amount)
                        	print "Your Account number is :",
                        	print self.z
                        	self.Account.append(self.z)
				self.Time.append(date.today())
                        	self.z=self.z+1	
    		     
	def BalanceEnquiry(self,account) :
		m=account in self.Account
	#	print m
		if(m==False) :
			print "AccountNumber is InValid"
		else :
			k=self.Account.index(account)
        	        print "Your balance is :",
        	        print self.Amount[k]
                
	def DepositAmount(self,account,amount) :
		m=account in self.Account
	#	print m
		if(m==False) :
			print "AccountNumber is InValid"
		else :
			k=self.Account.index(account)
			if self.Type[k]==3 :
				print "Deposits are not permitted ."
			else :
				self.Amount[k]=self.Amount[k]+amount
				print "Your final balance is :",
				print self.Amount[k]
		
	def WithdrawAmount(self,account,amount) :
		m=account in self.Account
	#	print m
		if(m==False) :
			print "AccountNumber is InValid"
		else :	
			k=self.Account.index(account)
			if self.Type[k]==3 :
				print "Withdrawl of amount is not permitted .Only way to withdraw money is to close the account"
			else :
				if self.Amount[k]-amount>=5000 :
					self.Amount[k]=self.Amount[k]-amount
				else :
					while self.Amount[k]-amount < 5000 :	
						print ("Maximum Amount can be taken : %d" % (Amount[k]-5000))
						amount=input()
					self.Amount[k]=self.Amount[k]-amount
				print "Your final balance is :",
				print self.Amount[k]
	
	def SearchByName(self,name) :
		i=0
		k=len(self.Name)
		flag=0
		while i<k :
			if name in self.Name[i] :
				print "Your name is :",
				print self.Name[i]
				print "Your Account number :",
				print self.Account[i]
				flag=1
#				break
			i=i+1
		if flag==0:
			print "Account doesn't exist"
			
	def CloseAccount(self,account) :
		l=account in self.Account
		if l==0 :
			print "Your Account is invalid ."
		else : 
			k=self.Account.index(account)
			print ("Balance to be refunded : %d" % (self.Amount[k]))					
			self.Account.remove(self.Account[k])
			self.Name.remove(self.Name[k])
			self.Amount.remove(self.Amount[k])
			self.Type.remove(self.Type[k])
			print "Your Account is closed "

	def Update(self,account) :
		m=account in self.Account
#		if(m==False) :
		#	print "AccountNumber is InValid"
		if m!=False :
			k=self.Account.index(account)
			if self.Type[k]==1 :
				today=date.today()
				tem=abs(today-self.Time[k])
				l=tem.days
				if l!=0 :
					self.Amount[k]=self.Amount[k]+(self.Amount[k]*(float(4)/100)*(float(l)/365))
				self.Time[k]=today
			elif self.Type[k]==2 :
				today=date.today()
				self.Time[k]=today
			elif self.Type[k]==3 :
				today=date.today()
        	                tem=abs(today-self.Time[k])
                	        l=tem.days
	                        if l!=0 :
	                                self.Amount[k]=self.Amount[k]+(self.Amount[k]*(float(12)/100)*(float(l)/365))
	                        self.Time[k]=today
					

	
B=Bank()
while 1 :
	print ""
	print "1.Create account         ",
	print "2.Balance Enquiry      ",
	print "3.Deposit Amount  "
	print "4.Withdraw Amount        ",
	print "5.Search by name       ",
	print "6.Close Account   "
	print "7.exit"
	try:
		num=input()	
		if num==1 :
			print "Choose your type :"
			print "1.Savings Account     ",
			print "2.Current Account     ",
			print "3.Fixed Account"
			while 1:
				try:
					typenumber=input()
					break
				except:
					print "Please select the account type as listed above"
			print "Enter your name :",
			name=raw_input()
			print "Enter the amount :",
			amount=input()
			B.CreateAccount(typenumber,name,amount)
			
		elif num==2 :
			print "Enter your account number :",
			account=input()
			B.Update(account)
			B.BalanceEnquiry(account)

		elif num==3 :
			print "Enter your Account number :",
			account=input()
			print "Enter the amount to be deposited :",
			amount=input()
			B.Update(account)
			B.DepositAmount(account,amount)

		elif num==4 :
			print "Enter your Account number :",
			account=input()
			print "Enter the amount to be withdrawn :",
			amount=input()
			B.Update(account)
			B.WithdrawAmount(account,amount)

		elif num==5 :
			print "Enter your name :",
			name=raw_input()
			B.SearchByName(name)
		
		elif num==6 :
			print "Enter your Account number :",
			account=input()
			B.Update(account)
			B.CloseAccount(account)
	
		elif num==7:
			break
	
		else:
			print "Please choose a number between 1 and 7"
	except:
		print "\nPlease choose a valid option"
		
print "\n----------------------------------------------"
print "Ac_Holder_Name  "+"Ac_No  "+"Amount  "+"Type"
print "----------------------------------------------"

for i in range(len(B.Name)):
	print str(B.Name[i])+"\t\t"+str(B.Account[i])+"\t"+str(B.Amount[i])+"\t"+str(B.Type[i])

print "----------------------------------------------"
print "\n"

f=open("bank.txt","w")
f.write("Name : AccountNumber : Amount : Type\n")
y=len(B.Name)
i=0
while i<=y-1 :
	f.write(B.Name[i])
	f.write(" : %d"%(B.Account[i]))
	B.Update(B.Account[i])
	a=str(B.Time[i])
	f.write(" : %d"%(B.Amount[i]))
	f.write(" : %d : "%(B.Type[i]))
	f.write(a)
	f.write("\n")
	i=i+1
