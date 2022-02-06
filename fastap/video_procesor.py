import datetime
import schedule
import time
from fastap.models.route import routes
from fastap.config.db import conn

from counting_car_1 import video_analysis


def update_table_routes():
    routes_list =['mazimbu', 'mafiga', 'kilakala']
    for route_name in routes_list:
        video_in_que = route_name+'.mp4'
        route_status = video_analysis(video_in_que)
        if route_status:
            status = 'Jam'
        elif not route_status:
            status = 'No Jam'

        conn.execute(routes.insert().values(route=route_name, status=status))


schedule.every(20).seconds.do(update_table_routes)
while 1:
    schedule.run_pending()
    time.sleep(20)

