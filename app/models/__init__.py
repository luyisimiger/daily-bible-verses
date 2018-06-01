from app import login_manager
from app.models.bible import Bible
from app.models.biblebook import BibleBook
from app.models.biblebookchapter import BibleBookChapter
from app.models.bibleverse import BibleVerse
from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
