from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RouterDetailsSerializer
# Create your views here.
import random
from RandomWordGenerator import RandomWord
from randmac import RandMac
from .models import *
def home(request):
	return render(request,'index.html')
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/r/tlst/',
		'Detail View':'/r/tinfo/<str:pk>/',
		'Create':'/r/tcreate/',
		'Update':'/r/tupdate/<str:pk>/',
		'Delete':'/r/tdelete/<str:pk>/',
		'Bulk Create': '/r/tbulk/',
		}

	return Response(api_urls)

@api_view(['GET'])
def routerList(request):
	routers=RouterDetails.objects.all()
	ser=RouterDetailsSerializer(routers,many=True)
	return Response(ser.data)

@api_view(['GET'])
def routerinfo(request,pk):
	routers=RouterDetails.objects.get(rid=pk)
	ser=RouterDetailsSerializer(routers,many=False)
	return Response(ser.data)

@api_view(['POST'])
def routerCreate(request):
	ser=RouterDetailsSerializer(data=request.data)
	print(request.data)
	data={}
	if ser.is_valid():
		ser.save()
		data['created']="Created"
		return Response(data=data)
	data['Not created']="Not Created"
	return Response(data=data)

@api_view(['POST'])
def routerUpdate(request,pk):
	router=RouterDetails.objects.get(rid=pk)
	ser=RouterDetailsSerializer(instance=router,data=request.data)
	data={}
	if ser.is_valid():
		ser.save()
		data['Updated']="Updated"
		return Response(data=data)
	data['Invalid input']="Invalid Input"
	return Response(data=data)

@api_view(['DELETE'])
def routerDelete(request,pk):
	router=RouterDetails.objects.get(rid=pk)
	router.delete()
	return Response("Router Details deleted")

@api_view(['GET','POST'])

def routerBulk(request):
	print("dfgdgf")
	rw = RandomWord(max_word_size=5)
	res=[]
	val={}
	for i in range(0,3):

		tmp=str(rw.generate())
		val["sapid"]=tmp+str(i)
		val["hostname"]=tmp
		val["loopbackid"]=".".join(map(str, (random.randint(0, 255) for _ in range(4))))
		val["mac_add"]=str(RandMac())
		ser=RouterDetailsSerializer(data=val)
		print(ser)
		if ser.is_valid():
			ser.save()
			print("****")
			res.append(val["loopbackid"])

	return Response(res)