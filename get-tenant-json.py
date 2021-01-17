#`python
import requests
import json

requests.packages.urllib3.disable_warnings()
encoded_body = json.dumps({
"aaaUser": {
"attributes": {
"name": "admin",
"pwd": "ciscopsdt"
}
}
})

resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)
header = {"Cookie": "APIC-cookie=" + resp.cookies["APIC-cookie"]}
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json?rsp-subtree-include=health,faults", headers=header, verify=False)
### print JSON as text###
#print(tenants.text)
### print JASON as JSON object###
json_response = json.loads(tenants.text)
#print(json.dumps(json_response, sort_keys=True, indent=4))
json_tenants = json_response['imdata']
for tenant in json_tenants:
 tenant_name = tenant['fvTenant']['attributes']['name']
 tenant_dn = tenant['fvTenant']['attributes']['dn']
 tenant_health = tenant['fvTenant']['children'][0]['healthInst']['attributes']['cur']
 output = "Tenant: " + tenant_name + "\t Health Score: " + tenant_health + "\n DN: " + tenant_dn
 print(output.expandtabs(40))
