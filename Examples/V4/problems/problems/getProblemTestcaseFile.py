"""
Example presents usage of the successful problems.getTestcaseFile() API method
"""
from sphere_engine import ProblemsClientV4

# define access parameters
accessToken = '<access_token>'
endpoint = '<endpoint>'

# initialization
client = ProblemsClientV4(accessToken, endpoint)

# API usage
problemCode = 'TEST'
testcaseNumber = 0
file = 'input'

response = client.problems.getTestcaseFile(problemCode, testcaseNumber, file)