from django.conf.urls import patterns, include, url
from manual_selection import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('general.urls')),
    url(r'^manual-selection/', views.ManualSelectionView.as_view()),
)
