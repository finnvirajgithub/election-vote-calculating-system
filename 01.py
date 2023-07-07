from dbconnect import conn, mycursor
import os
import matplotlib.pyplot as plt

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
  def __init__(self, name, NIC, elect_no, age, party, province, edu):
    super().__init__(name, NIC, age, province)
    self.elect_no = elect_no
    self.party = party
    self.edu = edu
    
    sql = 'INSERT INTO candidate VALUES(%s,%s,%s,%s,%s,%s,%s)'
    values = (self.NIC, self.name, self.elect_no, self.age, self.province, self.party, self.edu)
    mycursor.execute(sql,values)
    conn.commit()


#Add candidates

def add_candidate():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  name = input("\t\tEnter the name : ")
  nic = input("\t\tEnter the NIC number : ")
  elect_no = int(input("\t\tEnter the election number : "))
  age = int(input("\t\tEnter the age : "))
  party = input("\t\tEnter the Political Party : ")
  province = input("\t\tEnter the province : ")
  edu = input("\t\tEnter the education qualifications(No O/L / O/L / A/L / Graduate) : ")
  
  name = Candidate(name,nic,elect_no,age,party,province,edu)

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
    print("\t\tElection Number         : ", candidate[2])
    print("\t\tAge                     : ", candidate[3])
    print("\t\tParty                   : ", candidate[4])
    print("\t\tProvince                : ", candidate[5])
    print("\t\tEducation qualification : ", candidate[6])
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
  
  
#check citizen valid or not

def check_validity():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  #get nic
  input_nic = input("Enter the NIC : ")
  print("\n\n\n")
  
  #check nic in citizen table
  get_citizen_details = 'SELECT * FROM citizen'
  mycursor.execute(get_citizen_details)
  citizen_details = mycursor.fetchall()
  
  for nic in citizen_details:
    if (nic[0] == input_nic):
      the_nic = True
      the_age = nic[2]
      the_province = nic[3]
      break
    else:
      the_nic = False
      continue
  
  
  #check age > 18
  if (the_nic):
    if (the_age>18):
      check_past(input_nic,the_province)
    else:
      print("\t\tYou can't vote")
      goBack()
  else:
    print("\t\tYou can't vote") 
    goBack()
  
  
#check past votes

def check_past(nic,province):
  get_vote_details = 'SELECT * FROM vote'
  mycursor.execute(get_vote_details)
  vote_details = mycursor.fetchall()
  
  print(vote_details)
  
  if not vote_details:
    add_vote(nic,province)
  else:
    for vote in vote_details:
      if(vote[1]==nic):
        print("\t\t\You Already voted!")
        goBack()
      else:
        add_vote(nic,province)
  
  
#add vote

def add_vote(nic,province):
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  #get election number
  
  elec_no = int(input("\t\t Enter the Election Number of the candidate : "))
  
  #check citizens province equal to candidates province
  
  get_candidate_details = 'SELECT * FROM candidate WHERE election_number = %s'
  mycursor.execute(get_candidate_details, (elec_no,))
  candidate_details = mycursor.fetchall()
  
  for candidate in candidate_details:
    if (candidate[4]==province):
      #add vote
      sql = 'INSERT INTO vote VALUES (%s,%s,%s,%s,%s)'
      values = (candidate[0],nic,elec_no,candidate[4],candidate[5])
      mycursor.execute(sql,values)
      conn.commit()
    else:
      print("\t\tYou can't vote another province candidates.")
  
  goBack()

#show chart province vice
def province_vise():
  sql = "SELECT province, count(*) FROM vote GROUP BY province"
  mycursor.execute(sql)
  data = mycursor.fetchall()
  
  provinces = []
  counts = []
  
  for row in data:
    province = row[0]
    count = row[1]
    provinces.append(province)
    counts.append(counts)
  
  #create bar chats
  
  plt.bar(provinces, counts)
  plt.xlabel('Provinces')
  plt.ylabel('Votes')
  plt.title('Votes in Province vise')
  plt.show()

def party_vise():
  sql = "SELECT party, count(*) FROM vote GROUP BY party"
  mycursor.execute(sql)
  data = mycursor.fetchall()
  
  parties = []
  counts = []
  
  for row in data:
    party = row[0]
    count = row[1]
    parties.append(party)
    counts.append(counts)
  
  #create bar chats
  
  plt.bar(parties, counts)
  plt.xlabel('Parties')
  plt.ylabel('Votes')
  plt.title('Votes in party vise')
  plt.show()

def candidate_vise():
  sql = "SELECT electtion_No, count(*) FROM vote GROUP BY electtion_No"
  mycursor.execute(sql)
  data = mycursor.fetchall()
  
  candidates = []
  counts = []
  
  for row in data:
    candidate = row[0]
    count = row[1]
    candidates.append(candidate)
    counts.append(counts)
  
  #create bar chats
  
  plt.bar(candidates, counts)
  plt.xlabel('Candidates')
  plt.ylabel('Votes')
  plt.title('Votes in candidate vise')
  plt.show()
  
def view_results():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  print("\t\t\t1.Province vise Votes")
  print("\t\t\t2.Party vise Votes")
  print("\t\t\t1.Candidate vise Votes")
  
  user_input = int(input("Enter A Value : "))
  
  if (user_input==1):
    province_vise()
    
  elif (user_input==2):
    party_vise()
    
  elif (user_input==3):
    candidate_vise()

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
  print("\t\t\t6. View results\n\n")

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
    check_validity()
  
  elif (user_input==6):
    view_results()

main()


  
  
  