import json
file = open("servers.json")
rac_struc = json.load(file)

#exercise 1:
print("")
print("List of server names, ip addresses, services, protocols and ports:")
for i in rac_struc["rack"]:
    print(" Server name and ip address is " + i["server"]["server_name"] , i["server"]["ip-address"] + ".")
    print(" Services, protocols and ports are:")
    for j in i["server"]["services"]: 
        print("  " + j["service"] , j["protocol"] , j["port"] + ".")

#exercise 2:
print("")
firstserver_name = rac_struc["rack"][0]["server"]["server_name"]
print("Name of the first server is " + firstserver_name + ".")

#exercise 3:
print("")
print("List of services, protocols and ports of server S3:")
for i in rac_struc["rack"][2]["server"]["services"]:
        print(" " + i["service"] , i["protocol"] , i["port"] + ".")

file.close()