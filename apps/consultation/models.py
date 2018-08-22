from django.db import models
from apps.home.models import User

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add = True)
    edit_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.id)

class CategoriesManager(models.Manager):
    def first_process(self, postdata):
        default = 0
        result = 0
        first_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=1))
        if int(postdata['choice']) > 0:
            for i in postdata['choice']:
                low_tyroids = i
                low_cortisal = i
                low_androgen = i
                print (str(low_tyroids), str(low_cortisal), str(low_androgen))
        return result

    def second_process(self, postdata):
        # checked
        default = 0
        second_question = Categories.objects.create(high_insulin=default, low_tyroids=default, high_cortisol=default, low_cortisal=default, high_androgen=postdata['choice'], low_androgen=default, estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=2))
        return second_question

    def third_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        third_question = Categories.objects.create(high_insulin=default, low_tyroids=default, high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=3))
        return third_question

    def fourth_process(self, postdata):
        # checked
        default = 0
        fourth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=default, estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=4))
        return fourth_question

    def fifth_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fifith_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=default, estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=5))
        return fifith_question

    def sixth_process(self, postdata):
        # checked
        default = 0
        sixth_quesiton = Categories.objects.create(high_insulin=default, low_tyroids=default, high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=6))
        return sixth_quesiton

    def seventh_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        seventh_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=default, estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=7))
        return seventh_question

    def eighth_process(self, postdata):
        # checked
        default = 0
        eight_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=default, estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=8))
        return eight_question

    def ninth_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        ninth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=9))
        return ninth_question

    def ten_process(self, postdata):
        # checked
        default = 0
        ten_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=10))
        return ten_question

    def eleventh_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        eleventh_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=11))
        return eleventh_question

    def twelveth_process(self, postdata):
        # checked
        default = 0
        twelveth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=default, estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=12))
        return twelveth_question

    def thirtheenth_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        thirtheenth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=13))
        return thirtheenth_question

    def fourtheenth_process(self, postdata):
        # checked
        default = 0
        fourtheenth_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=14))
        return fourtheenth_question

    def fiftheenth_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fiftheenth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=15))
        return fiftheenth_question

    def sixtheenth_process(self, postdata):
        # checked
        default = 0
        sixtheenth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=16))
        return sixtheenth_question

    def seventheenth_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        seventheenth = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=17))
        return seventheenth

    def eightheenth_process(self, postdata):
        # checked
        default = 0
        eightheenth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=18))
        return eightheenth_question

    def nintheenth_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        nintheenth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=19))
        return nintheenth_question

    def twentheeth_process(self, postdata):
        # checked
        default = 0
        twen_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=20))
        return twen_question

    def twen_one_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        twen_one_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=21))
        return twen_one_question

    def twen_two_process(self, postdata):
        # checked
        default = 0
        twen_two_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=22))
        return twen_two_question

    def twen_three_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        twen_three_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=23))
        return twen_three_question

    def twen_fourth_process(self, postdata):
        # checked
        default = 0
        twen_fourth_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=24))
        return twen_fourth_question

    def twen_fifth_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        twen_fifth_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=25))
        return twen_fifth_question

    def twen_sixth_process(self, postdata):
        # checked
        default = 0
        twen_sixth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=26))
        return twen_sixth_question

    def twen_seventh_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        twen_seventh_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=27))
        return twen_seventh_question

    def twen_eighth_process(self, postdata):
        # checked
        default = 0
        twen_eighth_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=28))
        return twen_eighth_question

    def twen_nine_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        twenty_nine_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=postdata['choice'], low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=29))
        return twenty_nine_question

    def thirthy_process(self, postdata):
        # checked
        default = 0
        thirty_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=30))
        return thirty_question

    def thirty_one_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        thirty_one_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=postdata['choice'], low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=31))
        return thirty_one_question

    def thirty_two_process(self, postdata):
        # checked
        default = 0
        thirty_two_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=postdata['choice'], low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=32))
        return thirty_two_question

    def thirty_three_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        thirty_three_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=33))
        return thirty_three_question

    def thirty_four_process(self, postdata):
        # checked
        default = 0
        thirty_four_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=34))
        return thirty_four_question

    def thirty_five_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        thirty_five_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=35))
        return thirty_five_question

    def thirty_six_process(self, postdata):
        # checked
        default = 0
        thirty_six_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=36))
        return thirty_six_question

    def thirty_seven_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        thirty_seven_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=37))
        return thirty_seven_question

    def thirty_eight_process(self, postdata):
        # checked
        default = 0
        thirty_eight_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=38))
        return thirty_eight_question

    def thirty_nine_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        thirty_nine_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=39))
        return thirty_nine_question

    def fourty_process(self, postdata):
        # checked
        default = 0
        fourty_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=40))
        return fourty_question

    def fourty_one_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fourty_one_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=41))
        return fourty_one_question

    def fourty_two_process(self, postdata):
        # checked
        default = 0
        fourty_two_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=42))
        return fourty_two_question

    def fourty_three_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fourty_three_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=43))
        return fourty_three_question

    def fourty_four_process(self, postdata):
        # checked
        default = 0
        fourty_four_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=default, high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=44))
        return fourty_four_question

    def fourty_five_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fourty_five_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=45))
        return fourty_five_question

    def fourty_six_process(self, postdata):
        # checked
        default = 0
        fourty_six_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=46))
        return fourty_six_question

    def fourty_seven_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fourty_seven_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=47))
        return fourty_seven_question

    def fourty_eight_process(self, postdata):
        # checked
        default = 0
        fourty_eight_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=48))
        return fourty_eight_question

    def fourty_nine_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fourty_nine_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=49))
        return fourty_nine_question

    def fifty_process(self, postdata):
        # checked
        default = 0
        fifty_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=50))
        return fifty_question

    def fifty_one_process(self, postdata):
        # checked
        default = 0
        print(postdata)
        fifty_one_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=51))
        return fifty_one_question

    def fifty_two_process(self, postdata):
        # checked
        default = 0
        fifty_two_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=52))
        return fifty_two_question

    def fifty_three_process(self, postdata):
        # checked
        default = 0
        fifty_three_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=postdata['choice'], question=Question.objects.get(pk=53))
        return fifty_three_question

    def fifty_four_process(self, postdata):
        # checked
        default = 0
        fifty_four_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=54))
        return fifty_four_question

    def fifty_five_process(self, postdata):
        # checked
        default = 0
        fifty_five_question = Categories.objects.create(high_insulin=default, low_tyroids=postdata['choice'], high_cortisol=default, low_cortisal=postdata['choice'], high_androgen=default, low_androgen=postdata['choice'], estrogen_dominace=postdata['choice'],  estrogen_progesterone=default, question=Question.objects.get(pk=55))
        return fifty_five_question

    def fifty_six_process(self, postdata):
        default = 0
        value = []
        fifty_six_question = Categories.objects.create(high_insulin=postdata['choice'], low_tyroids=postdata['choice'], high_cortisol=postdata['choice'], low_cortisal=postdata['choice'], high_androgen=postdata['choice'], low_androgen=postdata['choice'], estrogen_dominace=default,  estrogen_progesterone=default, question=Question.objects.get(pk=56))
        return fifty_six_question


class Categories(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    high_insulin = models.IntegerField(default=0)
    low_tyroids = models.IntegerField(default=0)
    high_cortisol = models.IntegerField(default=0)
    low_cortisal = models.IntegerField(default=0)
    high_androgen = models.IntegerField(default=0)
    low_androgen = models.IntegerField(default=0)
    estrogen_dominace = models.IntegerField(default=0)
    estrogen_progesterone = models.IntegerField(default=0)
    objects = CategoriesManager()

    def __str__(self):
        return "High Insulin: " + str(self.high_insulin) + ', ' + "Low Tyroids: " + str(self.low_tyroids) + ', ' + "High Cortisal: " + str(self.high_cortisol) + ', ' + "Low Cortisal: "  + str(self.low_cortisal) + ', ' + "High Andregon: " + str(self.high_androgen) + ', ' + "Low Androgen: "+ str(self.low_androgen) + ', ' + "Estrogen Dominance: "+ str(self.estrogen_dominace) + ', '+ "Estrogen Progesterone: " + str(self.estrogen_progesterone) + ', ' + "Question: " + str(self.question.id)

#
# class Result(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Categories, related_name='categories')
#     questions = models.ManyToManyField(Question, related_name = 'questions')
#
