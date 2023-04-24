from chat import app, db, User, bcrypt

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        users = [
            User(first_name="pfano",
                 last_name="sigama",
                 email="pfano@email.com",
                 password=bcrypt.generate_password_hash("12345")),
            User(first_name="john",
                 last_name="doe",
                 email="john@email.com",
                 password=bcrypt.generate_password_hash("12345"),
                 ),
            User(first_name="may",
                 last_name="april",
                 email="may@email.com",
                 password=bcrypt.generate_password_hash("12345"),
                 ),
            User(first_name="tech",
                 last_name="smith",
                 email="tech@email.com",
                 password=bcrypt.generate_password_hash("12345"),
                 ),
            User(first_name="roy",
                 last_name="mat",
                 email="roy@email.com",
                 password=bcrypt.generate_password_hash("12345"),
                 )
        ]
        db.session.add_all(users)
        db.session.commit()
