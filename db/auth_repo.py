from db.user_model import User


def find_user_by_id(db, user_id):
    return db.query(User).filter(
        User.user_id == user_id
    ).first()