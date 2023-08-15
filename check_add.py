import requests
import json
import re



#Assumptions
# 1. pincode will always be present at last in address string
# 2. Address will contain correct postoffice name in address matching with api database
    # eg some cities have two names or two spellings for a name like "nimkathana" and "neemkathana"
    # so if user write "neem ka thana" in address then it will give error because postoffice database have 'nim ka thana'

# function to find pincode from address string
def fetch_pincode(address):
    pattern = r"\b\d{6}\b"  # Regex pattern to match 6-digit pincode
    #finding all 6 digit numbers in add string
    match = re.findall(pattern, address)
    if match:
        return match[-1]
    else:
        return ""

#function to check pincode isvalid or not / match with address location
def check_pincode(pincode, address):
    if len(pincode) == 6:
        search_url = "https://api.postalpincode.in/pincode/{}".format(pincode)
        # here i am using get method to fetch information for a pincode
        response = requests.get(search_url)
        resp = json.loads(response.content)
        if resp[0]['Status'] == 'Success':
            for postoffice in resp[0]['PostOffice']:
                if postoffice.get('Name').lower() in address.lower():
                    return True
                else:
                    continue            
        else:
            return False
    else:
        return False

#function to check address
def check_address(address):
    if address:
        pincode = fetch_pincode(address)
        check =  check_pincode(pincode, address)
        if check == True:
            print("Address is correct")
        else: 
            print("Incorrect Address")
    else:
        print("please enter address")

#take address as input
address = input("Enter your address\n")
check_address(address)


#examples to test 
#correct ones 
# 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050
# 2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050
# 374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050
# hemawali dhani , nimkathana,332713

#incorrect ones
# empty string
# address with incorrect pincode
# 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095
# Colony, Bengaluru, Karnataka 560050
# hemawali dhani , neemkathana,332713

#**************------ Methods to Improve uncertanity and error in address------------------------------------------

# 1. We can use select fields instead of char fields for cities, post office according to pincode
# 2. We can also integrate our system with google maps 