from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SiteVitrine.urls')),        # site vitrine
    path('beneficiaires/', include('beneficiaires.urls')),  # app bénéficiaires
    # Le service worker est déjà géré dans beneficiaires.urls, 
    # mais pour le scope PWA, il est souvent préférable de le laisser à la racine si besoin.
]
