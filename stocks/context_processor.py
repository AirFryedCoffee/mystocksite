from .views import get_trending_tickers
from .views import trending_tickers_view

def trending_tickers(request):
    trending_tickers_data = get_trending_tickers()
    return {'trending_tickers': trending_tickers_data}
