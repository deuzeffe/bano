SELECT :'dept'||'%' AS deptlike 
\gset
DELETE FROM :schema_cible.lieux_dits WHERE insee_com LIKE :'deptlike';
INSERT INTO :schema_cible.lieux_dits (insee_com,
                       nom,
                       created,
                       updated,
                       geometrie)
SELECT commune,
       --nom,
       regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(nom,'   ',' ','g'),'   ',' ','g'),'  ',' ','g'),'  ',' ','g'),'  ',' ','g'),
       created,
       updated,
       geometrie
FROM   tmp_lieux_dits:dept;
DROP TABLE tmp_lieux_dits:dept;