from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home_page'),
    url(r'^about/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^person_detail/(?P<pk>\d+)/$', views.PersonDetailView.as_view(), name='person_detail'),
    url(r'^add/$', views.CreatePersonView.as_view(), name='add_person'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeletePersonView.as_view(), name='delete_person'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdatePersonView.as_view(), name='update_person'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^user_login/$', auth_views.LoginView.as_view(template_name='myapp/user_login.html'), name='user_login'),
    url(r'^new_customer_entry/$', views.CustomerEntryView.as_view(), name='new_customer_entry'),
    url(r'^customer_list/$', views.CustomerListView.as_view(), name='customer_list'),
    url(r'^update_customer/(?P<pk>\d+)/$', views.UpdateCustomerView.as_view(), name='update_customer'),
    url(r'^customer_information/(?P<pk>\d+)/$', views.CustomerInformation.as_view(), name='customer_info')

]
