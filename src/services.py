def createUser(self,name,email,phone_number,address,conn):
    conn.execute(text(CREATE_USER_TABLE))
    new_user = User(name,email,phone_number,address)
    conn.execute(text(INSERT_USER),[{"name":new_user.name,"email":new_user.email,"phone_number":new_user.phone_number,"address":new_user.address}])
    conn.commit()