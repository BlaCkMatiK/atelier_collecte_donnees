SELECT 
    GID,
    DATE_DEBUT,
    DATE_FIN,
    COMMUNE,
    LOCALISATION_EMPRISE,
    gid_acte
FROM {{ ref('travaux') }}