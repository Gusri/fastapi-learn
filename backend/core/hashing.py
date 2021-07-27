from passlib.context import CryptContext
# from passlib.utils import generate_password
# from core.hashing.Has
# from passlib.utils.decor import deprecated_function

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password(plain_password):
        return pwd_context.hash(plain_password)

