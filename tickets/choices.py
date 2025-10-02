
#Ticket Priorities
PRIORITY_CHOICES = [
    ("low", "Low"),
    ("middle", "Middle"),
    ("high", "High" ),

]

PRIORITY_COLORS = {
    "low": "#198754",  #Bootstrap green
    "middle": "#0d6efd",  #Bootstrap blue
    "high": "#dc3545",  #Bootstrap red
}

#Assignment Status
STATUS_CHOICES = [
    ("new" , "New"),
    ("in-progress", "In Progress"),
    ("solved", "Solved"),
    ("impossible", "Impossible"),
]

STATUS_COLORS = {
    "new":"#0dcaf0", #Bootstrap info
    "in-progress": "#198754",
    'solved':"#198754",
    "impossible":"#dc3545"
}