from src.user.dao import UserDao
from security import hash_password
from security import verify_password
from logger import get_logger

logger=get_logger()

class Service:
    def create_user(user,db):
        try:
            user.password=hash_password(user.password)
            result=UserDao.create_user(user,db)
            return result
        except Exception as e:
            raise e
        
    def get_user_by_id(id,db,current_user):
        result= UserDao.get_user_by_id(id,db)
        logger.info(f"user fetched : {result.id} ,{result.email}")
        return result
        
        
    @staticmethod
    def get_all_users(page,page_size,db):
        try:
            page= (page - 1) * page_size
            result=UserDao.get_all_users(page,page_size,db)
            return result
        except Exception as e:
            raise e

    def get_user_for_security(id, db):
        return UserDao.get_user_by_id(id, db)
    
    def update_user(id,user,db):
        result=UserDao.update_user(id,user,db)
        return result
    
    @staticmethod
    def authenticate_user(email: str, password: str, db):
        # 1. Get user from DAO
        user = UserDao.get_user_by_email(db, email)
        if not user:
            return None
        
        # 2. Check password using the verify_password function you wrote
        if not verify_password(password, user.password):
            return None
            
        return user

    @staticmethod
    def get_user_by_email(email: str, db):
        return UserDao.get_user_by_email(db, email)
    
    @staticmethod
    def delete_user(id,db,current_user):
        return UserDao.delete_user(id,db)