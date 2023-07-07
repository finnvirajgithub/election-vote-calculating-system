from dbconnect import conn, mycursor
import os

#classes

class Citizen():
  def __init__(self,name,NIC,age,province):
    self.name = name
    self.NIC = NIC
    self.age = age
    self.province = province
    
    sql = 'INSERT INTO citizen VALUES(%s,%s,%s,%s)'
    values = (self.NIC, self.name, self.age, self.province)
    mycursor.execute(sql,values)
    conn.commit()
    
  def display_citizen(self):
    pass

class Candidate(Citizen):
  def __init__(self, name, NIC, age, party, province, edu):
    super().__init__(name, NIC, age, province)
    self.party = party
    self.edu = edu
    
    sql = 'INSERT INTO candidate VALUES(%s,%s,%s,%s,%s,%s)'
    values = (self.NIC, self.name, self.age, self.party, self.province, self.edu)
    mycursor.execute(sql,values)
    conn.commit()


#Add candidates

def add_candidate():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  name = input("\t\tEnter the name : ")
  nic = input("\t\tEnter the NIC number : ")
  age = int(input("\t\tEnter the age : "))
  party = input("\t\tEnter the Political Party : ")
  province = input("\t\tEnter the province : ")
  edu = input("\t\tEnter the education qualifications(No O/L / O/L / A/L / Graduate) : ")
  
  name = Candidate(name,nic,age,party,province,edu)

  goBack()
  
  
#View Candidates

def view_candidate():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  view_candidate = 'SELECT * FROM candidate'
  mycursor.execute(view_candidate)
  candidates = mycursor.fetchall()
  
  for candidate in candidates:
    print("\t\tNIC                     : ", candidate[0])
    print("\t\tName                    : ", candidate[1])
    print("\t\tAge                     : ", candidate[2])
    print("\t\tParty                   : ", candidate[3])
    print("\t\tProvince                : ", candidate[4])
    print("\t\tEducation qualification : ", candidate[5])
    print("\n\n\n")
  
  goBack()
  
  
#Add citizen

def add_citizen():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  name = input("\t\tEnter the name : ")
  nic = input("\t\tEnter the NIC number : ")
  age = int(input("\t\tEnter the age : "))
  province = input("\t\tEnter the province : ")
  
  name = Citizen(name,nic,age,province)

  goBack()
  
  
#View Citizens

def view_citizen():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  view_citizen = 'SELECT * FROM citizen'
  mycursor.execute(view_citizen)
  citizens = mycursor.fetchall()
  
  for citizen in citizens:
    print("\t\tNIC                     : ", citizen[0])
    print("\t\tName                    : ", citizen[1])
    print("\t\tAge                     : ", citizen[2])
    print("\t\tProvince                : ", citizen[3])
    print("\n\n\n")

  goBack()
  
  
def add_vote():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  

def goBack():
  user_input = input("\t\t To go back to main menu please enter 'E' or 'e' :")
  
  if (user_input=='E' or user_input=='e'):
    main()
  
def main():  
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")

  print("\t\t\t1. Add A Candidates")
  print("\t\t\t2. View candidates")
  print("\t\t\t3. Add a citizen")
  print("\t\t\t4. View citizens")
  print("\t\t\t5. Add A Vote\n\n")

  user_input = int(input("Enter A Value : "))

    
  if (user_input==1):
    add_candidate()
    
  elif (user_input==2):
    view_candidate()
    
  elif (user_input==3):
    add_citizen()
    
  elif (user_input==4):
    view_citizen()
    
  elif (user_input==5):
    add_vote()

main()


  
  
  