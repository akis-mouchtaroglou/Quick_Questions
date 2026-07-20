import time
import threading
import random
print("When the program says go, you will answer the questions that appear on the terminal ")
print("DISCLAIMER: Divisions are rounded up, so you di=n;t have to deal with the decimals😉")
time.sleep(5)
print("GO!")

v_stop = True
score = 0
def stop():
    global v_stop
    print(f"TIME'S UP!!! You answered {score} questions right!")
    exit()


threading.Timer(30, stop).start()

while v_stop == True:
    no1 = random.randint(1 , 100)
    no2 = random.randint(1 , 100)
    candidate = ["/" , "*" , "+" , "-"]
    moderator = random.choice(candidate)
    if moderator == "/":
        correct_ans = round(no1 / no2)
    elif moderator == "*":
        correct_ans = no1 * no2
    elif moderator == "+":
        correct_ans = no1 + no2
    else:
        correct_ans = no1 - no2
    question = str(no1) + moderator + str(no2)
    answer = float(input(question))
    if correct_ans == answer:
        print("Congrats, moving on...")
        score = score + 1
    else:
        print("Oh no... Try to answer correctly next time...")
     