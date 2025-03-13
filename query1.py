from data.users import User
from data import db_session

db_session.global_init('database/mars_explorer.db')
session = db_session.create_session()

capitan = User()
capitan.surname = 'Scott'
capitan.name = 'Ridley'
capitan.age = 21
capitan.position = 'capitan'
capitan.speciality = 'engineer'
capitan.address = 'module_1'
capitan.email = 'scott_chief@mars.org'
capitan.hashed_password = '45467'
session.add(capitan)

boatsman = User()
boatsman.surname = 'Scott'
boatsman.name = 'Travis'
boatsman.age = 27
boatsman.position = 'boatsman'
boatsman.speciality = 'warrior'
boatsman.address = 'module_2'
boatsman.email = 'scott_travis@mars.org'
boatsman.hashed_password = '1233332'
session.add(boatsman)

shkiper = User()
shkiper.surname = 'Scottina'
shkiper.name = 'Mars'
shkiper.age = 66
shkiper.position = 'shkiper'
shkiper.speciality = 'shturman'
shkiper.address = 'module_3'
shkiper.email = 'holland_boat@mars.org'
shkiper.hashed_password = '2312321455'
session.add(shkiper)

clown = User()
clown.surname = 'Vladimir'
clown.name = 'Zelensky'
clown.age = 18
clown.position = 'clown'
clown.speciality = 'happy'
clown.address = 'module_4'
clown.email = 'sad_clown@mars.org'
clown.hashed_password = '23123214522325'
session.add(clown)



session.commit()
