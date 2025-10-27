Feature: Buscar una pelicula y validar el titulo de la pelicula y el rating
  Scenario: Validar el titulo y el rating de la pagina de Inception
    Given el usuario esta en el home page de imdb
    When busca la pelicula "Inception"
    And selecciona el resultado inception
    Then el titulo de la pelicula dede ser "Inception"
    And el rating de la pelicula debe ser "8.8"