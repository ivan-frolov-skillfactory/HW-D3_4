
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import News, Category
from datetime import datetime

 
 
class NewsList(ListView):
    model = News  
    template_name = 'news.html'  
    context_object_name = 'news'  
    queryset = News.objects.order_by('-id')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() 
        context['value1'] = None 
        return context
 
class NewsDetail(DetailView):
    model = News 
    template_name = 'detail.html'
    context_object_name = 'detail' 
