from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class HealthCheckView(View):
    """
    A simple health check endpoint that returns the status of the application.
    """
    def get(self, request):
        return JsonResponse({
            'status': 'healthy',
            'message': 'OurMoney.Africa backend is running'
        })
