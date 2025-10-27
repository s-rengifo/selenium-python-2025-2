Feature: Buscar un artista y validar la fecha del ultimo release
  Scenario: Validar la fecha del ultimo lanzamiento de Mac Miller
    Given el usuario esta en el home page de last.fm
    When busca al artista "Mac Miller"
    And selecciona el primer resultado
    Then la fecha del ultimo release dede ser "24 October 2025"