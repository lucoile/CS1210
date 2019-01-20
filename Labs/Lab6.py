#!/usr/local/anaconda/bin/python
######################################################################
# YOUR NAME GOES HERE
# YOUR DISCUSSION SECTION (e.g., "A09") GOES HERE
######################################################################

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# Replace "hawkid" in the singleton tuple in the function below with
# your own hawkid USING LOWER CASE CHARACTERS ONLY.
#
# ATTENTION: Your hawkid is your login name for ICON, it is not
# your student ID number. 
#
# Failure to correctly do so will result in a 0 grade.
######################################################################
def hawkid():
    return(("buffard",))

######################################################################
# Write a good comment here.
class Student():
    def __init__(self, name):
        self.name = name		# e.g., "CS1210"
        self.transcript = {}		# My enrollments

    # Simplify what gets printed.
    def __repr__(self):
        return('<Student: {}>'.format(self.name))

    ##################################################################
    # Manipulate the student's transcript to reflect enrollment.
    def enroll(self, c):
        self.transcript.update({c: 'I'})
        
    ##################################################################
    # Manipulate the student's transcript to reflect withdrawl.
    def drop(self, c):
        self.transcript[c] = 'W'

######################################################################
# Write a good comment here.
class Class():
    def __init__(self, name, cap = 30):
        self.name = name	        # e.g., "Joe"
        self.cap = cap			# Course enrolment cap
        self.roster = {}		# Students in course
        self.waitlist = []		# Students on waitlist

    # Simplify what gets printed.
    def __repr__(self):
        return('<Class: {}>'.format(self.name))

    ##################################################################
    # Method to enroll given student in this class. Make sure you
    # don't exceed the course enrollment cap; you'll need to check the
    # roster for students still marked active. Any student attempting
    # to enroll beyond the cap should be added to the course waitlist
    # instead. Important: once enrolled, make sure you invoke the
    # Student.enroll() method to update the student object as well.
    def enroll(self, student):
        # Check if there is room in the class by creating a list of
        # all the currently enrolled students and checking if it's
        # lower than the cap.
        if len([ s for s in self.roster if self.roster[s] == True ]) < self.cap:
            # Add student to roster.
            self.roster.update({student:True})
            # Add class to students transcript.
            student.enroll(self)
        else:
            # If there is no space, add student to waitlist.
            self.waitlist.append(student)

    ##################################################################
    # Method to drop given student in this class. If there are
    # students still on the waitlist, they should be automatically
    # enrolled. Students who drop should remain on the roster but
    # should be marked inactive. Important: once withdrawn, make sure
    # you invoke the Student.drop() method to update the student
    # object as well.
    def drop(self, student):
        self.roster[student] = False
        student.drop(self)
        # Check if there is room in the class after dropping by creating
        # a list of all the currently enrolled students and checking if it's
        # lower than the cap.
        if len([ s for s in self.roster if self.roster[s] == True ]) < self.cap:
            # Get the next person on the waitlist and enroll them in the class.
            waitlister = self.waitlist[0]
            waitlister.enroll(self)
            self.roster.update({waitlister:True})
            # Remove the waitlister from the list after enrolling them.
            self.waitlist.remove(waitlister)






