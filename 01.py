from dbconnect import conn, mycursor
import os

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

def view_candidate():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  

def add_citizen():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  name = input("\t\tEnter the name : ")
  nic = input("\t\tEnter the NIC number : ")
  age = int(input("\t\tEnter the age : "))
  province = input("\t\tEnter the province : ")
  
  name = Citizen(name,nic,age,province)

def view_citizen():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")

def add_vote():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  
  
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




  
  
  