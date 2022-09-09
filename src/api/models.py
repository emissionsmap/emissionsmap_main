from django.db import models


class TablaHecho(models.Model):
    anio = models.TextField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    combustible = models.TextField(blank=True, null=True)
    continente = models.TextField(blank=True, null=True)
    idanio = models.TextField(db_column='Idanio', blank=True, null=True)  # Field 
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field 
    idcombustible = models.TextField(db_column='Idcombustible', blank=True, null=True)  # Field 
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'Tabla_Hecho'


class ElectricidadProdFuenteApilada(models.Model):
    pais = models.TextField(blank=True, null=True)
    continente = models.TextField(blank=True, null=True)
    codigo = models.TextField(primary_key=True)
    anio = models.BigIntegerField(blank=True, null=True)
    carbon = models.FloatField(blank=True, null=True)
    gas = models.FloatField(db_column='a partir gas', blank=True, null=True)  # Field suitable characters.
    hidro = models.FloatField(blank=True, null=True)
    otras_renovables= models.FloatField(db_column='otras renovables incluida la bioenergia', blank=True, null=True)  # Field suitable characters.
    solar = models.FloatField(blank=True, null=True)
    petroleo = models.FloatField(blank=True, null=True)
    viento = models.FloatField(blank=True, null=True)
    nuclear = models.FloatField(db_column='origen nuclear', blank=True, null=True)  # Field suitable characters.
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field 
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field 
    id_anio = models.TextField(db_column='Id_anio', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'electricidad-prod-fuente-apilada'


class Energiaco2(models.Model):
    pais = models.TextField(blank=True, null=True)
    codigo = models.TextField(primary_key=True)
    continente = models.TextField(blank=True, null=True)
    combustible = models.TextField(blank=True, null=True)
    anio = models.BigIntegerField(blank=True, null=True)
    consumo_energia = models.FloatField(db_column='energia',blank=True, null=True)
    produccion_energia = models.FloatField(db_column='produccion energia', blank=True, null=True)  # Field suitable characters.
    pib = models.FloatField(blank=True, null=True)
    poblacion = models.FloatField(blank=True, null=True)
    intensidad_energetica_percap = models.FloatField(db_column='intensidad energetica per capita', blank=True, null=True)  # Field suitable characters.
    intensidad_energetica_pib = models.FloatField(db_column='intensidad energetica por pib', blank=True, null=True)  # Field suitable characters.
    emision_co2 = models.FloatField(db_column='emision co2', blank=True, null=True)  # Field suitable characters.
    consumo_energia_twh = models.FloatField(db_column='energia twh', blank=True, null=True)  # Field suitable characters.
    produccion_energia_twh = models.FloatField(db_column='produccion energia twh', blank=True, null=True)  # Field suitable characters.
    intensidad_energetica_percap_twh = models.FloatField(db_column='intensidad energetica per capita twh', blank=True, null=True)  # Field suitable characters.
    intensidad_energetica_pib_twh = models.FloatField(db_column='intensidad energetica por pib twh', blank=True, null=True)  # Field suitable characters.
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field 
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field 
    idcombustible = models.TextField(db_column='Idcombustible', blank=True, null=True)  # Field 
    id_anio = models.TextField(db_column='Id_anio', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'energiaco2'


class Gases(models.Model):
    anio = models.BigIntegerField(primary_key=True)
    oxido_nitroso = models.FloatField(db_column='medios n20', blank=True, null=True)  # Field suitable characters.
    hexafloruro_azufre = models.FloatField(db_column='medios sf6', blank=True, null=True)  # Field suitable characters.
    dioxido_carbono = models.FloatField(db_column='medios de co2', blank=True, null=True)  # Field suitable characters.
    metano = models.FloatField(db_column='medios canal 4', blank=True, null=True)  # Field suitable characters.
    id_anio = models.TextField(db_column='Id_anio', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'gases'


class HistoricEmissions(models.Model):
    pais = models.TextField(blank=True, null=True)
    codigo = models.TextField(primary_key=True)
    continente = models.TextField(blank=True, null=True)
    fuente_de_datos = models.TextField(db_column='fuente de datos', blank=True, null=True)  # Field suitable characters.
    sector = models.TextField(blank=True, null=True)
    gas = models.TextField(blank=True, null=True)
    unidad = models.TextField(blank=True, null=True)
    year_2019 = models.FloatField(db_column='2019', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2018 = models.FloatField(db_column='2018', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2017 = models.FloatField(db_column='2017', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2016 = models.FloatField(db_column='2016', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2015 = models.FloatField(db_column='2015', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2014 = models.FloatField(db_column='2014', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2013 = models.FloatField(db_column='2013', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2012 = models.FloatField(db_column='2012', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2011 = models.FloatField(db_column='2011', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2010 = models.FloatField(db_column='2010', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2009 = models.FloatField(db_column='2009', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2008 = models.FloatField(db_column='2008', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2007 = models.FloatField(db_column='2007', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2006 = models.FloatField(db_column='2006', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2005 = models.FloatField(db_column='2005', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2004 = models.FloatField(db_column='2004', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2003 = models.FloatField(db_column='2003', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2002 = models.FloatField(db_column='2002', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2001 = models.FloatField(db_column='2001', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_2000 = models.FloatField(db_column='2000', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1999 = models.FloatField(db_column='1999', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1998 = models.FloatField(db_column='1998', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1997 = models.FloatField(db_column='1997', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1996 = models.FloatField(db_column='1996', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1995 = models.FloatField(db_column='1995', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1994 = models.FloatField(db_column='1994', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1993 = models.FloatField(db_column='1993', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1992 = models.FloatField(db_column='1992', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1991 = models.FloatField(db_column='1991', blank=True, null=True)  # Field asn't a valid Python identifier.
    year_1990 = models.FloatField(db_column='1990', blank=True, null=True)  # Field asn't a valid Python identifier.
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field 
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'historic_emissions'


class HuellaBiocapacidad(models.Model):
    anio = models.BigIntegerField(primary_key=True)
    poblacion = models.BigIntegerField(blank=True, null=True)
    biocapacidad_percap = models.FloatField(db_column='biocapacidad percap', blank=True, null=True)  # Field suitable characters.
    huella_ecologica_percap = models.FloatField(db_column='huella ecologica percap', blank=True, null=True)  # Field suitable characters.
    tierra = models.FloatField(blank=True, null=True)
    id_anio = models.TextField(db_column='Id_anio', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'huella_biocapacidad'


class HuellaSosteniblePorPais(models.Model):
    pais = models.TextField(blank=True, null=True)
    codigo = models.TextField(primary_key=True)
    continente = models.TextField(blank=True, null=True)
    desarrollo_sostenible = models.FloatField(db_column='indice objetivos desarrollo sostenible', blank=True, null=True)  # Field suitable characters.
    expectativa_vida = models.FloatField(db_column='expectativa vida', blank=True, null=True)  # Field suitable characters.
    indice_desarrollo_humano = models.FloatField(db_column='indice desarrollo humano', blank=True, null=True)  # Field suitable characters.
    pib_percap = models.TextField(db_column='pib per capita', blank=True, null=True)  # Field suitable characters.
    grupo_ingresos = models.TextField(db_column='grupo ingresos', blank=True, null=True)  # Field suitable characters.
    poblacion = models.TextField(blank=True, null=True)
    huella_carbono = models.FloatField(db_column='huella carbono', blank=True, null=True)  # Field suitable characters.
    huella_ecologica = models.FloatField(db_column='huella ecologica', blank=True, null=True)  # Field suitable characters.
    biocapacidad = models.FloatField(blank=True, null=True)
    tierra = models.FloatField(blank=True, null=True)
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field 
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'huella_sostenible_por_paiss'


class PrimariaSubEnergiaFuente(models.Model):
    pais = models.TextField(blank=True, null=True)
    continente = models.TextField(blank=True, null=True)
    codigo = models.TextField(primary_key=True)
    anio = models.BigIntegerField(blank=True, null=True)
    eolico = models.FloatField(blank=True, null=True)
    hidroelectrico = models.FloatField(blank=True, null=True)
    solar = models.FloatField(blank=True, null=True)
    nuclear = models.FloatField(blank=True, null=True)
    biocombustibles_total = models.FloatField(db_column='biocombustibles    total', blank=True, null=True)  # Field suitable characters.
    biomasa = models.FloatField(blank=True, null=True)
    carbon = models.FloatField(blank=True, null=True)
    aceite = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field 
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field 
    id_anio = models.TextField(db_column='Id_anio', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'primaria-sub-energia-fuente'


class SubEnergiaFosilRenovablesNuclear(models.Model):
    pais = models.TextField(blank=True, null=True)
    continente = models.TextField(blank=True, null=True)
    codigo = models.TextField(primary_key=True)
    anio = models.BigIntegerField(blank=True, null=True)
    combustibles_fosiles = models.FloatField(db_column='combustibles fosiles', blank=True, null=True)  # Field suitable characters.
    renovables = models.FloatField(blank=True, null=True)
    nuclear = models.FloatField(blank=True, null=True)
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field 
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field 
    id_anio = models.TextField(db_column='Id_anio', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'sub-energia-fosil-renovables-nuclear'


class TemperaturaAnomalia(models.Model):
    anio = models.BigIntegerField(primary_key=True)
    temperatura_media = models.FloatField(db_column='anomalia la temperatura media promedio 1961 a 1990', blank=True, null=True)  # Field suitable characters.
    limite_superior = models.FloatField(db_column='limite superior', blank=True, null=True)  # Field suitable characters.
    limite_inferior = models.FloatField(db_column='limite inferior', blank=True, null=True)  # Field suitable characters.
    id_anio = models.TextField(db_column='Id_anio', blank=True, null=True)  # Field 

    class Meta:
        managed = False
        db_table = 'temperatura_anomalia'
