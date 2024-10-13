SELECT 
    Bateau,
    Date passage,
    Fermeture totale
FROM {{ ref('pont_chaban') }}