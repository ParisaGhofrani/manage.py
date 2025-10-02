from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

from tickets.models import Ticket



def index(request):
    tickets = Ticket.objects.prefetch_related('tags').all()
#    print("\n",tickets[0].tags, tickets[0].id, "\n")

    return render(request, template_name='index.html', context={'tickets':tickets})


def ticket_create(request):
    return HttpResponse('TicketCreated ')

def ticket_detail(request):
    return HttpResponse('Ticket Detail')

def ticket_update(request):
    return HttpResponse('Ticket update')


def ticket_delete(request):
    return HttpResponse('TicketRemove')