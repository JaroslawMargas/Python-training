class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.got_marks = self.name + ' obtained ' + self.marks + ' marks'

    @property
    def got_marks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    @got_marks.setter
    def got_marks(self, sentence):
        name, marks = sentence.split(' ')
        self.name = name
        self.marks = marks


st = Student("Jaki", "25")
print(st.name)
# Jaki
print(st.marks)
# 25
print(st.got_marks)
# Jaki obtained 25 marks

# @ propert

# setter
st.got_marks = 'Golam 36'
# get
print(st.got_marks)
# Golam obtained 36 marks
print(st.name)
# Golam
print(st.marks)
# 36
