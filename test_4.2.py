from app import app, sentiment_analysis

def test_all_users():
    # This will automatically analyze ALL users
    top_users = sentiment_analysis()

if __name__ == "__main__":
    # ✅ Run inside Flask's application context
    with app.app_context():
        test_all_users()

