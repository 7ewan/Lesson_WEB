from datetime import datetime

from data.jobs import Jobs
from data import db_session

db_session.global_init('database/mars_explorer.db')
session = db_session.create_session()

shut = Jobs()
shut.team_leader = 1
shut.job = 'capitan'
shut.work_size = 15
shut.collaborators = '2, 3'
shut.start_date = datetime.now()
shut.is_finished = False
session.add(shut)

session.commit()