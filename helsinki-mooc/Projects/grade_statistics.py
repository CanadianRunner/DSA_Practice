# Write your solution here

def userInputFunc():
  numberOfInputs = 0
  points = []
  grades = []
  grade5 = grade4 = grade3 = grade2 = grade1 = grade0 = 0
  passCount = 0

  while True:
    userInput = input("Exam points and exercises completed: ")
    if userInput == "":
      break

    examPointsStr, exercisesCompletedStr = userInput.split()
    examPointsInt = int(examPointsStr)
    exercisesCompletedInt = int(exercisesCompletedStr)

    exercisePoints = exercisesCompletedInt // 10
    totalPoints = examPointsInt + exercisePoints 

    points.append(totalPoints)
    grades.append(exercisePoints)
    numberOfInputs += 1

    if examPointsInt < 10:
      grade = 0
    elif totalPoints <= 14:
      grade = 0
    elif totalPoints <= 17:
      grade = 1
    elif totalPoints <= 20:
      grade = 2
    elif totalPoints <= 23:
      grade = 3
    elif totalPoints <= 27:
      grade = 4
    else:
      grade = 5

    if grade == 0:
      grade0 += 1
    elif grade == 1:
      grade1 += 1
    elif grade == 2:
      grade2 += 1
    elif grade == 3:
      grade3 += 1
    elif grade == 4:
      grade4 += 1
    else:
      grade5 += 1

    if grade > 0:
      passCount += 1

  return numberOfInputs, points, grades, passCount, grade0, grade1, grade2, grade3, grade4, grade5


def calculateExamPoints(numberOfInputs, points, passCount):
  if numberOfInputs == 0:
    return 0.0, 0.0
  totalPointsSum = sum(points)
  pointsAverage = totalPointsSum / numberOfInputs
  passPercentage = 100.0 * passCount / numberOfInputs
  return passPercentage, pointsAverage


def printResults(passPercentage, pointsAverage, grade0, grade1, grade2, grade3, grade4, grade5):
  print("Statistics:")
  print(f"Points average: {pointsAverage:.1f}")
  print(f"Pass percentage: {passPercentage:.1f}")
  print("Grade distribution:")
  print(f"  5: {'*' * grade5}")
  print(f"  4: {'*' * grade4}")
  print(f"  3: {'*' * grade3}")
  print(f"  2: {'*' * grade2}")
  print(f"  1: {'*' * grade1}")
  print(f"  0: {'*' * grade0}")


def main():
  numberOfInputs, points, grades, passCount, g0, g1, g2, g3, g4, g5 = userInputFunc()
  passPercentage, pointsAverage = calculateExamPoints(numberOfInputs, points, passCount)
  printResults(passPercentage, pointsAverage, g0, g1, g2, g3, g4, g5)

main()
