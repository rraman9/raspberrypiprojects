import re
from atlassian import Jira
#WORDS = ["ISSUE", "BUG", "JIRA", "GO"]
WORDS = ["GO"]

def getSummary(issue):
    return issue['fields']['summary']

jira = Jira(
    url='https://tools.publicis.sapient.com/jira',
    username='rajraman',
    password='xx')

JQL = 'project in (WGT) and priority in ("P1 - Blocker") and status not in (Closed)'

def handle(text, mic, profile):
     # Responds to user-input, typically speech text, by replying Kaw-Kaw.
     # Arguments:
     # text -- user-input, typically transcribed speech
     # mic -- used to interact with the user (for both input and output)
     # profile -- contains information related to the user
     mic.say("Searching")
     
     data = jira.jql(JQL)
     issues = data['issues']
     if (len(issues)==0):
         mic.say("No issues")
     else:
         mic.say("There are " + `len(issues)` + " issues")
         # Print the issues
         for issue in data['issues']:
             mic.say(getSummary(issue))

def isValid(text):
     # Returns True if the input is related to freedom eagle.
     # Arguments
     # text -- user-input, typically transcribed speech
     return bool(re.search(r'\b(go)\b', text, re.IGNORECASE))

