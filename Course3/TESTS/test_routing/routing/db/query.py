from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create_user(name):
    user = User(first_name=name[0], last_name=name[1])
    user.save()


def create_blog(title, user_name, created=None):
    author = User.objects.get(first_name=user_name)
    if created:
        blog = Blog(title=title, author=author, created=created)
    else:
        blog = Blog(title=title, author=author)
    blog.save()


def subscribe_user(blog_title, user_name):
    blog = Blog.objects.get(title=blog_title)
    if isinstance(user_name, tuple):
        for name in user_name:
            user = User.objects.get(first_name=name)
            blog.subscribers.add(user)
    elif isinstance(user_name, str):
        user = User.objects.get(first_name=user_name)
        blog.subscribers.add(user)


def create_topic(title, blog_name, author, created=None):
    blog = Blog.objects.get(title=blog_name)
    author = User.objects.get(first_name=author)
    if created:
#        created = datetime.fromisoformat(created)
        topic = Topic(title=title, blog=blog, author=author, created=created)
    else:
        topic = Topic(title=title, blog=blog, author=author)
    topic.save()


def like_topic(topic, user_name):
    topic = Topic.objects.get(title=topic)
    if isinstance(user_name, tuple):
        for name in user_name:
            user = User.objects.get(first_name=name)
            topic.likes.add(user)
    elif isinstance(user_name, str):
        user = User.objects.get(first_name=user_name)
        topic.likes.add(user)


def create():
    create_user(['u1'] * 2)
    create_user(['u2'] * 2)
    create_user(['u3'] * 2)
    create_blog('blog1', 'u1')
    create_blog('blog2', 'u1')
    subscribe_user('blog1', ('u1', 'u2'))
    subscribe_user('blog2', 'u2')
    create_topic('topic1', 'blog1', 'u1')
    create_topic('topic2_content', 'blog1', 'u3', '2017-01-01')
    like_topic('topic1', ('u1', 'u2', 'u3'))


def edit_all():
    User.objects.all().update(first_name='uu1')


def edit_u1_u2():
    User.objects.filter(Q(first_name='u1') | Q(first_name='u2')).update(first_name='uu1')


def delete_u1():
    User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    user = User.objects.get(first_name='u2')
    for blog in Blog.objects.filter(subscribers=user):
        blog.subscribers.remove(user)


def get_topic_created_grated():
    return Topic.objects.filter(created__gt='2018-01-01')


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith='content')


def get_user_with_limit():
    return User.objects.all().order_by('-id')[:2]


def get_topic_count():
    return Blog.objects.annotate(topic_count=Count('topic')).order_by('topic_count')


def get_avg_topic_count():
    return Blog.objects.annotate(topic_count=Count('topic')).aggregate(avg=Avg('topic_count'))


def get_blog_that_have_more_than_one_topic():
    return Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt=1)


def get_topic_by_u1():
    return Topic.objects.filter(author__first_name='u1')


def get_user_that_dont_have_blog():
    return User.objects.annotate(blog_count=Count('blog')).filter(blog_count=0).order_by('id')


def get_topic_that_like_all_users():
    return Topic.objects.all().annotate(likes_count=Count('likes')).filter(likes_count=User.objects.count())


def get_topic_that_dont_have_like():
    return Topic.objects.all().annotate(likes_count=Count('likes')).filter(likes_count=0).order_by('id')