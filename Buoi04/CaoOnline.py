endpoint="https://onlineapi.hcmue.edu.vn/api/authenticate/authpsc"
data={"username": "0808", "password": "pass_la_gi"}
api_key="hcmuepscRBF0zT2Mqo6vMw69YMOH43IrB2RtXBS0EHit2kzvL2auxaFJBvw=="
client_id="hcmue"

import requests

myheaders={
    "apikey": api_key,
    "clientid": client_id
}
rs = requests.post(endpoint, json=data, headers=myheaders)
print(rs.status_code)
if rs.status_code == 200:
    # print(rs.json())
    TOKEN=rs.json()["Token"]
    print("TOKEN", TOKEN)

    if TOKEN is not None:
        api_lay_tkb_hk="https://onlineapi.hcmue.edu.vn/api/professor/getTKBNamHocKyTuan"
        payload = {"YearStudy":"2026-2027","TermId":"HK01","Week":"41"}
        myheaders={
            "authorization": f"Bearer {TOKEN}",
            "apikey": api_key,
            "clientid": client_id
        }
        result = requests.post(api_lay_tkb_hk, json=payload, headers=myheaders)
        print(result.json())

else:
    print(rs.text)