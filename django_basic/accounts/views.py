from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .models import CustomUser, Comment
from .forms import CustomUserCreationForm
from .forms import CommentForm
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views import generic

#Ajax用
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class AccountCreateView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = "/accounts/login"  # Redirect to login page after account creation

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'アカウントが正常に作成されました。ログインしてください。')
        return response

#ユーザーの詳細情報の確認
class UserDetail(DetailView):
    model = CustomUser  # UserをCustomUserに変更
    template_name='accounts/accounts_detail.html'

#ログイン
class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = "/accounts/stageselect"
#ログアウト 
class Logout(LogoutView):
    next_page = '/accounts/login'

#コメント作成
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)  # Validate the form data
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('accounts:comment_list')  # Redirect to comment_list view after saving the comment
    else:
        form = CommentForm()
    return render(request, 'comment/stage_coment_create.html', {'form': form})

#コメント閲覧
class CommentList(generic.ListView):
    model = Comment
    template_name = 'comment/stage_coment_list.html'
    context_object_name = 'comments'

# コメント削除
class CommentDelete(generic.DeleteView):
    model = Comment
    template_name = 'comment/stage_coment_delete.html'
    success_url = "/accounts/stageselect/comments"


 
class Home(TemplateView):
    template_name = 'accounts/home.html'

#ページ遷移
class stageselect(TemplateView):
    template_name = 'accounts/stageselect.html'

class stage1(TemplateView):
    template_name = 'game/stage1.html'

class stage2(TemplateView):
    template_name = 'game/stage2.html'

#Ajaxを用いたステージクリアに応じてmodels.pyのstage_cleartを１増やす際の処理
@csrf_exempt
def increase_stage_clear(request):
    if request.method == 'POST':
        model_instance = CustomUser.objects.get(pk=request.POST['id']) # id を元にインスタンスを取得
        model_instance.stage_cleart += 1
        model_instance.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

