from django.shortcuts import render,redirect

from .models import Post

from .forms import PostForm,CommentForm

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.
def post_list(request):
    data = Post.objects.all()
    return render(request,'post_list.html',{'posts':data})

class PostList(ListView):
    model = Post
# -----------------------------------------------------------------------------------------
class PostDatail(DetailView):
    model = Post

def post_detail(request,pk):

    data = Post.objects.get(id=pk)

    form = CommentForm()
    return render(request,'blog/post_detail.html',{'post':data,'form':form})





# -----------------------------------------------------------------------------------------
def new_post(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.author = request.user
            myform.save()
        return redirect('/blog')
    else:
        form = PostForm()
    return render(request,'new_post.html',{'form': form})


class PostCreate(CreateView):
    model = Post
    fields =  ['title','content','create_date','draft','tags','author','image']

    success_url = '/blog'




def edit_post(request,post_id):
    data = Post.objects.get(id=post_id)
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.author = request.user
            myform.save()
        return redirect('/blog')
    else:
        form = PostForm(instance=data)
    return render(request,'edit_post.html',{'form': form})



class PostUpdate(UpdateView):
    model = Post
    fields =  ['title','content','create_date','draft','tags','author','image']
    success_url = '/blog'
    template_name = 'blog/edit_post.html'

# ------------------------------------------------------------------------------------------------


def delete_post(request,post_id):
     data = Post.objects.get(id=post_id)
     data.delete()
     return redirect('/blog')





class PostDelete(DeleteView):
    model =  Post 
    success_url = '/blog'

    