#!/bin/bash
export PGPASSWORD=insecure
export IP=`minikube ip`

for fn in `ls ../data/[1-4].json`; do
  ogr2ogr \
    -append \
    -sql 'SELECT 
      Soortnaam_NL AS nl_naam,
      Soortnaam_WTS AS wetenschappelijke_naam,
      Boomnummer AS nummer,
      Boomhoogte AS hoogte,
      Boomtype AS type,
      plantjaar AS plantjaar,
      eigenaar AS eigenaar,
      beheerder AS beheerder,
      categorie AS categorie,
      SOORT_KORT AS geslacht_naam,
      sdview AS sdview,
      radius AS radius
    FROM BOMEN' \
    Pg:"dbname=bomen host=$IP user=admin port=31642" \
    $fn
done
