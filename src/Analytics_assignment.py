import json

class SAA:
    """ A class wrapping a set of functions analyzing a given set of json data.
    """
    data = []
    grades = []
    
    def __init__(self):
        """ Create an instance of the SAA class which automatically grabs the grade-data.json from the data folder and stores it for later use. 
        
        Currently no functionality to aquire alternate data set outside of replacing the json file in data
        """
        with open('..\\data\\grade-data.json') as f:
            self.data = json.loads(f.read())
        self.grades = {"A":4,"B":3,"C":2,"D":1,"F":0}
            
    def avg_fGrade(self):
        """ Returns the average final grade of the class in letter form.
        """
        sum = 0
        for i in self.data:
            sum += self.grades[i[3]]
            
        avg = round(sum/len(self.data))
        return list(self.grades.keys())[list(self.grades.values()).index(avg)]
        
    def avg_Change(self):
        """ Returns the average value change from midterm grades to final grades. 
        
        A change of 1 indicates an average change of one letter grade upwards. a change of -1 indicates an average change of one letter grade downwards.
        """
        sumC = 0
        for i in self.data:
            if i[2] != i[3]:
                sumC += (self.grades[i[2]] - self.grades[i[3]])
        return (sumC/len(self.data))
        
    def count_Grade(self):
        """ Returns a dictionary of Grades and the number of students with that final grade.
        """
        A,B,C,D,F = 0,0,0,0,0
        for i in self.data:
            if i[3] == "A":
                A += 1
            elif i[3] == "B":
                B += 1
            elif i[3] == "C":
                C += 1
            elif i[3] == "D":
                D += 1
            else:
                F += 1
                
        return dict([("A",A),("B",B),("C",C),("D",D),("F",F)])
        
    def count_Sex(self):
        """ Returns a dictionary with the number of male and female students.
        """
        M,F = 0,0
        for i in self.data:
            if i[1] == "M":
                M += 1
            else:
                F += 1
                
        return dict([("M",M),("F",F)])
        
