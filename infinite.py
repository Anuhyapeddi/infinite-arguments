# to pass infinite no. of arguments in funtions 

def print_people(*people):
    for person in people :
        print("This person is", person)
        
# to call the function 

print_people("Nick","jack","alice","jasmine","anu")
