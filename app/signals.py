from app import app, lm

@app.before_request
def register_current_user():
    app.g.user = lm.current_user
