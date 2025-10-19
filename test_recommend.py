# test_recommend.py
from app import recommend, query_db, app

def test_recommendations():
    with app.app_context():   # Needed to use query_db() safely
        # Try for a few user IDs that exist in your DB
        users = query_db('SELECT id,username ,* FROM users')

        for user in users:
            print(dict(user))
            uid = user['id']
            username = user['username']
            print(f"\n=== Recommendations for User {uid}: {username} ===")
            posts = recommend(uid)
            if not posts:
                print("No recommendations found.")
            else:
                for p in posts:
                    print(f"- {p['username']}: {p['content'][:60]!r}")

if __name__ == "__main__":
    test_recommendations()
