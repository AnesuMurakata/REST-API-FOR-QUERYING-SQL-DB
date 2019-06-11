import falcon
import uuid
import json

from models import User

class UserResource:

    def on_get(self, req, resp):
        if 'username' in req.params:
            user = self.session.query(User).filter(User.username == req.params['username']).one()
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(user)
        else:
            user = [{
                'username': user.username,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'email': user.email
             } for user in self.session.query(User).all()]
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(user)

    def on_post(self, req, resp):
        body = req.stream.read()
        payload = json.loads(body)
        firstname = payload['firstname']
        lastname = payload['lastname']
        username = payload['username']
        email = payload['email']
        password = payload['password']

        #create user to be added
        user = User(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email,
            password=password
        )

        self.session.add(user)
        self.session.commit()

        resp.status = falcon.HTTP_201
        resp.body = json.dumps({
            'firstname': user.firstname,
            'lastname': user.lastname,
            'username': user.username,
            'email': user.email
        })