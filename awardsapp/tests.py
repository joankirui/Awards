from django.test import TestCase
from .models import Profile,Post,Rating
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='joan',password='weuh')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

# class TestPost(TestCase):
#     def setUp(self):
#         self.user = User(id=1, username='joan',password='weuh')
#         self.post = Post(id=1, title='test post', photo='https://www.google.com/search?q=sky+images&tbm=isch&source=iu&ictx=1&fir=F8M43skF5JYDjM%252Cp8w6zOo7OEpOcM%252C_%253Bd4FAGYttGo2neM%252CuS4CORNFOUOQEM%252C_%253BnxYixhQwC0ajpM%252Crgp2mgfeoHN-PM%252C_%253BX0Z-k1DLFYtllM%252CL6FfB4hQGffgAM%252C_%253BxzLZd5AagBAPTM%252Cp8w6zOo7OEpOcM%252C_%253B5YqFrWgGGC4RDM%252CFb4X3tnmAmbY4M%252C_%253BqKfSvkU5Q_t92M%252Cp8w6zOo7OEpOcM%252C_%253BuiazbjcZRCJ7cM%252C2ewD5zRW0RM-TM%252C_%253BMHut9vDghxnrdM%252CKmNtIlIaGi0OdM%252C_%253BeXUC-3WyVcZa-M%252C438sZF7B1n5GpM%252C_%253Bx3gYqwqrvjNqSM%252CjKggd0AWgFttkM%252C_%253B05igrZvUDInlaM%252CiYyI_vpOpQdfOM%252C_%253B5xRqV4rlJ9IhdM%252CP08LsPe95_8lvM%252C_%253B7ezCKVfvguf7zM%252CjC7VBYh6Pozu3M%252C_&vet=1&usg=AI4_-kT2OBWyxnX2c-bbvZISZD20124FBw&sa=X&sqi=2&ved=2ahUKEwiItpG6y-D0AhV8qZUCHfTVDNsQ9QF6BAgYEAE#imgrc=nxYixhQwC0ajpM',description='desc',user=self.user, url='http://ur.coml')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.post, Post))

#     def test_save_post(self):
#         self.post.save_post()
#         post = Post.objects.all()
#         self.assertTrue(len(post) > 0)