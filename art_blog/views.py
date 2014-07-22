from django.shortcuts import render
from art_blog.models import Article,Comment
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.context_processors import csrf
from forms import ArticleForm,CommentForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required



def main_page(request):
    list_articles=Article.objects.all()
    username=auth.get_user(request).username
    return render(request,'main_page.html',
        {'list_articles':list_articles,'username':username})

def content(request,article_id):
    article=Article.objects.get(id=article_id)
    comments=article.comment_set.all()
    username=auth.get_user(request).username
    return render(request,'article.html',
        {'article':article,'comments':comments,'username':username})

@login_required(login_url='/login/')
def add_article(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.pub_date=timezone.now()
            c.save()
            return HttpResponseRedirect("/")
    else:
        form=ArticleForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render(request,"add_article.html",args)

@login_required(login_url='/login/')
def edit_article(request,article_id):
    a=Article.objects.get(id=article_id)
    username=auth.get_user(request).username
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form=ArticleForm(request.POST,instance=a)
            c=form.save(commit=False)
            c.article=a
            c.pub_date=timezone.now()
            c.save()
            return HttpResponseRedirect("/get/%s/"%a.id)
    else:
        form=ArticleForm(instance=a)
    args={}
    args.update(csrf(request))
    args['form']=form
    args['article']=a
    args['username']=username
    return render(request,"edit_article.html",args)

@login_required(login_url='/login/')
def delete_article(request,article_id):
    a=Article.objects.get(id=article_id)
    a.delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def add_comment(request,article_id):
    a=Article.objects.get(id=article_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.article=a
            c.com_date=timezone.now()
            c.save()
            messages.success(request,'Your comment was successfully added!')
            return HttpResponseRedirect("/get/%s/"% article_id)
    else:
        form=CommentForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['article']=a
    return render(request,'add_comment.html',args)

@login_required(login_url='/login/')
def delete_comment(request,comment_id):
    c=Comment.objects.get(id=comment_id)
    article_id=c.article.id
    c.delete()
    return HttpResponseRedirect('/get/%s'% article_id)


def search_results(request):
    if request.method=='POST':
        search_text=request.POST['search_text']
    else:
        search_text=''
    articles=Article.objects.filter(title__icontains=search_text)
    return render(request,'ajax_search.html',{'articles':articles})

