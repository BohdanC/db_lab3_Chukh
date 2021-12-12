import psycopg2
import matplotlib.pyplot as plt

username = 'Chukh_B'
password = '1234'
database = 'youtube_stat'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW VideoCategory as
select cat_name,count(title) from video 
inner join category on video.category_id=category.category_id 
group by cat_name
'''
query_2 = '''
CREATE VIEW VideoCountry as
select country_name,count(title) from video 
inner join country on video.country_id=country.country_id 
group by country_name
'''

query_3 = '''
CREATE VIEW VideoChannel as
select channel_title,count(title) from video 
inner join channel on video.channel_id=channel.channel_id 
group by channel_title

'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS VideoCategory')

    cur.execute(query_1)
    cur.execute('select * from VideoCategory')
    categor = []
    cat_count = []

    for row in cur:
        categor.append(row[0])
        cat_count.append(row[1])

    cur.execute('DROP VIEW IF EXISTS VideoCountry')

    cur.execute(query_2)
    cur.execute('select * from VideoCountry')
    country = []
    cn_count = []

    for row in cur:
        country.append(row[0])
        cn_count.append(row[1])

    cur.execute('DROP VIEW IF EXISTS VideoChannel')

    cur.execute(query_3)
    cur.execute('select * from VideoChannel')
    chanel = []
    ch_count = []

    for row in cur:
        chanel.append(row[0])
        ch_count.append(row[1])

    fig, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    # bar
    bar_ax.set_title('Кількість відео в певній категорії')
    bar_ax.set_xlabel('Категорія')
    bar_ax.set_ylabel('Кількість відео')
    bar = bar_ax.bar(categor, cat_count)
    bar_ax.set_xticks(range(len(categor)))
    bar_ax.set_xticklabels(categor, rotation=30)

    # pie
    pie_ax.pie(cn_count, labels=country, autopct='%1.1f%%')
    pie_ax.set_title('Кількість відео по кожній країні')

    # graph
    graph_ax.plot(chanel, ch_count, marker='o')
    graph_ax.set_xlabel('Назва каналу')
    graph_ax.set_ylabel('Кількість відео')
    graph_ax.set_title('Графік залежності кількості відео від назви каналу')
    for chn, count in zip(chanel, ch_count):
        graph_ax.annotate(count, xy=(chn, count), xytext=(7, 2), textcoords='offset points')

plt.get_current_fig_manager().resize(1600, 700)
plt.show()