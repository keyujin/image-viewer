from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Imgs, Target

# Global number of targets to display in edit
PAGE_SIZE = 5;

# Create your views here.

def index(request):
    img = Imgs.objects.all().order_by('-pk')[0]
    return render(request, "viewer/index.html", {'image': img})

def submit(request):
    return render(request, "viewer/submit.html")

def interop(request):
    data = Target.objects.order_by('pk')
    return render(request, "viewer/interop.html", {'data': data})

@api_view(['POST','GET'])
def edit(request, page_number):
	if page_number is None:
		page_number = (int)(1)
	else:
		page_number = (int)(page_number)

	objects = Target.objects.order_by('pk')
	objects_paged = Paginator(objects, PAGE_SIZE)
	total_pages = objects_paged.num_pages
	data = objects_paged.get_page(page_number)

	return render(request, "viewer/edit.html", {'data': data, 'page_number':page_number, 'page_size':PAGE_SIZE, 'total_pages':total_pages})

@api_view(['POST','GET'])
def resizePage(request):
	global PAGE_SIZE
	if request.data.get("pageSize") is not None:
		PAGE_SIZE = request.data.get("pageSize")
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)
	return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def submitImage(request):
    img1 = request.data.get("myimg")
    obj = Imgs(img=img1)
    obj.save()

    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def submitToInterop(request):
    orientation = request.data.get("orientation")
    shape = request.data.get("shape")
    alphanumeric = request.data.get("alphanumeric")
    color = request.data.get("color")
    img = request.data.get("image")

    t = Target(orientation=orientation, shape=shape, alphanumeric=alphanumeric, color=color, image=img)
    t.save()

    return Response(status=status.HTTP_200_OK)

@api_view(['POST','GET'])
def updateImage(request, item_id):
	obj = Target.objects.get(pk=item_id)
	obj.orientation = request.data.get("orientation")
	obj.shape = request.data.get("shape")
	obj.alphanumeric = request.data.get("alphanumeric")
	obj.color = request.data.get("color")
	obj.image = request.data.get("image")
	obj.save()
	return Response(status=status.HTTP_200_OK)

@api_view(['POST','GET'])
def deleteTarget(request):
	key = request.data.get("key");
	print(key);
	Target.objects.filter(pk=key).delete();
	return Response(status=status.HTTP_200_OK)
