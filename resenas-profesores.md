# Reseñas de Profesores

<input type="text" id="search-input" placeholder="Buscar...">
<ul id="results-container"></ul>

## Profesores
  * [Pedro A.](resenas_profesores/pedro_a.md)
  * [Verónica G.](resenas_profesores/veronica_g.md)

## Tutores
  * [Alonso P.](resenas_profesores/alonso_p.md)
  * [Lizeth D.](resenas_profesores/lizeth_d.md)

<script src="/assets/js/jekyll-search.js" type="text/javascript"></script>

<script type="text/javascript">
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '/assets/search_indexes/profesores.json',
    searchResultTemplate: '<li><a href="{url}" title="{desc}">{title}</a></li>',
    noResultsText: 'No se encontraron resultados',
    limit: 10,
    fuzzy: false,
    exclude: ['Welcome']
  })
</script>