from src.user.schema import User

class UserDao:
    def create_user(user,db):
        ex_user=db.query(User).filter(User.email==user.email)
        if ex_user.first():
            raise Exception("User with this ID already exists")
        result=User(**user.model_dump())
        db.add(result)
        db.commit()
        return result

    def get_user_by_id(id,db):
        result = db.query(User).filter(User.id==id,User.is_deleted==False).first()
        if not result:
            raise Exception("User not found")
        return result
        

    @staticmethod
    def get_all_users(skip,limit,db):
        try:
            # .offset() skips the first N items
            # .limit() restricts the number of items returned
            result = db.query(User).offset(skip).limit(limit).all()
            return result
        except Exception as e:
            raise e


    def update_user(id,user,db):
        ex_user=UserDao.get_user_by_id(id,db)
        if ex_user:
            ex_user.name=user.name
            ex_user.is_deleted=user.is_deleted
            ex_user.password=user.password
            db.commit()
            return ex_user
        

    @staticmethod
    def get_user_by_email(db, email: str):
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def delete_user(id,db):
        user=UserDao.get_user_by_id(id,db)
        if user:
            db.query(User).filter(User.id==id).update({"is_deleted":True})
            db.commit()
            return {"detail": "user deleted successfully"}