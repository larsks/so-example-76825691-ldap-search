import ldap3


ldap_conn = ldap3.Connection(
    "ldap://localhost:1389", "cn=admin,dc=example,dc=com", "secret"
)
basedn = "dc=example,dc=com"
attribs = ["mail"]
data = []

for account in ["alice", "bob"]:
    sfilter = f"(cn={account})"
    ldap_conn.open()
    ldap_conn.search(basedn, sfilter, attributes=attribs)
    if ldap_conn.entries:
        test = ldap_conn.entries[0].mail
        data.append(test.value)

print(data)
