from django.db import models

class PaisMaestro(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    pais = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pais_maestro'


class InformacionPais(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    pais = models.ForeignKey('PaisMaestro', on_delete=models.PROTECT,related_name='pais_informacion')
    anio = models.FloatField(blank=True, null=True)
    poblacion = models.FloatField(blank=True, null=True)
    pbi = models.FloatField(blank=True, null=True)
    gen_elect = models.FloatField(blank=True, null=True)
    dem_elect = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informacion_pais'


class ConsumoPais(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    informacion = models.ForeignKey('InformacionPais', on_delete=models.PROTECT,
                    related_name='informacion_consumo')
    codigo = models.TextField(blank=True, null=True)
    anio = models.FloatField(blank=True, null=True)
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
        db_table = 'consumo_pais'



class ProduccionPais(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    informacion = models.ForeignKey('InformacionPais', on_delete=models.PROTECT,
                    related_name='informacion_produccion')
    anio = models.FloatField(blank=True, null=True)
    codigo = models.TextField(blank=True, null=True)
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
        db_table = 'produccion_pais'

class HuellaPais(models.Model):
    pais = models.TextField(blank=True, null=True)
    codigo = models.CharField(primary_key=True, max_length=3)
    continente = models.TextField(blank=True, null=True)
    indice_objetivos_desarrollo_sostenible = models.FloatField(db_column='indice objetivos desarrollo sostenible', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    expectativa_vida = models.FloatField(db_column='expectativa vida', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indice_desarrollo_humano = models.FloatField(db_column='indice desarrollo humano', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pib_per_capita = models.TextField(db_column='pib per capita', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    grupo_ingresos = models.TextField(db_column='grupo ingresos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    poblacion = models.TextField(blank=True, null=True)
    huella_carbono = models.FloatField(db_column='huella carbono', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    huella_ecologica = models.FloatField(db_column='huella ecologica', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    biocapacidad = models.FloatField(blank=True, null=True)
    tierra = models.FloatField(blank=True, null=True)
    idpais = models.TextField(db_column='Idpais', blank=True, null=True)  # Field name made lowercase.
    idcontinente = models.TextField(db_column='Idcontinente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'huella_pais'

class EmisionesPais(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    pais = models.CharField(max_length=100)
    continente = models.CharField(max_length=100)
    n2019 = models.FloatField(db_column='2019', blank=True, null=True)
    n2018 = models.FloatField(db_column='2018', blank=True, null=True)
    n2017 = models.FloatField(db_column='2017', blank=True, null=True)
    n2016 = models.FloatField(db_column='2016', blank=True, null=True)
    n2015 = models.FloatField(db_column='2015', blank=True, null=True)
    n2014 = models.FloatField(db_column='2014', blank=True, null=True)
    n2013 = models.FloatField(db_column='2013', blank=True, null=True)
    n2012 = models.FloatField(db_column='2012', blank=True, null=True)
    n2011 = models.FloatField(db_column='2011', blank=True, null=True)
    n2010 = models.FloatField(db_column='2010', blank=True, null=True)
    n2009 = models.FloatField(db_column='2009', blank=True, null=True)
    n2008 = models.FloatField(db_column='2008', blank=True, null=True)
    n2007 = models.FloatField(db_column='2007', blank=True, null=True)
    n2006 = models.FloatField(db_column='2006', blank=True, null=True)
    n2005 = models.FloatField(db_column='2005', blank=True, null=True)
    n2004 = models.FloatField(db_column='2004', blank=True, null=True)
    n2003 = models.FloatField(db_column='2003', blank=True, null=True)
    n2002 = models.FloatField(db_column='2002', blank=True, null=True)
    n2001 = models.FloatField(db_column='2001', blank=True, null=True)
    n2000 = models.FloatField(db_column='2000', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emisiones_pais'


class MundialMaestro(models.Model):
    anio = models.PositiveIntegerField(primary_key=True)
    poblacion = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mundial_maestro'


class HuellaMundial(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    anio = models.ForeignKey('MundialMaestro', models.PROTECT, db_column='anio',
                        related_name='mundial_huella')
    biocapacidad = models.FloatField(blank=True, null=True)
    huella_ecologica = models.FloatField(blank=True, null=True)
    tierra = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huella_mundial'


class GasesMundial(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    anio = models.ForeignKey('MundialMaestro', models.PROTECT, db_column='anio',
                        related_name='mundial_gases')
    N2O = models.FloatField(db_column='N2O', blank=True, null=True)
    SF6 = models.FloatField(db_column='SF6', blank=True, null=True)
    CO2 = models.FloatField(db_column='CO2', blank=True, null=True)
    CH4 = models.FloatField(db_column='CH4', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gases_mundial'


class TemperaturaMundial(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    anio = models.ForeignKey(MundialMaestro, models.PROTECT, db_column='anio',
                        related_name='mundial_temperatura')
    MAT = models.FloatField(db_column='MAT', blank=True, null=True)
    lim_sup = models.FloatField(blank=True, null=True)
    lim_inf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temperatura_mundial'


class PrediccionMundial(models.Model):
    anio = models.PositiveIntegerField(primary_key=True)
    emision_co2 = models.FloatField(blank=True, null=True)
    produccion_energia = models.FloatField(blank=True, null=True)
    var_emision_co2 = models.FloatField(blank=True, null=True)
    var_produccion_energia = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prediccion_mundial'