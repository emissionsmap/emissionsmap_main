from django.db import models


class ConsumoEnergiaPais(models.Model):
    year = models.FloatField(blank=True, null=True)
    iso_code = models.TextField(primary_key=True)
    petroleo = models.FloatField(blank=True, null=True)
    carbon = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    nuclear = models.FloatField(blank=True, null=True)
    hidraulica = models.FloatField(blank=True, null=True)
    solar = models.FloatField(blank=True, null=True)
    eolica = models.FloatField(blank=True, null=True)
    otras_renovables = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumo_energia_pais'


class DatosExtrasEnergiaPais(models.Model):
    year = models.FloatField(blank=True, null=True)
    iso_code = models.TextField(primary_key=True)
    country = models.TextField(blank=True, null=True)
    population = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_extras_energia_pais'


class Gases(models.Model):
    year = models.BigIntegerField(primary_key=True)
    n2o = models.FloatField(db_column='N2O', blank=True, null=True)
    sf6 = models.FloatField(db_column='SF6', blank=True, null=True)
    co2 = models.FloatField(db_column='CO2', blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gases2'


class HistoricoGhg(models.Model):
    country = models.TextField(blank=True, null=True)
    code = models.TextField(primary_key=True)
    continente = models.TextField(blank=True, null=True)
    number_2019 = models.FloatField(db_column='2019', blank=True, null=True)
    number_2018 = models.FloatField(db_column='2018', blank=True, null=True)
    number_2017 = models.FloatField(db_column='2017', blank=True, null=True)
    number_2016 = models.FloatField(db_column='2016', blank=True, null=True)
    number_2015 = models.FloatField(db_column='2015', blank=True, null=True)
    number_2014 = models.FloatField(db_column='2014', blank=True, null=True)
    number_2013 = models.FloatField(db_column='2013', blank=True, null=True)
    number_2012 = models.FloatField(db_column='2012', blank=True, null=True)
    number_2011 = models.FloatField(db_column='2011', blank=True, null=True)
    number_2010 = models.FloatField(db_column='2010', blank=True, null=True)
    number_2009 = models.FloatField(db_column='2009', blank=True, null=True)
    number_2008 = models.FloatField(db_column='2008', blank=True, null=True)
    number_2007 = models.FloatField(db_column='2007', blank=True, null=True)
    number_2006 = models.FloatField(db_column='2006', blank=True, null=True)
    number_2005 = models.FloatField(db_column='2005', blank=True, null=True)
    number_2004 = models.FloatField(db_column='2004', blank=True, null=True)
    number_2003 = models.FloatField(db_column='2003', blank=True, null=True)
    number_2002 = models.FloatField(db_column='2002', blank=True, null=True)
    number_2001 = models.FloatField(db_column='2001', blank=True, null=True)
    number_2000 = models.FloatField(db_column='2000', blank=True, null=True)
    number_1999 = models.FloatField(db_column='1999', blank=True, null=True)
    number_1998 = models.FloatField(db_column='1998', blank=True, null=True)
    number_1997 = models.FloatField(db_column='1997', blank=True, null=True)
    number_1996 = models.FloatField(db_column='1996', blank=True, null=True)
    number_1995 = models.FloatField(db_column='1995', blank=True, null=True)
    number_1994 = models.FloatField(db_column='1994', blank=True, null=True)
    number_1993 = models.FloatField(db_column='1993', blank=True, null=True)
    number_1992 = models.FloatField(db_column='1992', blank=True, null=True)
    number_1991 = models.FloatField(db_column='1991', blank=True, null=True)
    number_1990 = models.FloatField(db_column='1990', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_GHG'


class HuellaMundial(models.Model):
    year = models.BigIntegerField(primary_key=True)
    poblation = models.BigIntegerField(blank=True, null=True)
    biocapacidad_percap = models.FloatField(db_column='biocapacidad percap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    huella_ecologica_percap = models.FloatField(db_column='huella ecologica percap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tierra = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huella_mundial'


class HuellaPais(models.Model):
    country = models.TextField(blank=True, null=True)
    code = models.TextField(primary_key=True)
    continente = models.TextField(blank=True, null=True)
    ids = models.FloatField(db_column='IDS', blank=True, null=True)  # Field name made lowercase.
    ele = models.FloatField(db_column='ELE', blank=True, null=True)  # Field name made lowercase.
    idh = models.FloatField(db_column='IDH', blank=True, null=True)  # Field name made lowercase.
    pib_percap = models.TextField(db_column='PIB_PerCap', blank=True, null=True)  # Field name made lowercase.
    poblacion = models.TextField(blank=True, null=True)
    huella_carbono = models.FloatField(db_column='huella carbono', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    huella_ecologica = models.FloatField(db_column='huella ecologica', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    biocapacidad = models.FloatField(blank=True, null=True)
    tierra = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huella_pais'


class PaisGeojson(models.Model):
    code = models.TextField(db_column='CODE', primary_key=True)  # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pais_geojson'


class ProduccionEnergiaPais(models.Model):
    year = models.FloatField(blank=True, null=True)
    iso_code = models.TextField(primary_key=True)
    petroleo = models.FloatField(blank=True, null=True)
    carbon = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    nuclear = models.FloatField(blank=True, null=True)
    hidraulica = models.FloatField(blank=True, null=True)
    solar = models.FloatField(blank=True, null=True)
    eolica = models.FloatField(blank=True, null=True)
    otras_renovables = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produccion_energia_pais'


class TemperaturaMundial(models.Model):
    year = models.BigIntegerField(primary_key=True)
    mat = models.FloatField(db_column='MAT', blank=True, null=True)  # Field name made lowercase.
    limite_superior = models.FloatField(db_column='limite superior', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    limite_inferior = models.FloatField(db_column='limite inferior', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'temperatura_mundial'

class Predicciones(models.Model):
    year = models.BigIntegerField(primary_key=True)
    emision_co2 = models.FloatField(blank=True, null=True)
    produccion_energia = models.FloatField(blank=True, null=True)
    var_emision_co2 = models.FloatField(blank=True, null=True)
    var_produccion_energia = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predicciones'