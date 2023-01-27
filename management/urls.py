from django.urls import path, re_path
from management.views.pjt import get_all_pjt, ajax_get_pjt_member
from management.views import code, code_list, code_add

app_name = 'management'

urlpatterns = [
    path('pjt/', get_all_pjt, name='pjt_list'),
    path('code/', code, name='code'),
    path('code/list', code_list, name='code_list'),
    path('code/add', code_add, name='code_add'),




    # ajax api
    path('ajax/pjtmem', ajax_get_pjt_member, name='get_pjt_mem'),
    ]