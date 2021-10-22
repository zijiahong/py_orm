import db,model
new_user = model.Test(id='5', name='Bob')
db.create(new_user)