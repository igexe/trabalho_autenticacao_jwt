from cadastro import cadastro
from fastapi import FastAPI 
import jwt

app=FastAPI()

@app.get('/')
def log(user,senha):
    secret='s3cr3t'
    algorithm='HS256'
    t=open('users.txt','r+')
    d=t.readlines()
    u=''
    for x in d:
        x=x.rstrip('\n')
        x=jwt.decode(x,secret,algorithm)
        if x['user']==user and x['senha']==senha:
            u=x['user']
            break
        else:
            u='usuario ou senha invalidos'

    if u==0: return u
    else: return 'bem vindo '+u

@app.get('/cadastro')
def cad(id,user,senha):
    return cadastro(id,user,senha)