print("Welcome to Math Helper😊🙏🏻")
print("Solve math problems anytime⏳, anywhere👨🏻‍💻")
pr="thanks for using our services😊🙏🏻"
x=int(input("1.Basic\n2.Table\n3.Square root\n4.Cube root\n5.Sum of N Terms\n6.Use formulas\n7.Find Percentage of your result\n:-"))
if x==1:
	z=(int(input("1.Counting🔢\n2.Whole numbers🔢\n3.Natural numbers🔢\n4.Addition➕\n5.Subtraction➖\n6.Division➗\n7.Multiplication❌\n8.Even numbers🔢\n9.Odd numbers🔢\n10.Find Percentage%\n:-")))
	if z==1:
		c=int(input("Counting Numbers upto:- "))
		for i in range(0,c):
			print(i+1)
		print(pr)
	elif z==2:
		c=int(input("Whole Numbers upto:- "))
		for i in range(-1,c):
			print(i+1)
		print(pr)
	elif z==3:
		c=int(input("Natural Numbers upto:- "))
		for i in range(0,c):
			print(i+1)
		print(pr)
	elif z==4:
		bl=[]
		m2=int(input("How many numbers in your list:- "))
		for i in range (m2):
			bl.append(int(input("Enter number one by one:- ")))
		m=sum(bl)
		print("Sum of your numbers:- ",m)
		print(pr)
	elif z==5:
		x=int(input("Enter number:-"))
		x2=int(input('Enter 2nd number:-'))
		print("Subtraction of number is:-",x-x2)
		print(pr)
	elif z==6:
		x=int(input("Enter number:-"))
		x2=int(input('Enter 2nd number:-'))
		print("Ans is:-",x/x2)
		print(pr)
	elif z==7:
		x=int(input("Enter number:-"))
		x2=int(input('Enter 2nd number:-'))
		print("Ans is:-",x*x2)
		print(pr)
	elif z==8:
		c=int(input("Even Numbers upto:- "))
		for i in range(1,c):
			if i%2==0:
				print("Even numbers :-",i)
		print(pr)
	elif z==9:
		c=int(input("Even Numbers upto:- "))
		for i in range(1,c):
			if i%2!=0:
				print("Even numbers :-",i)
		print(pr)
	elif z==10:
		x=int(input("Enter Actual Value:-"))
		y=int(input("Enter  Total Value:-"))
		a=x/y*100
		a=int(a)
		print("Percentage:-",a,"%")
		print(pr)
	else:
		print("Error")
elif x==2:
	t1=1
	t=int(input("which table you need:- "))
	for i in range(0,10):
		print(t,"X",t1,"=",t*t1)
		t1=t1+1
	print(pr)
elif x==3:
	t1=1
	s=int(input("Which number you need to find square root:- "))
	for i in range(0,11):
		if i:
			print(s**2*t1)
			t1=t1+1
	print(pr)
elif x==4:
	t1=1
	c=int(input("Which number you need to find cube root:- "))
	for i in range(0,11):
		if i:
			print(c**3*t1)
			t1=t1+1
	print(pr)
elif x==5:
	bl=[]
	x=(int(input("Enter N:-")))
	for i in range(0,x):
		bl.append(i+1)
	print(sum(bl))
	print(pr)
elif x==6:
	f=int(input("1.Geometry Formulas\n2.Algebra Identities\n3.Surface Area and Volume Formulas\n4.Statistics\n5.Class 11th and 12th Formulas\n:-"))
	if f==1:
		f1=int(input("1.Triangle📐\n2.Rectangle\n3.Square\n4.Parallelogram\n5.Rhombus\n6.Trapezium\n7.Circle\n8.Cylinder\n9.Cone\n10.Sphere\n:-"))
		if f1==1:
			a1=int(input("1.Area\n2.Perimeter\n:-"))
			if a1==1:
				tr=int(input("Enter Triangle Base:- "))
				tr1=int(input("Enter Base:- "))
				print("Area of Triangle📐 =",tr*tr1/2)
				print(pr)
			elif a1==2:
				tr2=int(input("Enter first side:-"))
				tr3=int(input("Enter second side:-"))
				tr4=int(input("Enter third side:-"))
				print("Perimeter of Triangle📐 =",tr2+tr3+tr4)
				print(pr)
			else:
				print("Error")
		elif f1==2:
			re=int(input("1.Area\n2.Perimeter\n:-"))
			if re==1:
				re1=int(input("Enter length of Rectangle:-"))
				re2=int(input("Enter breadth of Rectangle:-"))
				print("Area of rectangle:-",re1*re2)
				print(pr)
			elif re==2:
				re3=int(input("Enter length of Rectangle:-"))
				re4=int(input("Enter breadth of Rectangle:-"))
				print("Perimeter of rectangle =",2*re3*re4)
				print(pr)
			else:
				print("Error")
		elif f1==3:
			sq=int(input("1.Area\n2.Perimeter\n:-"))
			if sq==1:
				sq1=int(input("Enter Length of the Side:-"))
				print("Area of square is:-",sq1**2)
				print(pr)
			elif sq==2:
				sq2=int(input("Enter Length of the Side:-"))
				print("Perimeter of square =",4*sq2)
				print(pr)
			else:
				print("Error")
		elif f1==4:
			pl=int(input("1.Area\n2.Perimeter\n:-"))
			if p1==1:
				pl1=int(input("Enter base of Parallelogram:-"))
				pl2=int(input("Enter height of Parallelogram:-"))
				print("Area	of Parallelogram is:-",pl1*pl2)
				print(pr)
			elif p1==2:
				pl3=int(input("Enter base of Parallelogram:-"))
				pl4=int(input("Enter side of Parallelogram:-"))
				print("Perimeter of Parallelogram =",2*pl3+pl4)
				print(pr)
			else:
				print("Error")
		elif f1==5:
			rm=int(input("1.Area\n2.Perimeter\n:-"))
			if rm==1:
				rm1=int(input("Enter the 1st diagonal of the rhombus:-"))
				rm2=int(input("Enter the 2nd diagonal of the rhombus:-"))
				print("Area	of Rhombus is:-",(rm1*rm2)/2)
				print(pr)
			elif rm==2:
				rm3=int(input("Enter side of Rhombus:-"))
				print("Perimeter of Rhombus =",4*rm3)
				print(pr)
			else:
				print("Error")
		elif f1==6:
			tz=int(input("1.Area\n2.Perimeter\n:-"))
			if tz==1:
				tz1=int(input("Enter Trapezium base 1:-"))
				tz2=int(input("Enter Trapezium base 2:-"))
				tz3=int(input("Enter Trapezium height :-"))
				print("Area of Trapezium",(tz1+tz2)/2*tz3)
				print(pr)
			elif tz==2:
				tz4=int(input("Enter 1st side:-"))
				tz5=int(input("Enter 2nd side:-"))
				tz6=int(input("Enter 3rd side:-"))
				tz7=int(input("Enter 4rth side:-"))
				print(tz4+tz5+tz6+tz7)
				print(pr)
			else:
				print("Error")
		elif f1==7:
			cr=int(input("1.Area\n2.Circumference\n:-"))
			if cr==1:
				cr1=int(input("Enter radius of Circle:-"))
				print("Area of Circle =",3.142*(cr1*cr1))
				print(pr)
			elif cr==2:
				cr2=int(input("Enter radius of Circle:-"))
				print("Circumference of Circle =",(2*3.142)*cr2)
				print(pr)
			else:
				print("Error")
		elif f1==8:
			cl=int(input("1.Surface Area of Cylinder\n2.Volume of Cylinder\n:-"))
			if cl==1:
				cl1=int(input("Enter height of Cylinder:-"))
				cl2=int(input("Enter radius of Cylinder:-"))
				print("Surface Area of Cylinder is =",(2*3.142)*cl2*(cl1+cl2))
				print(pr)
			elif cl==2:
				cl3=int(input("Enter height of Cylinder:-"))
				cl4=int(input("Enter radius of Cylinder:-"))
				print("Volume of Cylinder is =",3.142*(cl4*cl4)*cl3)
				print(pr)
			else:
				print("Error")
		elif f1==9:
			cn=int(input("1.Surface Area of Cone\n2.Volume of Cone\n:-"))
			if cn==1:
				cn1=int(input("Enter radius of Cone:-"))
				cn2=int(input("Enter slant height of cone:-"))
				print("Surface Area of Cone is =",3.142*cn1*(cn1+cn2))
				print(pr)
			elif cn==2:
				cn1=int(input("Enter radius of Cone:-"))
				cn2=int(input("Enter height of cone:-"))				
				print("Volume of Cone is =",3.142*(cn1*cn1)*cn2/3)
				print(pr)
			else:
				print("Error")
		elif f1==10:
			sp=int(input("1.Surface Area of sphere\n2.Volume "))
			if f2==1:
				sp1=int(input("Enter radius of sphere:-"))
				print("Surface Area of surface are =",4*3.142*(sp1*sp1))
				print(pr)
			elif f2==2:
				sp2=int(input("Enter radius of sphere:-"))
				print("Volume of sphere is =",4/3*3.142*sp2**3)
				print(pr)
			else:
				print("Error")
		else:
			print("Error")
	elif f==2:
		a=int(input("1.Square of a Sum{(a+b)2=a2+2ab+b2}\n2.Square of a Difference{(a−b)2=a2−2ab+b2}\n3.Product of a Sum and a Difference{(a+b)(a−b)=a2−b2}\n4.Cube of a Sum{(a+b)3=a3+b3+3ab(a+b)}\n5.Cube of a Difference{(a−b)3=a3−b3−3ab(a−b)}\n6.Sum of Cubes{a3+b3=(a+b)(a2−ab+b2)}\n7.Difference of Cubes{a3−b3=(a−b)(a2+ab+b2)}\n8.Square of a Binomial Sum{(x+y+z)2=x2+y2+z2+2xy+2yz+2zx}\n9.Sum of Squares of Three Terms{x2+y2+z2=(x+y+z)2−2(xy+yz+zx)}\n10.Square of a Binomial Difference{(x−y−z)2=x2+y2+z2−2xy+2yz−2zx}\n:-"))
		if a==1:
			print("Please enter values of a and b")
			v=int(input("a ="))
			v1=int(input("b ="))
			print("Square of a Sum is =",(v*v)+(2*v*v1)+(v1*v1))
			print(pr)
		elif a==2:
			print("Please enter values of a and b")
			v=int(input("a ="))
			v1=int(input("b ="))
			print("Square of a Difference is =",(v*v)-(2*v*v1)+(v1*v1))
			print(pr)
		elif a==3:
			print("Please enter values of a and b")
			v=int(input("a ="))
			v1=int(input("b ="))
			print("Product of a Sum and a Difference is =",(v+v1)*(v-v1))
			print(pr)
		elif a==4:
			print("Please enter values of a and b")
			v=int(input("a ="))
			v1=int(input("b ="))
			print("Cube of a Sum is =",(v**3)+(v1**3)+(3*v*v1)*(v+v1))
			print(pr)
		elif a==5:
			print("Please enter values of a and b")
			v=int(input("a ="))
			v1=int(input("b ="))
			print("Cube of a Difference is =",(v**3)-(v1**3)-(3*v*v1)*(v-v1))
			print(pr)
		elif a==6:
			print("Please enter values of a and b")
			v=int(input("a ="))
			v1=int(input("b ="))
			print("Sum of Cubes is =",(v+v1)*(v*v-v*v1+v1*v1))
			print(pr)
		elif a==7:
			print("Please enter values of a and b")
			v=int(input("a ="))
			v1=int(input("b ="))
			print("Difference of Cubes is =",(v-v1)*(v*v+v*v1+v1*v1))
			print(pr)
		elif a==8:
			print("Please enter values of a,b and c")
			v=int(input("a ="))
			v1=int(input("b ="))
			v2=int(input("c ="))
			print("Square of a Binomial Sum is =",(v*v)+(v1*v1)+(v2*v2)+(2*v*v1)+(2*v1*v2)+(2*v2*v))
			print(pr)
		elif a==9:
			print("Please enter values of a,b and c")
			v=int(input("a ="))
			v1=int(input("b ="))
			v2=int(input("c ="))
			print("Sum of Squares of Three Terms is =",(v+v1+v2)**2-(2*(v*v1+v1*v2+v2*v)))
			print(pr)
		elif a==10:
			print("Please enter values of a,b and c")
			v=int(input("a ="))
			v1=int(input("b ="))
			v2=int(input("c ="))
			print("Square of a Binomial Difference is =",(v*v)+(v1*v1)+(v2*v2)-(2*v*v1)+(2*v1*v2)-(2*v2*v))
			print(pr)
		else:
			print("Error")
	elif f==3:
		sh=int(input("1.Cuboid\n2.Cube\n3.Cylinder\n4.Cone\n5.Sphere\n6.Hemisphere\n7.Prism\n:-"))
		if sh==1:
			sh1=int(input("1.Find surface area\n2.Find Volume of Cuboid\n:-"))
			if sh1==1:
				print("Please enter length,Breadth and Height")
				sh2=int(input("Enter length ="))
				sh3=int(input("Enter breadth ="))
				sh4=int(input("Enter height ="))
				print("Surface area of Cuboid is =",2*(sh2*sh3+sh3*sh4+sh4*sh2))
				print(pr)
			elif sh1==2:
				print("Please enter length,Breadth and Height")
				sh2=int(input("Enter length ="))
				sh3=int(input("Enter breadth ="))
				sh4=int(input("Enter height ="))
				print("Volume of Cuboid is =",sh2*sh3*sh4)
				print(pr)
			else:
				print("Error")
		elif sh==2:
			sh1=int(input("1.Find surface area\n2.Find Volume of Cuboid\n:-"))
			if sh1==1:
				sh2=int(input("Please enter length of cube ="))
				print("Surface Area of cube is =",6*sh2*sh2)
				print(pr)
			elif sh1==2:
				sh2=int(input("Please enter length of cube ="))
				print("Volume of cube is =",sh2**3)
				print(pr)
			else:
				print("Error")
		elif sh==3:
			cy=int(input("1.CSA(Curved Surface Area)\n2.TSA(Total Surface Area)\n3.Volume\n:-"))
			if cy==1:
				print("Please enter Radius and Height")
				ra=int(input("Enter radius ="))
				he=int(input("Enter height ="))
				print("Curved Surface Area of Cylinder is =",2*3.142*ra*he)
				print(pr)
			elif cy==2:
				print("Please enter Radius and Height")
				ra=int(input("Enter radius ="))
				he=int(input("Enter height ="))
				print("Total Surface Area of Cylinder is =",2*3.142*ra*(ra+he))
				print(pr)
			elif cy==3:
				print("Please enter Radius and Height")
				ra=int(input("Enter radius ="))
				he=int(input("Enter height ="))
				print("Volume of Cylinder is =",3.142*(ra*ra)*he)
				print(pr)
			else:
				print("Error")
		elif sh==4:
			cy=int(input("1.CSA(Curved Surface Area)\n2.TSA(Total Surface Area)\n3.Volume\n:-"))
			if cy==1:
				print("Please enter Radius and length")
				ra=int(input("Enter radius ="))
				sh2=int(input("Enter length ="))
				print("Curved Surface Area of Cone is =",3.142*ra*sh2)
				print(pr)
			elif cy==2:
				print("Please enter Radius and length")
				ra=int(input("Enter radius ="))
				sh2=int(input("Enter length ="))
				print("Total Surface Area of Cone is =",3.142*ra*(ra+sh2))
				print(pr)
			elif cy==3:
				print("Please enter Radius and length")
				ra=int(input("Enter radius ="))
				he=int(input("Enter height ="))
				print("Volume of Cone is =",1/3*3.142*(ra*ra)*he)
				print(pr)
			else:
				print("Error")
		elif sh==5:
			cy=int(input("1.Surface Area and LSA\n2.Volume\n:-"))
			if cy==1:
				ra=int(input("Enter radius ="))
				print("Surface Area of sphere is =",4*3.142*(ra*ra))
				print(pr)
			elif cy==2:
				ra=int(input("Enter radius ="))
				print("Volume of sphere is =",4/3*3.142*(ra**3))
				print(pr)
			else:
				print("Error")
		elif sh==6:
			cy=int(input("1.CSA(Curved Surface Area)\n2.TSA(Total Surface Area)\n3.Volume\n:-"))
			if cy==1:
				ra=int(input("Enter radius ="))
				print("Curved Surface Area of Hemisphere is =",2*3.142*(ra*ra))
				print(pr)
			elif cy==2:
				ra=int(input("Enter radius ="))
				print("Total Surface Area of Hemisphere is =",3*3.142*(ra*ra))
				print(pr)
			elif cy==3:
				ra=int(input("Enter radius ="))
				print("Volume of Hemisphere is =",2/3*3.142*(ra**3))
				print(pr)
			else:
				print("Error")
		elif sh==7:
			cy=int(input("1.Surface Area)\n2.Volume\n:-"))
			if cy==1:
				sh2=int(input("Enter length ="))
				w=int(input("Enter Width ="))
				he=int(input("Enter height ="))
				pe=2*sh2+2*w
				print("Perimeter =",pe)
				area=sh2*w
				print("Area =",area)
				print("Surface area of Prism =",2*area+pe*he)
				print(pr)
			elif cy==2:
				sh2=int(input("Enter length ="))
				w=int(input("Enter Width ="))
				he=int(input("Enter height ="))
				area=sh2*w
				print("Area =",area)
				print("Volume of Prism is =",area*h)
				print(pr)
			else:
				print("Error")
		else:
			print("Error")
	elif f==4:
		m=int(input("1.Mean\n2.Median\n3.Mode\n:-"))
		if m==1:
			bl=[]
			m2=int(input("How many numbers in your list:- "))
			for i in range (m2):
				bl.append(int(input("Enter number one by one:- ")))
			print(bl)
			m=sum(bl)
			m3=int(m/m2)
			print("Mean =",m3)
			print(pr)
		elif m==2:
			import statistics
			bl=[]
			m2=int(input("How many numbers in your list:- "))
			for i in range (m2):
				bl.append(int(input("Enter number one by one:- ")))
			print(statistics.median(bl))
			print(pr)
		elif m==3:
			import statistics
			bl=[]
			m2=int(input("How many numbers in your list:- "))
			for i in range (m2):
				bl.append(int(input("Enter number one by one:- ")))
			print(statistics.mode(bl))
			print(pr)
	elif f==5:
		c1=int(input("1.Algebra Formulas\n2.Vector Formulas\n:-"))
		if c1==1:
			fo=int(input("1.Distributive property{a(b+c)=ab+ac }\n2.Commutative Property of Addition{a+b=b+a}\n3.Commutative Property of Multiplication{ab=ba}\n4.Associative Property of Addition{a+(b+c)=(a+b)+c}\n5.Associative Property of Multiplication{a(bc)=(ab)c}\n6.Additive Identity Property{a+0=a}\n7.Multiplicative Identity Property{a×1=a}\n8.Additive Inverse Property{a+(-a)=0}\n9.Multiplicative Inverse Property{a⋅(1/a)=1}\n10.Zero Property of Multiplication{a(0)=0}\n:-"))
			if fo==1:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				c=int(input("c ="))
				print("Ans =",(a*b)+(a*c))
				print(pr)
			elif fo==2:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				print("Ans =",b+a)
				print(pr)
			elif fo==3:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				print("Ans =",b*a)
				print(pr)
			elif fo==4:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				c=int(input("c ="))
				print("Ans =",(a+b)+c)
				print(pr)
			elif fo==5:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				c=int(input("c ="))
				print("Ans =",(a*b)*c)
				print(pr)
			elif fo==6:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				print("Ans =",a)
				print(pr)
			elif fo==7:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				print("Ans =",a)
				print(pr)
			elif fo==8:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				print("Ans =",0)
				print(pr)
			elif fo==9:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				print("Ans =",1)
				print(pr)
			elif fo==10:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				print("Ans =",0)
				print(pr)
			else:
				print("Error")
		elif c1==2:
			fo=int(input("1.Commutative Law{A+B=B+A}\n2.Associative Law{A+(B+C)=(A+B)+C}\n3.Dot Product{(A•B)=|P||Q|cosθ}\n4.Cross Product{(A×B)=|P||Q|sinθ}\n5.k(A+B)=kA+kB\n6.Additive Identity{A+0=0+A}\n:-"))
			if fo==1:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				print("Ans =",b+a)
				print(pr)
			elif fo==2:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				c=int(input("c ="))
				print("Ans =",(a+b)*+c)
				print(pr)
			elif fo==3:
				print("Error")
			elif fo==4:
				print("Error")
			elif fo==5:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				b=int(input("b ="))
				k=int(input("k ="))
				print("Ans =",(k*a)+(k*b))
				print(pr)
			elif fo==6:
				print("Please enter values of a,b and c")
				a=int(input("a ="))
				print("Ans =",a)
				print(pr)
			else :
				print("Error")
		else:
			print("Error")
elif x==7:
	a=[]
	a1=int(input("Enter your Total subject no.:-"))
	for i in range(0,a1):
		x=int(input("Enter subject marks one by one:-"))
		a.append(x)
	b=sum(a)
	print("Your Percentage is:-",b/a1,"%")
	print(pr)
else:
	print("Please re checck details")