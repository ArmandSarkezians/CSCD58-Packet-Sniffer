"""
NetRange:       143.110.128.0 - 143.110.255.255
CIDR:           143.110.128.0/17
NetName:        DIGITALOCEAN-143-110-128-0
NetHandle:      NET-143-110-128-0-1
Parent:         NET143 (NET-143-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       AS14061
Organization:   DigitalOcean, LLC (DO-13)
RegDate:        2020-01-17
Updated:        2020-04-03
Comment:        Routing and Peering Policy can be found at https://www.as14061.net
Comment:
Comment:        Please submit abuse reports at https://www.digitalocean.com/company/contact/#abuse
Ref:            https://rdap.arin.net/registry/ip/143.110.128.0

OrgName:        DigitalOcean, LLC
OrgId:          DO-13
Address:        101 Ave of the Americas
Address:        FL2
City:           New York
StateProv:      NY
PostalCode:     10013
Country:        US
RegDate:        2012-05-14
Updated:        2022-05-19
Ref:            https://rdap.arin.net/registry/entity/DO-13


OrgAbuseHandle: ABUSE5232-ARIN
OrgAbuseName:   Abuse, DigitalOcean
OrgAbusePhone:  +1-347-875-6044
OrgAbuseEmail:  abuse@digitalocean.com
OrgAbuseRef:    https://rdap.arin.net/registry/entity/ABUSE5232-ARIN

OrgNOCHandle: NOC32014-ARIN
OrgNOCName:   Network Operations Center
OrgNOCPhone:  +1-347-875-6044
OrgNOCEmail:  noc@digitalocean.com
OrgNOCRef:    https://rdap.arin.net/registry/entity/NOC32014-ARIN

OrgTechHandle: NOC32014-ARIN
OrgTechName:   Network Operations Center
OrgTechPhone:  +1-347-875-6044
OrgTechEmail:  noc@digitalocean.com
OrgTechRef:    https://rdap.arin.net/registry/entity/NOC32014-ARIN
"""
import re

# Whois regex
net_range_regex = r"NetRange:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*-\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
cidr_regex = r"CIDR:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/(\d{1,3})"
net_name_regex = r"NetName:\s*(.*)"
net_handle_regex = r"NetHandle:\s*(.*)"
parent_regex = r"Parent:\s*(.*)"
net_type_regex = r"NetType:\s*(.*)"
origin_as_regex = r"OriginAS:\s*(.*)"
organization_regex = r"Organization:\s*(.*)"

# Org regex
org_name_regex = r"OrgName:\s*(.*)"
org_id_regex = r"OrgId:\s*(.*)"
org_address_regex = r"Address:\s*(.*)"
org_city_regex = r"City:\s*(.*)"
org_state_prov_regex = r"StateProv:\s*(.*)"
org_postal_code_regex = r"PostalCode:\s*(.*)"
org_country_regex = r"Country:\s*(.*)"

def search_regex(regex, data):
    result = re.search(regex, data)
    if result:
        return result.group(1)
    return None

class Org:
    def __init__(self, data):
        self.name = None
        self.id = None
        self.address = None
        self.city = None
        self.state_prov = None
        self.postal_code = None
        self.country = None
        # self.reg_date = None
        # self.updated = None

    def parse(self, data):
        self.name = search_regex(org_name_regex, data)
        self.id = search_regex(org_id_regex, data)
        self.address = re.findall(org_address_regex, data)
        self.city = search_regex(org_city_regex, data)
        self.state_prov = search_regex(org_state_prov_regex, data)
        self.postal_code = search_regex(org_postal_code_regex, data)
        self.country = search_regex(org_country_regex, data)

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "address": self.address,
            "city": self.city,
            "state_prov": self.state_prov,
            "postal_code": self.postal_code,
            "country": self.country
        }



class WhoIs:
    def __init__(self, data):
        self.net_range = None
        self.cidr = None
        self.net_name = None
        self.net_handle = None
        self.parent = None
        self.net_type = None
        self.origin_as = None
        self.organization = None
        self.org = Org(data)
        self.data = data
        self.parse()

    def parse(self):
      self.net_range = re.findall(net_range_regex, self.data)
      self.cidr = re.findall(cidr_regex, self.data)
      self.net_name = search_regex(net_name_regex, self.data)
      self.net_handle = search_regex(net_handle_regex, self.data)
      self.parent = search_regex(parent_regex, self.data)
      self.net_type = search_regex(net_type_regex, self.data)
      self.origin_as = search_regex(origin_as_regex, self.data)
      self.organization = search_regex(organization_regex, self.data)
      self.org.parse(self.data)

    def to_json(self):
        return {
            "net_range": self.net_range,
            "cidr": self.cidr,
            "net_name": self.net_name,
            "net_handle": self.net_handle,
            "parent": self.parent,
            "net_type": self.net_type,
            "origin_as": self.origin_as,
            "organization_name": self.organization,
            "org": self.org.to_json(),
            "raw": self.data
        }