from app import app, user_reputation, query_db

def test_all_users():
    all_users = query_db('SELECT id,username FROM users')
    for user in all_users:
        uid = user['id']
        username = user['username']
        rep = user_reputation(uid)
        print(f"User ID {uid}:{username} → Reputation: {rep}")

if __name__ == "__main__":
    with app.app_context():
        test_all_users()