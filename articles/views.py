import random
from django.template.loader import render_to_string
from articles.models import Article
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    random_id = random.randint(1, 2)
    # loading from database(model)
    article_obj = Article.objects.get(id=random_id)
    article_list = Article.objects.all()
    context = {
        "Object_list": article_list,
        "Object": article_obj,
        "Title": article_obj.title,
        "Content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)


# def article_page(request, id, *args, **kwargs): # additional arguments passed with request
#     print('')
def article_page(request, id): # additional arguments passed with request
    articles_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
        context = {
            "object": article_obj,
        }
        return render(request, "articles/detail.html", context=context)

    # data = json.loads(request.body)
    # article_id = data['id']
    # print('article_id: ', article_id)
    # laoding from databse
    # print(Article.objects.all())
    # data = Article.objects.all()
    # print(type(data))
    # title = data[0].title
    # content = data[0].content

    # data = Article.objects.all().values()
    # # data = Article.objects.filter(id=1)
    # title = data[0]['title']
    # content = data[0]['content']
    #
    # # post = Article.objects.all()
    # # for item in post.iterator():
    # #     print(item.id)
    # #     title = item.title
    # #     content = item.content
    #
    #     # Django HTML template
    # H1_STRING = f"""
    # <h2>{title}</h2>
    #
    # """
    # P_STRING = f"""
    # <p>{content}</p>
    # """
    #
    # HTML_STRING = H1_STRING + P_STRING
