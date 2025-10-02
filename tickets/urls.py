from operator import index

from django.urls import path
from .views import *
urlpatterns =[

    path('', index, name = 'dashboard'),
    path('tickets', index, name='tickets'),

    path('tickets/create',ticket_create , name='tickets-create'),

    path('tickets/<int:id>, detail' , ticket_detail, name = 'tickets-detail'),

    path('tickets/edit/<int:id>', ticket_update, name='tickets-update'),

    path('tickets/delete/<int:id>',ticket_delete , name='tickets-delete'),
]