import json
from sampd import datas
data = json.loads(datas)
print("Interface Status")
print("================================================================================")
print("DN""                                                     ""Description""         ""Speed""     ""MTU")
print("--------------------------------------------------""  ""-----------------""      ""------""   ""------")
for d in data["imdata"]:
        dn = d["l1PhysIf"]["attributes"]["dn"]
        descrip = d["l1PhysIf"]["attributes"]["fecMode"]
        speed = d["l1PhysIf"]["attributes"]["speed"]
        mtu = d["l1PhysIf"]["attributes"]["mtu"]
        print(f'{dn:42}{" " :15}{descrip}{" ":14}{speed}{" ":2}{mtu}')