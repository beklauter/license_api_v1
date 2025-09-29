import api
import start
import user


if __name__ == '__main__':
    start.load_env()

    new_user = user.add_user("testuser", "testpass")
    new_license = new_user.create_license()
    user.save_users()
    print(f"User: {new_user.username}, Lizenz: {new_license}")

    api.api_run()