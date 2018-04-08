import time
from django.shortcuts import render
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from app.utils import fibonacci_calculation
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)




def fib_number(request):
    num = 0
    result = 0
    time_taken = 0
    try:
        if request.GET.get('number'):
            start_time = time.time()
            number = request.GET.get('number')
            try:
                num = int(number)
            except ValueError as e:
                return render(
                    request,
                    'index.html',
                    {
                        'number': num,
                        'result': "Value is not a whole number",
                        'time_taken': time_taken
                    }
                )
            if num < 0:
                return render(
                    request,
                    'index.html',
                    {
                        'number': num,
                        'result': "Value should not be negative number",
                        'time_taken': time_taken
                    }
                )
            if num in cache:
                result = cache.get(num)
                end_time = time.time() - start_time
                time_taken = str(end_time)[0:8]
            else:
                result = fibonacci_calculation(num)
                cache.set(num, result, timeout=CACHE_TTL)
                final_time = time.time() - start_time
                time_taken = str(final_time)[0:8]
    except Exception as e:
        return render(
            request,
            'index.html',
            {
                'number': num,
                'result': e,
                'time_taken': time_taken
            }
        )



    return render(
        request,
        'index.html',
        {
            'number': num,
            'result': result,
            'time_taken': time_taken
        }
    )



