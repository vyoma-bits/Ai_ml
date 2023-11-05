
from django.shortcuts import render,HttpResponse,redirect

from math import ceil
# import the logging library
import logging
import pandas as pd
from sklearn.tree  import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse





from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')


def SignupPage(request):
    if request.method=='POST':
        
        email=request.POST.get('casual leaves')
        
        pass1=request.POST.get('max_no.of cont.days off')
        pass4=request.POST.get('sick leaves')
        pass5=request.POST.get('overtime_hours')
       

        if pass1==-1:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            musi_data=pd.read_csv(r'C:\Users\vyoma123\Desktop\django_ieee\mac\shop\projects.csv')
            X=musi_data.drop(columns=['ACTION','OUTPUT'])
            y=musi_data['OUTPUT']
            X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
            model=DecisionTreeClassifier()
            model.fit(X_train,y_train)
            predictions=model.predict([[email,pass1,pass4,pass5]])
            
            
            
            music_data=pd.read_csv(r'C:\Users\vyoma123\Desktop\django_ieee\mac\shop\projects.csv')
            z=music_data.drop(columns=['ACTION'])
            q=music_data['ACTION']
            z_train, z_test,q_train,q_test=train_test_split(z,q,test_size=0.2)
            model=DecisionTreeClassifier()
            model.fit(z_train,q_train)
            prediction=model.predict([[email,pass1,pass4,pass5,predictions[0]]])
            
            if (prediction[0]=='Not likely to leave'):
                L=[prediction[0]]
            else:
                
                L=[predictions[0]," ",prediction[0]]
            
        
        

        
            
           
        

            return HttpResponse(L)
        
        



    return render (request,'shop/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'shop/LOGIN.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')