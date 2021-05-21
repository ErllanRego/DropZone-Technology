from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username= 'zona_de_drop', password='Mcl415263')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage = 100)
	
	session.follow_likers(['razer'], photos_grab_amount= 2, follow_likers_per_photo= 2, randomize = True, sleep_delay= 600, interact= True)

	comentarios = ['Nice picture']
	session.set_do_comment(enabled = True, percentage = 90)
	session.set_comments(comentarios, media = 'Photo')
	session.join_pods()