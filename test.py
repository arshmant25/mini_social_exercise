from app import app, user_risk_analysis

def test_all_users():
    # This will automatically analyze ALL users
    top_users = user_risk_analysis(None)

if __name__ == "__main__":
    # ✅ Run inside Flask's application context
    with app.app_context():
        test_all_users()

'''
from app import app, user_risk_analysis, query_db

def test_all_users():
    users = query_db('SELECT id, username FROM users WHERE id = ?', (105,))
    for user in users:
        user_id = user['id']
        username = user['username']
        total_risk = user_risk_analysis(user_id)
        print(f"User: {username} (ID: {user_id}) → Total Risk: {total_risk}")

if __name__ == "__main__":
    # ✅ Run inside Flask's application context
    with app.app_context():
        test_all_users()


'''