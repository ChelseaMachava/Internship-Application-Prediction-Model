from tkinter import *
import csv
import statistics
import matplotlib.pyplot as plt

stuData = []
maxQues = 0
maxStu = 0
activeStu = 0
correctAnswer = []
selectedAnswer = []
result = []


def showMainWin():
    global stuData
    global maxQues
    global maxStu
    global correctAnswer
    global selectedAnswer
    global result
    global btnPrev
    global btnNext

    maxQues = len(open("questions.txt").readlines()) - 1
    correctAnswer = [""] * maxQues
    with open("questions.txt") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=':')
        lineNo = 0
        for row in csvReader:
            if lineNo > 0:
                correctAnswer[lineNo - 1] = row[1]
            lineNo += 1

    maxStu = len(open("answer.txt").readlines())
    stuData = [[""] * 7 for _ in range(maxStu)]
    selectedAnswer = [""] * maxStu
    result = [""] * maxStu
    with open("answer.txt") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=':')
        lineNo = 0
        for row in csvReader:
            stuData[lineNo][0] = row[0]  # Name
            stuData[lineNo][1] = row[1]  # Age
            stuData[lineNo][2] = row[2]  # Gender
            stuData[lineNo][3] = row[3]  # Country
            stuData[lineNo][4] = row[4]  # CGPA
            stuData[lineNo][5] = row[5]  # Experience
            stuData[lineNo][6] = row[6]  # Projects
            strAns = ""
            strResult = ""
            for ans in range(maxQues):
                strAns = strAns + row[ans + 7]
                if row[ans + 7] == correctAnswer[ans]:
                    strResult = strResult + "1"
                else:
                    strResult = strResult + "0"
            selectedAnswer[lineNo] = strAns
            result[lineNo] = strResult
            lineNo += 1

    btnPrev = Button(tkw, text="Prev", command=btnPrevClick)
    btnPrev.place(x=25, y=575, height=25, width=75)
    btnQuit = Button(tkw, text="Quit", command=btnQuitClick)
    btnQuit.place(x=150, y=575, height=25, width=100)
    btnNext = Button(tkw, text="Next", command=btnNextClick)
    btnNext.place(x=300, y=575, height=25, width=75)

    btnAnalysis = Button(tkw, text="Show Analysis", command=showAnalysisWindow)
    btnAnalysis.place(x=150, y=600, height=25, width=100)

    btnPrev["state"] = "disabled"
    btnNext["state"] = "normal"
    cvs.pack()
    displayResult()


def btnPrevClick():
    global activeStu
    activeStu -= 1
    displayResult()


def btnNextClick():
    global activeStu
    activeStu += 1
    displayResult()


def displayResult():
    global btnPrev
    global btnNext

    curStuDesc = "Student " + str(activeStu + 1) + " of " + str(maxStu)
    curStuName = "Name: " + stuData[activeStu][0]
    curStuAge = "Age: " + stuData[activeStu][1]
    curStuGender = "Gender: " + stuData[activeStu][2]
    curStuCountry = "Country: " + stuData[activeStu][3]
    curStuCGPA = "CGPA: " + stuData[activeStu][4]
    curStuExperience = "Experience: " + stuData[activeStu][5]
    curStuProjects = "Projects: " + stuData[activeStu][6]

    Label(tkw, text=curStuDesc, font=("Arial 12 bold")).place(x=50, y=50, height=25, width=300)
    Label(tkw, text=curStuName, font=("Arial 12 bold")).place(x=50, y=75, height=25, width=300)
    Label(tkw, text=curStuAge, font=("Arial 12 bold")).place(x=50, y=100, height=25, width=300)
    Label(tkw, text=curStuGender, font=("Arial 12 bold")).place(x=50, y=125, height=25, width=300)
    Label(tkw, text=curStuCountry, font=("Arial 12 bold")).place(x=50, y=150, height=25, width=300)
    Label(tkw, text=curStuCGPA, font=("Arial 12 bold")).place(x=50, y=175, height=25, width=300)
    Label(tkw, text=curStuExperience, font=("Arial 12 bold")).place(x=50, y=200, height=25, width=300)
    Label(tkw, text=curStuProjects, font=("Arial 12 bold")).place(x=50, y=225, height=25, width=300)

    strHeader = "NO  SELECTED  ANSWER  RESULT"
    Label(tkw, text=strHeader, font=("Arial 10 bold"), anchor=W).place(x=50, y=275, height=25, width=300)
    startY = 300
    countCorrect = 0
    for k in range(maxQues):
        strResult = str(k + 1) + ".          " + (selectedAnswer[activeStu])[k] + "              "
        strResult = strResult + correctAnswer[k] + "           "
        if (result[activeStu])[k] == "1":
            strResult = strResult + "CORRECT"
            countCorrect += 1
        else:
            strResult = strResult + "WRONG"
        Label(tkw, text=strResult, font=("Arial 10 bold"), anchor=W).place(x=50, y=(startY + 25 * k), height=25,
                                                                           width=300)
    strStat = str(countCorrect) + "/" + str(maxQues)
    Label(tkw, text=strStat, anchor=W).place(x=50, y=(startY + 25 * maxQues), height=25, width=300)

    if activeStu == 0:
        btnPrev["state"] = "disabled"
        btnNext["state"] = "normal"
    elif (activeStu + 1) == maxStu:
        btnPrev["state"] = "normal"
        btnNext["state"] = "disabled"
    else:
        btnPrev["state"] = "normal"
        btnNext["state"] = "normal"


def showAnalysisWindow():
    max_scores = []
    avg_scores = []
    mode_score = []

    for ans in result:
        correct_count = ans.count('1')
        max_scores.append(correct_count)
        avg_scores.append(correct_count / maxQues)

    max_score = max(max_scores)
    avg_score = sum(avg_scores) / len(avg_scores)
    mode_score = statistics.mode(max_scores)

    plt.figure(figsize=(10, 6))
    plt.hist(max_scores, bins=range(0, max_score + 2), align='left', rwidth=0.8)
    plt.xlabel('Maximum Scores')
    plt.ylabel('Frequency')
    plt.title('Distribution of Maximum Scores')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(avg_scores) + 1), avg_scores, marker='o')
    plt.xlabel('Students')
    plt.ylabel('Average Score')
    plt.title('Average Score per Student')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(['Maximum Score', 'Average Score', 'Mode Score'], [max_score, avg_score, mode_score])
    plt.xlabel('Statistics')
    plt.ylabel('Scores')
    plt.title('Summary Statistics')
    plt.grid(True)
    plt.show()


def btnQuitClick():
    tkw.destroy()


tkw = Tk()
tkw.title("Test Result")
tkw.geometry("400x650")
cvs = Canvas(tkw, width=400, height=750, bg='white')
showMainWin()
tkw.mainloop()
