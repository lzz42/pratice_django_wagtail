from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice
# Create your views here.


def index(request):
    # 获取数据
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 载入模板
    template = loader.get_template('polls/index.html')
    # 构建上下文
    context = {
        'latest_question_list': latest_question_list,
    }
    # 生成响应
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello you're at polls index")


def admin(request):
    return HttpResponse("helle this is Admin")


def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question ID %s not exist" % str(question_id))
    return render(request, 'polls/detail.html', {'question': q})
    # return HttpResponse("You are looking question: %s"%question_id)


def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': q})


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
        pass
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': q, 'error_message': "You do not select a choice"})
        pass
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))

# ---------------------------------------------------------------------------------------


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date = timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
