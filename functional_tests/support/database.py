from plex_requests_api.model.database import Database
from ..config import config

# Reuses Database class from source code

def drop_all():
    db = Database(config['DB_PATH'])
    db._conn.executescript('DELETE FROM requests WHERE 1')
