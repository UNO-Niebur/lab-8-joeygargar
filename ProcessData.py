#ProcessData.py
#Name: Mia Garcia
#Date: 4/6/26
#Assignment: Lab 8 

import random

def main():

  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  for line in inFile:
    info = line.strip().split(" ")

    first = info[0]
    last = info[1]
    studentID = info[3]
    year = info[5]
    major = info[6]

    firstInitial = first[0].lower()
    lastLower = last.lower()

    lastThree = studentID[-3:]

    if len(lastLower) < 5:
      lastLower += "Y"

    userID = firstInitial + lastLower + lastThree

    majorCode = major[:3].upper()

    if year == "Freshman":
      yearCode = "FR"
    elif year == "Sophomore":
      yearCode = "SO"
    elif year == "Junior":
      yearCode = "JR"
    elif year == "Senior":
      yearCode = "SR"

    majorYear = majorCode + "-" + yearCode

    outFile.write(last + "," + first + "," + userID + "," + majorYear + "\n")

  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()