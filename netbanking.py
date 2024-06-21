print("Welcome unknown net banking online service🙏🏻")
print("Benefits of our net Baking🏦 services")
print("24/7⏰ Access to Banking🏦 Services")
print("Effortless Financial Transactions💵")
print("Organized Transaction History⏳ and Statements📑")
print("Secure🔒 Online🌐 Banking Experience")
print("Access🔓 to Additional➕ Services")
user="kunal123"
password="123"
balance=12000
Wallet=1000
mobilenumber=1234567891
accountinfo="Accounnt holder Name :- Kunal👦\nAccount Number :- 1234 56 7891 0111 (Saving account🏦)\nWelcome to HDFC online service🙏🏻"
a=str(input("Enter Your User Id:- "))
if a==user:
	b=str(input("Enter Password:- "))
	if b==password:
		print("Unlocked🙏🏻")
		c=int(input("\n1.Mobile Banking \n2.Debit cards \n3.Fund transfers \n4.Order a new cheque book \n5.Mobile recharge and dth payments\n6.Customer Service\n:- "))
		if c==1:
			print(accountinfo)
			d=(int(input("\n1.Pay to mobile number \n2.Loans \n3.Purchase Gift card for shopping \n4.Offers\n:-")))
			if d==1:
				e=str(input("Enter Mobile Number:- "))
				f=int(input("Enter Amount:- "))
				g = len(e)
				if g==10:
					print("Paid Successfully✅🙏🏻")
				else:
					print("Wrong Mobile Number🚫😕")
			elif d==2:
				h=int(input("\n1.Home loan\n2.Gold loan\n3.Personal loan\n4.Car loan\n5.Education loan\n6.Business loan\n:-"))
				if h==1:
					print("Get Home🏠 loans of up to ₹5 crores💵\nThank you for showing interest😊\nMy customer support contact you in 24 hours🙏🏻")
				elif h==2:
					print("Customer Eligibility:-All resident Indians🙏🏻 (Salaried🏢,Self-Employed💸,House wife👩🏻,Students🧑🏻‍🎓,etc.) aged between 18 and 70 years are eligible for our Gold🪙Loans.\nCompetitive and fixed interest rates with no step-up⬆🆙, starting from 0.90%📉 p.m\nNo income documents🗎 required\nPlease Visit our nearest branch🏢\nTiming🕰️ 10am to 4pm and 24*7 customer support☎️")
				elif h==3:
					print("Get a credit line of up to ₹10 lakh💰 in a flash\nThank you for showing interest😊\nMy customer support contact you in 24 hours🙏🏻")
				elif h==4:
					print("Get up to 90%📉funding on purchase of new car🚗\nPlease Visit our nearest branch🏢\nTiming🕰️ 10am to 4pm and 24*7 customer support☎️")
				elif h==5:
					print("Avail unsecured loans of up to INR 50 lakhs📈\nKnow more visit our website💻 www.unknown.com")
				elif h==6:
					print("Take your business🏢 to great heights📶, get unsecured funding up to ₹1 Cr📈\nThank you for showing interest😊\nMy customer support contact you in 24 hours🙏🏻")
				else:
					print("Know more visit our website🔗 www.unknown.com 🙏🏻")
			elif d==3:
				b1=int(input("Brand name\n1.Amazon🛒Pay Gift Card\n2.Flipkart🛒 Gift Card\n3.Myntra Gift Card\n4.Levi's👕🛒 Gift Card\n5.US Polo Assn🛍️ Gift Card\n:-"))
				b2=int(input("Enter amount:-"))
				if b2>100:
					if b1==1:
						print("Gift card send on your mobile number💌☎️")
						print("After Tax📑 and discount🏷 gift card amount is:-",b2-b2*0.02)
					elif b1==2:
						print("Gift card send on your mobile number💌☎️")
						print("After Tax📑 and discount🏷 gift card amount is::-",b2+b2*0.02)
					elif b1==3:
						print("Gift card send on your mobile number💌☎️")
						print("After Tax📑 and discount🏷 gift card amount is::-",b2+b2*0.1)
					elif b1==4:
						print("Gift card send on your mobile number💌☎️")
						print("After Tax📑 and discount🏷 gift card amount is::-",b2)
					elif b1==5:
						print("Gift card send on your mobile number💌☎️")
						print("After Tax📑 and discount🏷 gift card amount is::-",b2-b2*0.018)
					else:
						print("you can't🚫 purchase gift card under⬇️ rs.100☹")
			elif d==4:
				print("20% discount😎 on your all shopping🛒\nTerms and conditions apply🙏🏻")
		elif c==2:
			d1=int(input("\n1.Apply for physical debit card💳\n2.Apply for virtual📱 debit card💳\n3.Block debit card💳\n:-"))
			if d1==1:
				print("Thanks for applying a new debit card💳\ncostumer support will contact you in 24 Hr⏲️ and verify your details and inform your card information and delivery date")
				print("We’re so lucky to have customers like you😊")
			elif d1==2:
				print("Thanks for applying a new virtual debit card💳")
				print("your card active in half an hour be patient\nThank you for making us your first choice, or at least your final choice😇")
			elif d1==3:
				print("Please contact our costumer service📞 and answer some few details like\nAccount number\nDebit card💳number and\nYour card will be blocked❌")
				print("Thank you for making us your first choice, or at least your final choice😇")
			else:
				print("Please contact our costumer service📞")
		elif c==3:
			f1=int(input("1.Upi Money Transfer\n2.Bank Transfer\n3.Wallet\n:-"))
			if f1==1:
				f2=str(input("Enter Upi Id 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃:-"))
				f3=int(input("Enter Amount:-"))
				if f3<=balance:
					print("successfully Transfer😊🙏🏻")
				else:
					print("insufficient funds☹️🙏🏻")
			elif f1==2:
				f4=int(input("Enter 12 digit account number:-"))
				f5=int(input("Enter Amount:-"))
				if f5<=balance:
					print("successfully Transfer😊🙏🏻")
				else:
					print("Insufficient funds☹️🙏🏻")
			elif f1==3:
				f6=int(input("1.Wallet to Bank\n2.Wallet to voucher or gift card\n:-"))
				if f6==1:
					f7=str(input("Enter account Number:-"))
					f8=int(input("Enter Amount:-"))
					if f8<=balance:
						print("successfully	Transfer😊🙏🏻")
					else:
						print("Insufficient	funds☹️🙏🏻")
				elif f6==2:
					f9=int(input("Please select a voucher brand:-\n1.Amazon🛒\n2.Flipkart🛒\n3.Myntra🛒\n4.Dominos's🍕\n5.Zomato📦\n6.Blinkit🚚\n7.Uber🚖\n:-"))
					f10=int(input("Enter Amount:- "))
					if f9==1:
						print("Voucher send on your mobile number☎️")
						print("Voucher after discount🏷 amount is:-",f10+f10*0.05)
						print("Thank You So Much for Your Order! I Hope You Enjoy Your New Purchase!😊🙏🏻 ")
					elif f9==2:
						print("Voucher send on your mobile number☎️")
						print("Voucher after discount🏷 amount is:-",f10+f10*0.1)
						print("Thank You for Shopping With Us!😊🙏🏻")
					elif f9==3:
						print("Voucher send on your mobile number☎️")
						print("Voucher after discount🏷 amount is:-",f10+f10*0.07)
						print("Thank You for Being Our Valued Customer😊🙏🏻")
					elif f9==4:
						print("Voucher send on your mobile number☎️")
						print("Voucher after discount🏷 amount is:-",f10+f10*0.2,"and 50% on your 1st order")
						print("Thank You for Choosing Us. Your Support Means a Lot to Us!😊🙏🏻")
					elif f9==5:
						print("Voucher send on your mobile number☎")
						print("Voucher after discount🏷 amount is:-",f10+f10*0.4)
						print("Free delivery on first order worth ₹199+")
						print("Thankful and Grateful to Have You as a Customer.😊🙏🏻")
					elif f9==6:
						print("Voucher send on your mobile number☎")
						print("Free delivery on first 4 orders worth ₹150+")
						print("Voucher amount is:-",f10)
						print("With heartfelt appreciation, thank you for your recent purchase!😊🙏🏻")
					elif f9==7:
						print("Voucher send on your mobile number☎")
						print("Voucher after discount🏷 amount is:-",f10+f10*0.25)
						print("Flat 25% Off* Upto ₹100 on your first 5 Uber Auto Rides🚖")
						print("Thank you for choosing us to fulfill your needs!😊🙏🏻")
					else:
						print("Error404")
		elif c==4:
			c1=int(input("Verify Mobile Number:-"))
			c2=int(input("Enter OTP\n:-"))
			c3=str(input("Enter Your permanent address\n:-"))
			print("(Multicity Cheques will be issued on your request on this portal🌐. If you desire to have a normal cheque book.\nkindly contact your home branch🏦 for the purpose.\nCharges @3 per cheque leaf for all Savings Bank🏛 accounts having Quarterly Average Balance (QAB) as on \nprevious quarter end below 25,000")
			print("Charges @ 2 per cheque leaf for accounts having QAB 25000 and above as on previous⬅️ quarter end.")
			print("50 Leaves free per year📆 for senior citizen👴👵/salary accounts and 20 leaves free per year for other \nP-Segment/AGL Segment customers)")
			if c1:
				print("Your cheque book(s) will be dispatched at the following address within 3 working days")
				print("Cheque book📒(s) will be delivered📦 at the following address📫\n",c3)
				print("Your request has been registered successfully✅\n",accountinfo)
				print("thanks for choosing us🙌")
			else:
				print("Error")
		elif c==5:
			g1=int(input("1.Mobile recharge\n2.Dth payments\n:-"))
			if g1==1:
				g2=int(input("Enter 10 digit mobile number☎️\n:-"))
				g3=str(input("Enter SIM💾Operator:- "))
				g4=str(input("Select Plan:-\n₹179 2GB/Pack validity 30 Days\n₹199 3GB/Pack validity 28 day\n₹239 1.5GB/Day validity 28 day\n₹279 2GB/Pack validity 45 day\n₹519 1.5GB/Day validity 56 day\nType any alphabet and press enter key to continue😊\n:-"))
				g5=int(input("Enter Amount:- ₹"))
				if g5==179:
					print("Successfully✅")
					print("Recharge amount is:-",g5)
					print("Plan details:- 2GB/Pack validity 30 Days")
				elif g5==199:
					print("Successfully✅")
					print("Recharge amount is:-",g5)
					print("Plan details:- 3GB/Pack validity 28 day")
				elif g5==239:
					print("Successfully✅")
					print("Recharge amount is:-",g5)
					print("Plan details:- 1.5GB/Day validity 28 day")
				elif g5==279:
					print("Successfully✅")
					print("Recharge amount is:-",g5)
					print("Plan details:- 2GB/Pack validity 45 day")
				elif g5==519:
					print("Successfully✅")
					print("Recharge amount is:-",g5)
					print("Plan details:- 1.5GB/Day validity 56 day")
				else:
					print("please select correct plan😊")
			elif g1==2:
				g6=str(input("Enter Your DTH📺Operator:-"))
				g7=str(input("Enter Customer👨‍💼ID:-"))
				g8=str(input("₹247 for 1 Month with 74 Channels\n₹360 for 1 Month with 121 Channels\n₹1,406 with 72 Channels for 12 Months\n₹1,837 for 6 Months with 72 Channels\n₹1,343 for 12 Months with 115 Channels\nType any alphabet and press enter key to continue😊\n:-"))
				g9=int(input("Enter Amount:- ₹"))
				if g9==247:
					print("Successfully✅")
					print("Recharge amount is:-",g9)
					print("Plan details:- TV Hindi Value Lite SD Pack New for 1 Month with 74 Channels")
				elif g9==360:
					print("Successfully✅")
					print("Recharge amount is:-",g9)
					print("Plan details:- Digital TV Hindi Value Sports SD Pack New for 1 Month with 121 Channels")
				elif g9==1406:
					print("Successfully✅")
					print("Recharge amount is:-",g9)
					print("Plan details:- Digital TV Uttam UDP 12M HD Pack with 72 Channels for 12 Months")
				elif g9==1837:
					print("Successfully✅")
					print("Recharge amount is:-",g9)
					print("Plan details:- Digital TV Hindi Value Sports Lite for 6 Months with 72 Channels")
				elif g9==1343:
					print("Successfully✅")
					print("Recharge amount is:-",g9)
					print("Plan details:- Digital TV TN Ssp Pack With Kids for 12 Months with 115 Channels")
				else:
					print("please select correct plan😊")
			else:
				print("Please enter right keyword")
		elif c==6:
			print("24/7 customer support is a service that provides customers with assistance at all times of the day, regardless of time zone.")
			print("Customer care number 112")
	else:
		print("Wrong Password")
else:
	print("The details that you've entered is incorrect. Please try again☹ ")