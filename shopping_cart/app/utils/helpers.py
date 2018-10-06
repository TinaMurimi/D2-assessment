from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
bcrypt = Bcrypt()


def encrpt_password(password):
    return bcrypt.generate_password_hash(
        password.encode('utf8'), 12).decode('utf8')


@auth.verify_password
def verify_password(self, password):
    if bcrypt.check_password_hash(self.password, password):
        return True

    return False


def sql(session, sql, args={}):
    "Execute raw sql, optionally with prepared query"
    result = session.execute(sql, args)
    session.commit()
    return result
