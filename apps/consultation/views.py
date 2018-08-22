from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Question, Categories
from apps.home.models import User
# from apps.home.models import User


# Create your views here.


def index(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    return render(request, 'consultations/index.html')
def index_process(request):
    first = Question.objects.get(id=1)
    context = {'first': first}
    return render(request, 'consultations/first.html', context)

def first_process(request):
    postdata = {'choice': request.POST['choice']}
    second = Question.objects.get(id=2)
    context = {'second':second}
    process = Categories.objects.first_process(postdata)
    return render(request, 'consultations/second.html', context)
#
def second_process(request):
    postdata = {'choice': request.POST['choice']}
    third = Question.objects.get(id=3)
    context = {'third':third}
    process = Categories.objects.second_process(postdata)
    return render(request, 'consultations/third.html', context)

def third_process(request):
    postdata = {'choice': request.POST['choice']}
    fourth = Question.objects.get(id=4)
    context = {'fourth':fourth}
    process = Categories.objects.third_process(postdata)
    return render(request, 'consultations/fourth.html', context)
#
def fourth_process(request):
    postdata = {'choice': request.POST['choice']}
    fifth = Question.objects.get(id=5)
    process = Categories.objects.fourth_process(postdata)
    context = {'fifth':fifth}
    return render(request, 'consultations/fifth.html', context)
#
# def fifth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     process = Categories.objects.fifth_process(postdata)
#     sixth= Question.objects.get(id=6)
#     context = {'sixth':sixth}
#     return render(request, 'consultations/sixth.html', context)
#
# def sixth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     process = Categories.objects.sixth_process(postdata)
#     seventh = Question.objects.get(id=7)
#     context = {'seventh':seventh}
#     return render(request, 'consultations/seventh.html', context)
#
# def seventh_process(request):
#     postdata = {'choice': request.POST['choice']}
#     process = Categories.objects.seventh_process(postdata)
#     eighth = Question.objects.get(id=8)
#     context = {'eighth':eighth}
#     return render(request, 'consultations/eighth.html', context)
#
# def eighth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     ninth= Question.objects.get(id=9)
#     process = Categories.objects.eighth_process(postdata)
#     context = {'ninth':ninth}
#     return render(request, 'consultations/ninth.html', context)
#
# def ninth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     tenth= Question.objects.get(id=10)
#     process = Categories.objects.ninth_process(postdata)
#     context = {'tenth':tenth}
#     return render(request, 'consultations/tenth.html', context)
#
# def tenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     process = Categories.objects.ten_process(postdata)
#     eleventh = Question.objects.get(id=11)
#     context = {'eleventh':eleventh}
#     return render(request, 'consultations/eleventh.html', context)
#
# def eleventh_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twelveth = Question.objects.get(id=12)
#     context = {'twelveth':twelveth}
#     process = Categories.objects.eleventh_process(postdata)
#     return render(request, 'consultations/twelveth.html', context)
#
# def twelveth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     thirtheenth = Question.objects.get(id=13)
#     context = {'thirtheenth':thirtheenth}
#     process = Categories.objects.twelveth_process(postdata)
#     return render(request, 'consultations/thirtheenth.html', context)
#
# def thirtheenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     fourtheenth = Question.objects.get(id=14)
#     context = {'fourtheenth':fourtheenth}
#     process = Categories.objects.thirtheenth_process(postdata)
#     return render(request, 'consultations/fourtheenth.html', context)
#
# def fourtheenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     fiftheenth = Question.objects.get(id=15)
#     context = {'fiftheenth':fiftheenth}
#     process = Categories.objects.fourtheenth_process(postdata)
#     return render(request, 'consultations/fiftheenth.html', context)
#
# def fiftheenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     sixtheenth = Question.objects.get(id=16)
#     process = Categories.objects.fiftheenth_process(postdata)
#     context = {'sixtheenth':sixtheenth}
#     return render(request, 'consultations/sixtheenth.html', context)
# def sixtheenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     seventheenth = Question.objects.get(id=17)
#     process = Categories.objects.sixtheenth_process(postdata)
#     context = {'seventheenth':seventheenth}
#     return render(request, 'consultations/seventheenth.html', context)
#
# def seventheenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     eightheenth = Question.objects.get(id=18)
#     process = Categories.objects.seventheenth_process(postdata)
#     context = {'eightheenth':eightheenth}
#     return render(request, 'consultations/eightheenth.html', context)
#
# def eighteenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     nintheenth = Question.objects.get(id=19)
#     process = Categories.objects.eightheenth_process(postdata)
#     context = {'nintheenth':nintheenth}
#     return render(request, 'consultations/nintheenth.html', context)
#
# def nintheenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twenth = Question.objects.get(id=20)
#     process = Categories.objects.nintheenth_process(postdata)
#     context = {'twenth':twenth}
#     return render(request, 'consultations/twenth.html', context)
#
# def twenth_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_one = Question.objects.get(id=21)
#     context = {'twen_one':twen_one}
#     process = Categories.objects.twentheeth_process(postdata)
#     return render(request, 'consultations/twen_one.html', context)
#
# def twen_one_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twent_two = Question.objects.get(id=22)
#     context = {'twent_two':twent_two}
#     process = Categories.objects.twen_one_process(postdata)
#     return render(request, 'consultations/twent_two.html', context)
#
# def twen_two_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_three = Question.objects.get(id=23)
#     context = {'twen_three':twen_three}
#     process = Categories.objects.twen_two_process(postdata)
#     return render(request, 'consultations/twen_three.html', context)
#
# def twen_third_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_four = Question.objects.get(id=24)
#     process = Categories.objects.twen_three_process(postdata)
#     context = {'twen_four':twen_four}
#     return render(request, 'consultations/twen_four.html', context)
#
# def twen_four_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_five = Question.objects.get(id=25)
#     context = {'twen_five':twen_five}
#     process = Categories.objects.twen_fourth_process(postdata)
#     return render(request, 'consultations/twen_five.html', context)
#
# def twen_five_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_six = Question.objects.get(id=26)
#     process = Categories.objects.twen_fifth_process(postdata)
#     context = {'twen_six':twen_six}
#     return render(request, 'consultations/twen_six.html', context)
#
# def twen_six_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_seven = Question.objects.get(id=27)
#     process = Categories.objects.twen_sixth_process(postdata)
#     context = {'twen_seven':twen_seven}
#     return render(request, 'consultations/twen_seven.html', context)
#
# def twen_seven_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_eight = Question.objects.get(id=28)
#     context = {'twen_eight':twen_eight}
#     process = Categories.objects.twen_seventh_process(postdata)
#     return render(request, 'consultations/twen_eight.html', context)
#
# def twen_eight_process(request):
#     postdata = {'choice': request.POST['choice']}
#     twen_nine = Question.objects.get(id=29)
#     context = {'twen_nine':twen_nine}
#     process = Categories.objects.twen_eighth_process(postdata)
#     return render(request, 'consultations/twen_nine.html', context)
#
# def twen_nine_process(request):
#     postdata = {'choice': request.POST['choice']}
#     thirthy = Question.objects.get(id=30)
#     context = {'thirthy':thirthy}
#     process = Categories.objects.twen_nine_process(postdata)
#     return render(request, 'consultations/thirthy.html', context)
#
# def thirthy_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_one = Question.objects.get(id=31)
#     context = {'third_one':third_one}
#     process = Categories.objects.thirthy_process(postdata)
#     return render(request, 'consultations/third_one.html', context)
#
# def third_one_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_two = Question.objects.get(id=32)
#     context = {'third_two':third_two}
#     process = Categories.objects.thirty_one_process(postdata)
#     return render(request, 'consultations/third_two.html', context)
#
# def third_two_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_three = Question.objects.get(id=33)
#     context = {'third_three':third_three}
#     process = Categories.objects.thirty_two_process(postdata)
#     return render(request, 'consultations/third_three.html', context)
#
# def third_three_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_four = Question.objects.get(id=34)
#     context = {'third_four':third_four}
#     process = Categories.objects.thirty_three_process(postdata)
#     return render(request, 'consultations/third_four.html', context)
#
# def third_four_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_five = Question.objects.get(id=35)
#     context = {'third_five':third_five}
#     process = Categories.objects.thirty_four_process(postdata)
#     return render(request, 'consultations/third_five.html', context)
#
# def third_five_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_six = Question.objects.get(id=36)
#     context = {'third_six':third_six}
#     process = Categories.objects.thirty_five_process(postdata)
#     return render(request, 'consultations/third_six.html', context)
#
# def third_six_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_seven = Question.objects.get(id=37)
#     context = {'third_seven':third_seven}
#     process = Categories.objects.thirty_six_process(postdata)
#     return render(request, 'consultations/third_seven.html', context)
#
# def third_seven_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_eight = Question.objects.get(id=38)
#     context = {'third_eight':third_eight}
#     process = Categories.objects.thirty_seven_process(postdata)
#     return render(request, 'consultations/third_eight.html', context)
#
# def third_eight_process(request):
#     postdata = {'choice': request.POST['choice']}
#     third_nine = Question.objects.get(id=39)
#     context = {'third_nine':third_nine}
#     process = Categories.objects.thirty_eight_process(postdata)
#     return render(request, 'consultations/third_nine.html', context)
#
# def third_nine_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_zero = Question.objects.get(id=40)
#     context = {'four_zero':four_zero}
#     process = Categories.objects.thirty_nine_process(postdata)
#     return render(request, 'consultations/four_zero.html', context)
#
# def four_zero_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_one = Question.objects.get(id=41)
#     context = {'four_one':four_one}
#     process = Categories.objects.fourty_process(postdata)
#     return render(request, 'consultations/four_one.html', context)
#
# def four_one_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_two = Question.objects.get(id=42)
#     context = {'four_two':four_two}
#     process = Categories.objects.fourty_one_process(postdata)
#     return render(request, 'consultations/four_two.html', context)
#
# def four_two_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_three = Question.objects.get(id=43)
#     context = {'four_three':four_three}
#     process = Categories.objects.fourty_two_process(postdata)
#     return render(request, 'consultations/four_three.html', context)
#
# def four_three_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_four = Question.objects.get(id=44)
#     context = {'four_four':four_four}
#     process = Categories.objects.fourty_three_process(postdata)
#     return render(request, 'consultations/four_four.html', context)
#
# def four_four_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_five = Question.objects.get(id=45)
#     context = {'four_five':four_five}
#     process = Categories.objects.fourty_four_process(postdata)
#     return render(request, 'consultations/four_five.html', context)
#
# def four_five_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_six = Question.objects.get(id=46)
#     context = {'four_six':four_six}
#     process = Categories.objects.fourty_five_process(postdata)
#     return render(request, 'consultations/four_six.html', context)
#
# def four_six_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_seven = Question.objects.get(id=47)
#     context = {'four_seven':four_seven}
#     process = Categories.objects.fourty_six_process(postdata)
#     return render(request, 'consultations/four_seven.html', context)
#
# def four_seven_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_eight = Question.objects.get(id=48)
#     context = {'four_eight':four_eight}
#     process = Categories.objects.fourty_seven_process(postdata)
#     return render(request, 'consultations/four_eight.html', context)
#
#
# def four_eight_process(request):
#     postdata = {'choice': request.POST['choice']}
#     four_nine = Question.objects.get(id=49)
#     context = {'four_nine':four_nine}
#     process = Categories.objects.fourty_eight_process(postdata)
#     return render(request, 'consultations/four_nine.html', context)
#
# def four_nine_process(request):
#     postdata = {'choice': request.POST['choice']}
#     five_zero = Question.objects.get(id=50)
#     context = {'five_zero':five_zero}
#     process = Categories.objects.fourty_nine_process(postdata)
#     return render(request, 'consultations/five_zero.html', context)
#
# def five_zero_process(request):
#     postdata = {'choice': request.POST['choice']}
#     five_one = Question.objects.get(id=51)
#     context = {'five_one':five_one}
#     process = Categories.objects.fifty_process(postdata)
#     return render(request, 'consultations/five_one.html', context)
#
# def five_one_process(request):
#     postdata = {'choice': request.POST['choice']}
#     five_two = Question.objects.get(id=52)
#     context = {'five_two':five_two}
#     process = Categories.objects.fifty_one_process(postdata)
#     return render(request, 'consultations/five_two.html', context)
#
# def five_two_process(request):
#     postdata = {'choice': request.POST['choice']}
#     five_three = Question.objects.get(id=53)
#     context = {'five_three':five_three}
#     process = Categories.objects.fifty_two_process(postdata)
#     return render(request, 'consultations/five_three.html', context)
#
# def five_three_process(request):
#     postdata = {'choice': request.POST['choice']}
#     five_four = Question.objects.get(id=54)
#     context = {'five_four':five_four}
#     process = Categories.objects.fifty_three_process(postdata)
#     return render(request, 'consultations/five_four.html', context)
#
# def five_four_process(request):
#     postdata = {'choice': request.POST['choice']}
#     five_five = Question.objects.get(id=55)
#     context = {'five_five':five_five}
#     process = Categories.objects.fifty_four_process(postdata)
#     return render(request, 'consultations/five_five.html', context)

def five_five_process(request):
    postdata = {'choice': request.POST['choice']}
    fifty_six = Question.objects.get(id=56)
    context = {'fifty_six':fifty_six}
    process = Categories.objects.fifty_five_process(postdata)
    return render(request, 'consultations/final.html', context)

def final_process(request, *args, **kwargs):
    if 'user_id' not in request.session:
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    questions = Question.objects.all()
    postdata = {'choice': request.POST['choice']}
    if result in Categories.objects.first_process(result):
        categories = result
        print(categories)
        return categories
    context = {'user':user, 'questions':questions, 'categories': categories}
    process = Categories.objects.fifty_six_process(postdata)
    return render(request, 'consultations/results.html', context)
#remember to go back to 5th html to change it back to final_process to fifth_process
