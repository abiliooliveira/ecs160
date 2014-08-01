from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from general import views

urlpatterns = patterns('',
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^hosts/$', views.HostList.as_view()),
    url(r'^hosts/(?P<pk>[0-9]+)/$', views.HostDetails.as_view()),
    url(r'^allergies/$', views.AllergieList.as_view()),
    url(r'^allergies/(?P<pk>[0-9]+)/$', views.AllergieDetails.as_view()),
    url(r'^pets/$', views.PetList.as_view()),
    url(r'^pets/(?P<pk>[0-9]+)/$', views.PetDetails.as_view()),
    url(r'^familystructures/$', views.FamilyStructureList.as_view()),
    url(r'^familystructures/(?P<pk>[0-9]+)/$', views.FamilyStructureDetails.as_view()),
    url(r'^students/familystructurepreferences/$', views.FamilyStructurePreferenceList.as_view()),
    url(r'^students/familystructurepreferences/(?P<pk>[0-9]+)/$', views.FamilyStructurePreferenceDetails.as_view()),
    url(r'^requests/$', views.RequestList.as_view()),
    url(r'^requests/(?P<pk>[0-9]+)/$', views.RequestDetails.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)