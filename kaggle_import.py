import csv
import psycopg2

username = 'Chukh_B'
password = '1234'
database = 'youtube_stat'
host = 'localhost'
port = '5432'


INPUT_CSV_FILE = 'lab3/kaggleyoutube.csv'

query_0 = '''
CREATE TABLE new_video
(
    video_id character (200),
    title character varying(100),
    channel_title character varying(50),
    category_id integer,
    tags character varying(1000),
    CONSTRAINT pk_new_video PRIMARY KEY (video_id)
)
'''

query_1 = '''
DELETE FROM new_video
'''

query_2 = '''
INSERT INTO new_video (video_id, title, channel_title, category_id, tags) VALUES (%s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS new_video')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            values = (idx, row['title'], row['channel_title'], row['category_id'], row['tags'])
            cur.execute(query_2, values)

    conn.commit()