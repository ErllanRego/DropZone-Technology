from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username= 'zona_de_drop', password='Mcl415263')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage = 100)
	#nonFollowers para deixar de seguir quem não te segue 
	#allfollowing para deixar de todo mundo
	#unfollow_after deixa de seguir pessoas que não seguiram voce de volta em determinado tempo 
	session.unfollow_users(amount=10, nonFollowers=True, style="RANDOM", sleep_delay=450)

	comentarios = ['Nice picture', 'Good', 'love your post',]
	session.set_do_comment(enabled = True, percentage = 90)
	session.set_comments(comentarios, media = 'Photo')
	session.join_pods()