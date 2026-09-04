dictdata=[
    {"id":101,"name":"neha","address":"mirganj"},
    {"id":102,"name":"saloni","address":"mirganj"},
    {"id":103,"name":"shajiya","address":"mirganj"}
]
username=input("please enter your name:").lower()

found = False

for data in dictdata:
    if data["name"]==username:

        print("Record found successfully")
        print("id:", data["id"])
        print("name:", data["name"])
        print("address:", data["address"])

        found=True
        break

if not found:
    print("Record does not exits")








