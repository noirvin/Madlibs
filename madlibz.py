#PYTHON3 MADLIBS, story used from https://www.woojr.com/travel-mad-libs-for-kids/were-going-on-an-airplane/
#title
print("We are going on an airplane madlibs")
blankList = list()
#function to add elemets into the blankList array
def create(word):
    blankList.append(word)
#function to access default python input function
def user_input(prompt):
    user_input = input(prompt)
#variables to store words in the blanks
#adding the words into the blankList
verb1 = user_input("Enter a verb -ing")
create(verb1)
noun1 = user_input("Enter a noun")
create(noun1)
adjective1 = user_input("enter an adjective")
create(adjective1)
verb2 = user_input("enter a verb")
create(verb2)
verb3 = user_input("enter a verb")
create(verb3)
noun2 = user_input("enter a noun")
create(noun2)
noun3 = user_input("enter a noun")
create(noun3)
adjective2 = user_input("enter an adjective")
create(adjective2)
noun4 = user_input("enter a noun")
create(noun4)
verb4 = user_input("enter a verb")
create(verb4)
verb5 = user_input("enter a verb")
create(verb5)
adjective3 = user_input("enter a adjective")
create(adjective3)
noun5 = user_input("enter a noun; place")
create(noun5)
adjective4 = user_input("enter an adjective")
create(adjective4)
noun6 = user_input("enter a noun")
create(noun6)
verb6 = user_input("enter a verb")
create(verb6)
verb7 = user_input("enter a verb")
create(verb7)
noun7 = user_input("enter a noun")
create(noun7)
verb8 = user_input("enter a verb")
create(verb8)
noun8 = user_input("enter a noun")
create(noun8)


#display full story with the blanks filled in
print("""This will be my first time {} on a {} and I am so {} First, we will {} our suitcases with things we will {}
on vacation like {}, {}, and {} {} . Next, we will {} to the airport and {} our car in the {} lot. The
{} is very {} so we need to ride a {} from the parking lot to the airport.
Then we will {} our suitcases, which will {} in the {} of the plane during
the flight. I am excited to {} what things look like from up
high in the {}!""".format(blankList[0], blankList[1], blankList[2],
blankList[3], blankList[4], blankList[5], blankList[6], blankList[7],
blankList[8], blankList[9], blankList[10], blankList[11], blankList[12],
blankList[13], blankList[14], blankList[15], blankList[16], blankList[17], blankList[18], blankList[19]))
