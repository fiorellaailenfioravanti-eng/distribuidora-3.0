import unicodedata
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from apps.productos.models import Producto

# Create your views here.
def normalizar_texto(texto):
    """Elimina tildes y convierte a minúsculas para una búsqueda flexible."""
    if not texto:
        return ""
    # Convierte 'Bidón' en 'Bidon'
    texto = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
    return texto.lower().strip()

def buscar_productos(request):
    query_original = request.GET.get('q', '').strip()
    query_limpia = normalizar_texto(query_original)

    if not query_limpia:
        resultados = Producto.objects.none()
    else:
        # 1. Búsqueda por frase completa (prioridad)
        resultados = Producto.objects.filter(
            Q(nombre__icontains=query_original) | Q(nombre__icontains=query_limpia)
        )

        # 2. Si no hay nada, buscamos por "Raíz de palabra"
        # Esto permitirá que 'coc' o 'coca' tengan más chances de encontrar 'Cola'
        if not resultados.exists():
            palabras = query_limpia.split()
            q_fuzzy = Q()
            for p in palabras:
                if len(p) >= 3:
                    # Buscamos los primeros 2 caracteres para máxima flexibilidad
                    q_fuzzy |= Q(nombre__icontains=p[:2]) 
                else:
                    q_fuzzy |= Q(nombre__icontains=p)
            
            resultados = Producto.objects.filter(q_fuzzy).distinct()


    # Paginación (Mantenemos tus 6 productos por página)
    paginator = Paginator(resultados.order_by('nombre'), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {
        'query': query_original,
        'lista_productos': page_obj, # Nombre que usa tu resultados_busqueda.html
    }
    return render(request, 'buscador/resultados_busqueda.html', contexto)