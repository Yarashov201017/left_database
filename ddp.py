import psycopg2
def cl_connect():
    ish=psycopg2.connect(
        host="localhost",
        database="at_ishniklar",
        user="postgres",
        password="password"
    )
    return ish
