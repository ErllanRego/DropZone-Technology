from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username= 'zona_de_drop', password='Mcl415263')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage = 100)

	session.follow_user_followers(['hyperx','pichauoficial'], amount= 15, randomize= False)

	comentarios = ['Nice picture']
	session.set_do_comment(enabled = True, percentage = 90)
	session.set_comments(comentarios, media = 'Photo')
	session.join_pods()