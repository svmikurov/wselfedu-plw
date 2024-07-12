import psycopg2


def connect(db_url):
    """Create a new database connection."""
    return psycopg2.connect(db_url)


def close(conn):
    """Close a new database connection."""
    return conn.close()


def truncate_user_table(conn):
    """Truncate the users database table."""
    with conn.cursor() as curs:
        curs.execute('TRUNCATE TABLE users_usermodel CASCADE')
        conn.commit()
