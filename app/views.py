

# """
# To render html web pages
# """
# from articles.models import Article
# from django.http import HttpResponse
#
#
# def home_view(request):
#     # laoding from databse
#     article_obj = Article.objects.get(1)
#     title = article_obj.title
#     content = article_obj.content
#
#     # Django HTML template
#     H1_STRING = f"""
#     <h2>{title}</h2>
#
#     """
#     P_STRING = f"""
#     <p>{content}</p>
#     """
#
#     HTML_STRING = H1_STRING + P_STRING
#     return HttpResponse(HTML_STRING)
