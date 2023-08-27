import json 
import random

def create_user(email, passw):
   with open("users.json",'a') as file:
       
       data = {
           "email":email,
           "password":passw
       }
       
       json.dump(data, file)
       file.write("\n")
       
def fetch_user():
    posts = []
    with open('users.json', 'r') as file:
        for line in file:
            post = json.loads(line)
            posts.append(post)
            
    return posts
