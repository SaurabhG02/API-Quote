from django.urls import path,include
from quote.views import QuoteAPIView, QuoteUpdateAPIView

urlpatterns = [
    path('quotes',QuoteAPIView.as_view()),
    path('quotes/<int:id>',QuoteUpdateAPIView.as_view()),
    # path('posts',PostAPIView.as_view()),
    # path('posts/<int:id>',PostUpdateAPIView.as_view()),
]