balance=999999
import datetime
t=datetime.datetime.now()
import random
c=random.random()
c1=random.random()
print("Insert your ATM Card in the ATM machine")
print("Welcome to Unknown ATM")
# l=Str(input("Select your language\n1.English\2.Hindi"))
x=str(input("Enter atm pin:- "))
y=len(x)
if y==4:
	a=int(input("1.FAST CASH\n2.CASH WITHDRAWAL\n3.CASH DEPOSIT\n4.Change/Reset PIN\n5.Fund Transfer (Transfer Money from ATM)\n6.BALANCE ENQUIRY\n:-"))
	if a==1:
		# a1=int(input("1.Saving account\n2.Current account\n:-"))
		b=int(input("1.₹500\n2.₹1000\n3.₹1500\n4.₹2000\n5.₹5000\n6.₹10000\n"))
		if b==1:
			a1=int(input("1.Saving account\n2.Current account\n:-"))
			print("Now collect the cash\n₹500")
		elif b==2:
			a1=int(input("1.Saving account\n2.Current account\n:-"))
			print("Now collect the cash\n₹1000")
		elif b==3:
			a1=int(input("1.Saving account\n2.Current account\n:-"))
			print("Now collect the cash\n₹1500")
		elif b==4:
			a1=int(input("1.Saving account\n2.Current account\n:-"))
			print("Now collect the cash\n₹2000")
		elif b==5:
			a1=int(input("1.Saving account\n2.Current account\n:-"))
			print("Now collect the cash\n₹5000")
		elif b==6:
			a1=int(input("1.Saving account\n2.Current account\n:-"))
			print("Now collect the cash\n₹10000")
		else:
			print("Please collect your card")
	elif a==2:
		a1=int(input("1.Saving account\n2.Current account\n:-"))
		a3=int(input("Enter Amount:- "))
		if a3<balance:
			p=int(input("You need Print receipt or not\n1.Yes\n2.No\n:-"))
			if p==1:
				print("We understand your world")
				print("Unknown Branch")
				print("Date and time\n",t)
				print("Card no:- \n",c)
				print("TO KNOW YOUR BALANCES.CALL TOLL FREE ON 1800-270-3333 FROM  YOUR MOBILE AND GET YOUR ACCOUNT BALANCE INSTANTLY")
				print("S.NO\n",c1)
				print("TRAN.\nWITHDRAWAL")
				print("Withdrawal Amount \n₹",a3)
				print("Balance Amount is:-",balance-a3)
				print("Successfully withdrawal")
			elif p==2:
				print("Successfully withdrawal\nNow collect the cash ₹",a3)
				print("Thanks for using our services")
			else:
				print("Error")
		else:
			print("insufficient funds")
	elif a==3:
		a1=int(input("1.Saving account\n2.Current account\n:-"))
		print("Insert cash")
		d=int(input("Enter amount to verify\n:-₹"))
		print("After you have inserted all the cash and it has been counted by the machine, carefully review and confirm the amount displayed on the screen. The money will reflect in your account within just a few seconds.")
		print("Total amount is:- ₹",d+balance)
		print("Thanks for using our services")
		p1=int(input("You need Print receipt or not\n1.Yes\n2.No\n:-"))
		if p1==1:
			print("We understand your world")
			print("Unknown Branch")
			print("Date and time\n",t)
			print("Card no:- \n",c)
			print("TO KNOW YOUR BALANCES.CALL TOLL FREE ON 1800-270-3333 FROM  YOUR MOBILE AND GET YOUR ACCOUNT BALANCE INSTANTLY")
			print("S.NO\n",c1)
			print("TRAN.\nCASH DEPOSIT")
			print("DEPOSIT Amount is:- \n₹",d)
			print("Balance Amount is:-",balance+d)
			print("Successfully Deposit in your account")
		elif p1==2:
			print("Successfully Deposit in your account\n ₹",d)
			print("Thanks for using our services")
		else:
			print("Error")
	elif a==4:
		a1=int(input("1.Saving account\n2.Current account\n:-"))
		n=str(input("Enter Moblie number to verify\n:-"))
		n1=len(n)
		if n1==10:
			n3=str(input("Enter One-time password:-"))
			n4=len(n3)
			if n4==6:
				n5=int(input("Enter New Pin\n:-"))
				print("Your PIN Has Been Changed Successfully")
			else:
				print("Your One-time password is wrong\nPlease re-enter your One-time password\nTry again")
		else:
			print("Re-check your Moblie number\nTry again")
	elif a==5:
		a1=int(input("1.Saving account\n2.Current account\n:-"))
		t=str(input("Enter Bank Account Number:- "))
		t1=str(input("Enter IFSC Code:- "))
		t2=str(input("Enter Account Holder Name:- "))
		t3=int(input("Enter Phone number(optional):- "))
		t4=len(t)
		if t4==12:
			print("The fund will be transferred successfully.")
			print(" If a transaction is not completed within the time limit provided then a ‘time out’ message will appear. In such a case, the account-to-account transfer from the ATM process has to be repeated")
		else:
			print("Please re-check your details")
	elif a==6:
		a1=int(input("1.Saving account\n2.Current account\n:-"))
		print("Your account balance is:- ₹",balance)
		p2=int(input("You need Print receipt or not\n1.Yes\n2.No\n:-"))
		if p2==1:
			print("We understand your world")
			print("Unknown Branch")
			print("Date and time\n",t)
			print("Card no:- \n",c)
			print("TO KNOW YOUR BALANCES.CALL TOLL FREE ON 1800-270-3333 FROM  YOUR MOBILE AND GET YOUR ACCOUNT BALANCE INSTANTLY")
			print("S.NO\n",c1)
			print("Balance Amount is:-",balance)
		elif p2==2:
			print("Thanks for using our services")
	else:
		print("Error")
else:
	print("Please Enter Correct Pin")