import requests
import json

class Comment:
    def get_data(self):
        data = requests.get("https://jsonplaceholder.typicode.com/comments")
        return data.json()

    def search_email(self, email):
        data = self.get_data()
        for user in data:
            if user["email"] == email:
                return user
        return "Email not found"

api_ob = Comment()

email = input("Enter your email: ")

result = api_ob.search_email(email)
print(json.dumps(result,indent=4))

# Eliseo@gardner.biz

