from app  import app, topics

def test_all_users():
    # This will automatically analyze ALL users
    top_users = topics()

if __name__ == "__main__":
    # ✅ Run inside Flask's application context
    with app.app_context():
        test_all_users()

