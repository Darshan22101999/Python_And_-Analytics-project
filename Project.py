import mysql.connector
import pandas as p
import csv
import matplotlib.pyplot as plt
import numpy as np

# establishing the connection with mysql
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

# getting the cursor object to execute queries
c=mydb.cursor()
#c.execute("create database Project")

#c.execute("use Project")

#c.execute("create table if not exists music_instrument_shop(INSTRUMENT varchar(90),user_preference int,Brand varchar(90),M_R_P int,Material_type varchar(90))")

def add_instru():
	Instrument=input("Enter the name of instrument that you want to enter: ")
	user_preference=input("ENter the number of instrument that you want to order: ")
	Brand=input("Enter the brand name you want to order: ")
	M_R_P=input("Enter the price of instrument for cart evaluation: ")
	Material_type=input("Enter the material type of instrument: ")
	
	sql="Insert into Music_instrument_shop values(%s,%s,%s,%s,%s)"
	val=(Instrument,user_preference,Brand,M_R_P,Material_type)
	c.execute(sql,val)
	mydb.commit()
	return c




dictionary={"darsh22":996725}

def password_check():
	global dictionary
	Login_ID=input("Enter Login Id : ")	# to take username
	Password=int(input("Enter Password: "))	# to take password
	if (Login_ID,Password) in dictionary.items() :#username in dictionary: #for checking username
				print("Login_ID and Password are present")
				while True:
					print("1.Add a Instrument \n 2. View all Instrument, Quantity and M_R_P \n 3.Delete an Instrument \n 4. Add to cart \n 5. Total of cart value and payment  \n 6.Graphs  \n7.Exit ")
					choice=int(input("Please enter your choice: "))
						
					if choice==1:
						print("ADD THE INSTRUMENT you want to buy\n")
						
						name=input("how many records you want to write: ")
						material=input("enter Material: ")
						type=input("Enter Type you want to store: ")
						brand=input("Enter brand you want to store: ")
						mrp=int(input("ENter the price of instrument you wannt to add: "))
						stock=int(input("ENter the recent amount of instrument you want to store: "))
						
						with open("save file_1.csv","a",newline="") as f:
							writer=csv.writer(f)
							writer.writerow([name,material,type,brand,mrp,stock])
						f.close()	
						print("The instrument is added into the data. ")
					elif choice==2:
						print("View all Instrument, Quantity and M_R_P. ")
						print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
						csv_1=p.read_csv("save file_1.csv", encoding="ISO-8859-1" ) 
						print(csv_1) 
						print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
						print("\nM_R_P maybe increased based on the type and material of your instrument. This is the minimum amount of instrument")
						
					elif choice==3:
						class remove_instrument():
								def delete_instrument(self):
										
										self.name=input("Enter the name to check: ")
										self.Brand=input("Enter the brand name to check: ")
										c.execute('select * from music_instrument_shop')
										result=c.fetchall()
										for x in result:
											if self.name==(x[0]):
												if self.Brand==(x[1]):											
														c.execute(f'delete from music_instrument_shop where name="{self.name}",Brand="{self.Brand}"')
														print("instrument deleted sucessfully")
														mydb.commit()
														break
											
											mydb.commit()
						d=remove_instrument()
						d.delete_instrument()
						
					elif choice==4:
						print("Enter the details of your instrument that you want to buy ")
						print("--------------------------------------------------------------------")
						add_instru()
	
					elif choice==5:
						print("--------------------------------------------------------------------")
						c.execute("Select Sum(M_R_P) from music_instrument_shop ")
						result = c.fetchall()
						for i in result:
							print("The total cart value is: ",i[0])
						
						print("Do you want to go for payment or Do it later? Y/ N")
						ans=input("Enter your choice: ")
						if ans=="Y":
							print("Enter your card details")
							ca=int(78546855956)
							O=int(112266)
							card_number=int(input("Enter your card number: "))
							OTP=int(input("Enter your OTP to confirm the payment : "))
							if ca == card_number:
								if O==OTP:
									print("Card number is found")
							print("Ap8@tr")
							a="Ap8@tr"
							print("Enter the Above captcha")
							captcha=input("Enter captcha: ")
							if captcha==a:
								print("Payment Done!!!!")
						elif ans=="N":
							print("Ok No Issue Sir Done it later.")
					
					elif choice==6:
						c.execute("select * from  music_instrument_shop")
						result=c.fetchall()
						df=p.DataFrame(result,columns=["INSTRUMENT","user_preference","Brand","M_R_P","Material"])
						
						def bar():
							f=input("enter 1st preference: ")
							c.execute(f'select user_preference from music_instrument_shop where user_preference="{f}"')
							records=c.fetchall()
							first=0
							for x in records:
								if f==x[0]:
									mydb.commit()
									first+=1
							print("1st preference is:",first)

							s=input("Enter Brande name: ")
							c.execute(f'select Brand from music_instrument_shop where Brand="{s}"')
							records=c.fetchall()
							second=0
							for x in records:
								if s==x[0]:
									mydb.commit()
									second+=1
							print("Brand is : ",second)

							x=np.array([f,s])
							y=np.array([first,second])

							font1 = {'family':'serif','color':'blue','size':20}
							font2 = {'family':'serif','color':'green','size':10}

							plt.bar(x,y,color="blue",width=0.2)
							plt.xlabel("Name of user_preference",fontdict=font2)
							plt.ylabel("Number of Brand",fontdict=font2)
							plt.title("Bar Chart",fontdict=font1)
							plt.show()
						bar()	
					
						def piechart():
						
									f=input("enter 1st preference: ")
									c.execute(f'select user_preference from music_instrument_shop where user_preference="{f}"')
									records=c.fetchall()
									first=0
									for x in records:
										if f==x[0]:
											
											mydb.commit()
											first+=1
									print("1st preference is:",first)

									s=input("Enter 2nd preference: ")
									c.execute(f'select user_preference from music_instrument_shop where user_preference="{s}"')
									records=c.fetchall()
									second=0
									for x in records:
										if s==x[0]:
											
											mydb.commit()
											second+=1
									print("2nd preference is : ",second)
						
									t=input("Enter 3rd preference: ")
									c.execute(f'select user_preference from music_instrument_shop where user_preference="{t}"')
									records=c.fetchall()
									third=0
									for x in records:
										if t==x[0]:
											
											mydb.commit()
											third+=1
									print("3rd preference is :",third)

									y=np.array([first,second,third])
									mylabels =[f,s,t]
									myexplode = [0, 0.2, 0]
									color=["red","blue","green"]
									
									font1 = {'family':'serif','color':'green','size':20}
									plt.title("Pie Chart",fontdict=font1)
									plt.pie(y, labels = mylabels, explode = myexplode,colors=color)
									plt.show()
						piechart()
									
						def scat():
									x=p.array(df['user_preference'])
									y=p.array(df['M_R_P'])
									font1 = {'family':'serif','color':'blue','size':20}
									font2 = {'family':'serif','color':'green','size':10}
									plt.scatter(x, y,color="darkblue")
									plt.xlabel("user_preference",fontdict=font2)
									plt.ylabel("M_R_P",fontdict=font2)
									plt.title("Scattered Chart",fontdict=font1)
									plt.show()
						scat()

						
					elif choice==7:
						print("Thank you for Ordering from our shop. Please Visit Again!!!!")
						break
					else:
						print("Wrong Choice. Please select one of the below menus:")
	else:
		print("Wrong Login_ID or Password.Please check your entered Login_ID and Password and Enter Again!!!")
	return dictionary
password_check()

