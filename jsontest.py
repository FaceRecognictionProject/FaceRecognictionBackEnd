import json

Perple = {
        "Perplejson": [
            #1
            {  
                "IDname": "adisak",
                "name": "Adisak",
                "lastname": " Phiwphong",
                "age": "22",              
            },
            #2
            {
                "IDname": "aphiwat",
                "name": "Aphiwat",
                "lastname": "Deeying",
                "age": "22",
            },
            #3
            {
                "IDname": "assada",
                "name":"Assada",
                "lastname": "Rattanakorn",
                "age": "22",
            },
            #4
            {  
                "IDname": "chawin",
                "name":"Chawin",
                "lastname": "Hitakhun",
                "age": "22",
            },
            #5
            {  
                "IDname": "chutmongkhol",
                "name": "Chutmongkhol",
                "lastname": "Romket",
                "age": "22",
            },
            #6
            {  
                "IDname": "jenjira",
                "name": "Jenjira",
                "lastname": "Singthum",
                "age": "22",
            },
            #7
            {  
                "IDname": "nakarin",
                "name": "Nakarin",
                "lastname": "Chasaen",
                "age": "22",
            },
            #8
            {  
                "IDname": "pattaraporn",
                "name": "Pattaraporn",
                "lastname": "Rueangsaen",
                "age": "22",
            },
            #9
            {  
                "IDname": "pakknon",
                "name": "Pakknon",
                "lastname": "Wongkrajang",
                "age": "22",
            },
            #10
            {  
                "IDname": "ooraya",
                "name": "Ooraya",
                "lastname": "Aiyawan",
                "age": "22",
            },
            #11
            {  
                "IDname": "padcahrida",
                "name": "Padcahrida",
                "lastname": "Pantasa",
                "age": "22",
            },
            #12
            {  
                "IDname": "panida",
                "name": "Panida",
                "lastname": "hinso",
                "age": "22",
            },
            #13
            {  
                "IDname": "panupong",
                "name": "Panupong",
                "lastname": "wonglamphan",
                "age": "22",
            },
            #14
            {  
                "IDname": "pichit",
                "name": "Pichit",
                "lastname": "pankaew",
                "age": "22",
            },
            #15
            {  
                "IDname": "phadcharapon",
                "name": "Phadcharapon",
                "lastname": "Kaewmungkhun",
                "age": "22",
            },
            #16
            {  
                "IDname": "phiraphat",
                "name": "Phiraphat",
                "lastname": "Saentai",
                "age": "22",
            },
            #17
            {  
                "IDname": "phontawat",
                "name": "Phontawat",
                "lastname": "Wannawiset",
                "age": "22",
            },
            #18
            {  
                "IDname": "pimnipa",
                "name": "Pimnipa",
                "lastname": "Srihajak",
                "age": "22",
            },
            #19
            {  
                "IDname": "saksit",
                "name": "Saksit",
                "lastname": "Piyanan",
                "age": "22",
            },
            #20
            {  
                "IDname": "shongwut",
                "name": "Shongwut",
                "lastname": "Suwannahom",
                "age": "22",
            },
            #21
            {  
                "IDname": "sompong",
                "name": "Sompong",
                "lastname": "Kongphan",
                "age": "22",
            },
           
        ]
}
with open("Jsondata.json","w") as write_file:
    json.dump(Perple, write_file, indent=4, separators=(", ", ": "), sort_keys=True)
print (Perple)
