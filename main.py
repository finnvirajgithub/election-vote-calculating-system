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
  
  try:
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
  
  except:
    database_error()
    
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
  
  try:
    view_citizen = 'SELECT * FROM citizen'
    mycursor.execute(view_citizen)
    citizens = mycursor.fetchall()
    
    for citizen in citizens:
      print("\t\tNIC                     : ", citizen[0])
      print("\t\tName                    : ", citizen[1])
      print("\t\tAge                     : ", citizen[2])
      print("\t\tProvince                : ", citizen[3])
      print("\n\n\n")

  except:
    database_error()
  goBack()
  
  
#check citizen valid or not

def check_validity():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  #get nic
  input_nic = input("Enter the NIC : ")
  print("\n\n\n")
  
  try:
    #check nic in citizen table
    get_citizen_details = 'SELECT * FROM citizen'
    mycursor.execute(get_citizen_details)
    citizen_details = mycursor.fetchall()
  
  except:
    database_error()
  
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
  
  try:
    get_vote_details = 'SELECT * FROM vote'
    mycursor.execute(get_vote_details)
    vote_details = mycursor.fetchall()
  
  except:
    database_error()
  
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

  try:
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
        goBack()
      else:
        print("\t\tYou can't vote another province candidates.")
    
  except:
    database_error()
  
  goBack()

#show chart province wise
def province_wise():
  
  try:
    sql = "SELECT province, COUNT(*) FROM vote GROUP BY province"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    
  except:
    database_error()
  
  provinces = []
  counts = []
  
  for row in data:
    province = row[0]
    count = row[1]
    provinces.append(province)
    counts.append(count)
  
  #plot bar chats
  
  plt.bar(provinces, counts)
  plt.xlabel('Provinces')
  plt.ylabel('Votes')
  plt.title('Votes in Province wise')
  plt.show()
  goBack()
  

#plot chart party wise
def party_wise():
  
  try:
    sql = "SELECT party, COUNT(*) FROM vote GROUP BY party"
    mycursor.execute(sql)
    data = mycursor.fetchall()
  
  except:
    database_error()
  
  parties = []
  counts = []
  
  for row in data:
    party = row[0]
    count = row[1]
    parties.append(party)
    counts.append(count)
  
  #plot bar chats
  
  plt.bar(parties, counts)
  plt.xlabel('Parties')
  plt.ylabel('Votes')
  plt.title('Votes in party wise')
  plt.show()
  goBack()
  

#plot charts candidate wise
def candidate_wise():
  
  try:
    sql = "SELECT electtion_No, COUNT(*) FROM vote GROUP BY electtion_No"
    mycursor.execute(sql)
    data = mycursor.fetchall()
  
  except:
    database_error()
  
  candidates = []
  counts = []
  
  for row in data:
    candidate = row[0]
    count = row[1]
    candidates.append(candidate)
    counts.append(count)
  
  #plot bar chats
  
  plt.bar(candidates, counts)
  plt.xlabel('Candidates')
  plt.ylabel('Votes')
  plt.title('Votes in candidate wise')
  plt.show()
  goBack()


 
def view_results():
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")
  
  print("\t\t\t1.Province wise Votes")
  print("\t\t\t2.Party wise Votes")
  print("\t\t\t3.Candidate wise Votes\n\n")
  
  user_input = int(input("\t\tEnter A Value : "))
  
  if (user_input==1):
    province_wise()
    
  elif (user_input==2):
    party_wise()
    
  elif (user_input==3):
    candidate_wise()

#Route to the main menu
def goBack():
  user_input = input("\n\n\t\t To go back to main menu please enter 'E' or 'e' :")
  
  if (user_input=='E' or user_input=='e'):
    main()

#Error handling
#Error in database
def database_error():
  print("\n\n\t\tProblem with database") 
  goBack()
  

#Main function
def main():  
  os.system('cls')
  print("\n\n------------------------ELECTION VOTING SYSTEM------------------------\n\n\n")

  print("\t\t\t1. Add A Candidates")
  print("\t\t\t2. View candidates")
  print("\t\t\t3. Add a citizen")
  print("\t\t\t4. View citizens")
  print("\t\t\t5. Add A Votecls")
  print("\t\t\t6. View results")
  print("\t\t\t7. Exit\n\n")

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
  
  elif (user_input==7):
    exit()

main()


  
  
  