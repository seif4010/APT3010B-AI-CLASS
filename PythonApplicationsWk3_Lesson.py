# class school with inheritance concept
class Person:
    def __init__(self, name, Pid, department):
        self.name = name
        self.Pid = Pid
        self.department = department


# class object student to display the studnet data
class student:
    # insert data
    def __init__(self, name, Pid, department, score, standing):
        # properties from Persons in inherited through invoking it
        Person.__init__(self, name, Pid, department)
        self.standing = standing
        self.score = score
     # display the data

    def display(self):
        print("Studnet details are: " + self.name + " " + str(self.score) +
              " " + self.standing + " " + str(self.Pid) + " " + self.department)


# making the objects
student1 = student("Yussuf", 660411, "APT", 100, "Senior")
student2 = student("Watashi", 661401, "APT", 100, "Freshman")
student3 = student("Kim", 511400, "APT", 90, "Junior")

# displaying the contents of student
student1.display()
student2.display()
student3.display()

# class more examples using the tower Ranoi
# source rod
A = []
# middle rod
B = []
# target rod
C = []


def showAll():
    print(A, B, C, '_________________', sep='\n')


def move(n, source, target, bridge):
    if n > 0:
        # move n - 1 disks from source to bridge, so they are out of the way
        move(n - 1, source, bridge, target)

        # move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        showAll()

        # move the n - 1 disks that we left on bridge onto target
        move(n - 1, bridge, target, source)


discs = int(input("Number of disks: "))
print(discs, '_________________', sep='\n')
A = list(range(1, discs+1))[::-1]
showAll()
# initiate call from source A to target C with auxiliary B
move(discs, A, C, B)
print("Number of moves:" + str(2**discs - 1))
