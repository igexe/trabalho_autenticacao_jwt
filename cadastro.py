import jwt
secret='s3cr3t'
algorithm='HS256'

def cadastro(id:int,user:str,senha:str,):

    payload={
        'id':id,
        'user':user,
        'senha':senha,
        'adm':False
                }
    token=jwt.encode(payload,secret,algorithm)

    t=open('users.txt','r+')
    d=t.readlines()

    t.writelines(str(token)+'\n')
    t.close()

    return 'cadastro salvo é possivel ver o cadastro no txt "users"'