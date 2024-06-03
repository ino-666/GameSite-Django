from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
 
app_name = 'accounts'
urlpatterns = [
    path('accounts_create/', views.AccountCreateView.as_view(), name='accounts_create'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Login.as_view(), name='logout'),
    path('accounts_detail/<int:pk>/', login_required(views.UserDetail.as_view()), name='accounts_detail'),
    path('home/', login_required(views.Home.as_view()), name='home'),
    path('stageselect/', login_required(views.stageselect.as_view()), name='stageselect'),
    
    #各ステージへのリンク
    path('stageselect/stage1/', login_required(views.stage1.as_view()), name='stage1'),
    path('stageselect/stage2/', login_required(views.stage2.as_view()), name='stage2'),
    #path('stageselect/stage1/', login_required(views.stage1.as_view()), name='stage1'),

    #各ステージのコメント
    path('stageselect/comment/new/', views.comment_create, name='comment_new'),
    path('stageselect/comment/delete/<int:pk>/',login_required(views.CommentDelete.as_view()), name='comment_delete'),
    path('stageselect/comments/', login_required(views.CommentList.as_view()), name='comment_list'),

    #ステージクリアを判定するstage_cleartを増やす処理、Ajax使用
    path('stageselect/stage1/increase_stage_clear/', views.increase_stage_clear, name='increase_stage_clear'),
]

