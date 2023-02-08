'''This file contains API for SNNs'''

'''
Endpoint Description:

1.	Leser et personnummer og gir svar om det er gyldig eller ikke
2.	Leser et personnummer og svarer om det er mann eller dame. 
3.	Leser et personnummer og svarer hva alderen er i år.
4.	Leser et personnummer og svarer om det finnes i datasettet. 
5.	Ikke tar noen input, men gir et svar på antall gyldige personnummer pr kjønn pr aldersgruppe.
6.	Siste endepunkt skal telle antall personnummer, menn og kvinner i datasettet. '''

from fastapi import FastAPI
from SNN_logic import SNN

# Read SNNs from file
snns = open("data/pnr.txt", "r")
snns = snns.read()
snns = snns.splitlines()[1:]

app = FastAPI()
Snn = SNN(snns=snns)

@app.get("/")
def read_root():
    
    return {"Message": "Welcome to Matias' SNN mini database.\nCheck your SNN or check if it is in the database.\nVisit /docs for swagger documentation.",
            "/valid?snn=": "Check if SNN is valid",
            "/gender?snn=": "Check gender of SNN",
            "/age?snn=": "Check age of SNN",
            "/is_among_given_snns?snn=": "Check if SNN is among given SNNs",
            "/count_by_gender": "Get count of SNNs in database by gender",
            "/count_by_gender_by_age": "Get count of SNNs in database by gender by age"}

@app.get("/valid")
def valid(snn: str):
    return Snn.valid(snn)

@app.get("/gender")
def gender(snn: str):
    return Snn.gender(snn) if Snn.valid(snn) else "SNN is not valid"

@app.get("/age")
def age(snn: str):
        return Snn.age(snn) if Snn.valid(snn) else "SNN is not valid"

@app.get("/is_among_given_snns")
def is_among_given_snns(snn: str):
    
    return Snn.is_among_given_snns(snn) if Snn.valid(snn) else "SNN is not valid"

@app.get("/count_by_gender")
def count_by_gender():
    return Snn.count_by_gender()

@app.get("/count_by_gender_by_age")
def count_by_gender_by_age():
    return Snn.count_by_gender_by_age()
