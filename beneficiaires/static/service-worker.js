const CACHE_NAME = 'aidechain-v1';
const STATIC_ASSETS = [
  '/',
  '/static/css/style.css',
  '/static/manifest.json'
];

// Installation du service worker
self.addEventListener('install', event => {
  console.log('[SW] Installation en cours...');
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[SW] Cache ouvert:', CACHE_NAME);
      return cache.addAll(STATIC_ASSETS).catch(err => {
        console.warn('[SW] Erreur lors de la mise en cache:', err);
      });
    })
  );
  self.skipWaiting();
});

// Activation du service worker
self.addEventListener('activate', event => {
  console.log('[SW] Activation en cours...');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('[SW] Suppression du cache ancien:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Gestion des requêtes réseau
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  // Les requêtes POST sont toujours envoyées au serveur
  if (request.method === 'POST') {
    event.respondWith(fetch(request));
    return;
  }

  // Stratégie Cache-First pour les assets statiques
  if (request.url.includes('/static/')) {
    event.respondWith(
      caches.match(request).then(response => {
        return response || fetch(request).then(response => {
          const clonedResponse = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(request, clonedResponse);
          });
          return response;
        });
      }).catch(() => {
        // Pas de réponse dans le cache et pas de connexion
        return new Response('Ressource non disponible hors ligne', {
          status: 503,
          statusText: 'Service Unavailable'
        });
      })
    );
    return;
  }

  // Stratégie Network-First pour les pages et API
  event.respondWith(
    fetch(request)
      .then(response => {
        if (response.status === 200) {
          const clonedResponse = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(request, clonedResponse);
          });
        }
        return response;
      })
      .catch(() => {
        // En cas d'erreur réseau, retourner le cache si disponible
        return caches.match(request).then(response => {
          return response || new Response('Vous êtes hors ligne', {
            status: 503,
            statusText: 'Service Unavailable'
          });
        });
      })
  );
});
