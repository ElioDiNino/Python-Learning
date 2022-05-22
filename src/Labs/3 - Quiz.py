score = 0
questions = 6
import time
print("Welcome to my quiz.\n")
time.sleep(3)
## Question 1
print("Question 1: What continent is Canada located in?")
answer1 = input("Your answer:")
if answer1.lower() == "north america":
    time.sleep(1)
    print("Correct!")
    score += 1
else:
    print("Incorrect, you should know that it's North America.")
time.sleep(1)
print("Your Score:", score, "/1\n")
time.sleep(2)
## Question 2
print("Question 2: What equation is the Pythagoream Theorem?")
print("A. ax² + bx + c\nB. a² + b² + c²\nC. a² + b² = c²")
answer2 = input("Your answer:")
if answer2.lower() == "c" or answer2.lower() == "c." or answer2.lower() == "a² + b² = c²":
    time.sleep(1)
    print("Good job, you remembered grade 8 math!")
    score += 1
else:
    print("Good try, you should probably go back to basic math.")
time.sleep(1)
print("Your Score:", score, "/2\n")
time.sleep(2)
## Question 3
print("Question 3: What is the force of gravity for a 2kg object (in newtons)")
answer3 = input("Your answer:")
if answer3.lower() == "19.6n":
    time.sleep(1)
    print("Correct, you must be taking physics.")
    score += 1
else:
    print("Incorrect, you have to use Fg = mg to solve it.")
time.sleep(1)
print("Your Score:", score, "/3\n")
time.sleep(2)
## Question 4
print("Question 4: What is 13/9 (2 decimal places)?")
answer4 = input("Your answer:")
if answer4 == "1.44":
    time.sleep(1)
    print("You got it, hopefully you didn't use a calculator!")
    score += 1
else:
    print("Don't worry not everyone can do this in their head.")
time.sleep(1)
print("Your Score:", score, "/4\n")
time.sleep(2)
## Question 5
print("Question 5: What country is located in the Middle East and starts with a B?")
answer5 = input("Your answer:")
if answer5.lower() == "bahrain":
    time.sleep(1)
    print("Great job, you know your map!")
    score += 1
else:
    print("Don't worry, most people don't get this one.")
time.sleep(1)
print("Your Score:", score, "/5\n")
time.sleep(2)
## Question 6
print("Question 6: What should and shouldn't python be used for?")
print("A. Graphics; Data\nB. Data; Graphics\nC. Websites; Hacking")
answer6 = input("Your answer:")
if answer6.lower() == "b" or answer6.lower() == "b." or answer6.lower() == "data; graphics":
    time.sleep(1)
    print("Congratulations, you understand python!")
    score += 1
else:
    print("It's okay, we all mess up sometimes.")
time.sleep(1)
print("Your Score:", score, "/6\n")
time.sleep(2)
## Final Grade
print("Your quiz grade:", "{:.2%}".format(score/questions))
time.sleep(1)
grade = score/questions*100
if grade < 50:
    print("You failed, you definently need to try again.")
elif grade >= 50 and grade < 60:
    print("You passed, but just barely with a C-.")
elif grade >= 60 and grade < 67:
    print("You got a C, so you could do with some more practice.")
elif grade >= 67 and grade < 73:
    print("Not bad, a C+ makes you a decent student.")
elif grade >= 73 and grade < 86:
    print("You got a B, that's good!")
elif grade >=86 and grade <100:
    print("You got an A, that's amazing!")
elif grade == 100:
    print("You got 100%, you are a god!")
