# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# Though everything else is in English, strings will be in pt-BR.


# Vampire Clans
class Clan(models.Model):
    # Longest clan name is Filhas da Cacofonia?
    idClan = models.AutoField(primary_key=True, verbose_name="ID do Clã")
    clanName = models.CharField(max_length=19, unique=True,
               verbose_name="nome")

    def __unicode__(self):
        return "%s" % (self.clanName)

    class Meta:
        verbose_name = "Clã"
        verbose_name_plural = "Clãs"


# Vampire Sects
class Sect(models.Model):
    idSect = models.AutoField(primary_key=True, verbose_name="ID da Seita")
    # Longest sect name is independents?
    sectName = models.CharField(max_length=13, unique=True,
               verbose_name="nome")

    def __unicode__(self):
        return "%s" % (self.sectName)

    class Meta:
        verbose_name = "Seita"
        verbose_name_plural = "Seitas"


# Vampire Disciplines
class Discipline(models.Model):
    idDiscipline = models.AutoField(primary_key=True,
                   verbose_name="ID da Disciplina")
    # Longest discipline name is Obtenebration?
    disciplineName = models.CharField(max_length=13, unique=True,
                     verbose_name="nome")

    def __unicode__(self):
        return "%s" % (self.disciplineName)

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


# Backgrounds
class Background(models.Model):
    idBackground = models.AutoField(primary_key=True,
                   verbose_name="ID do Antecedente")
    # Longest discipline name is what?
    backgroundName = models.CharField(max_length=30, unique=True,
                     verbose_name="nome")

    def __unicode__(self):
        return "%s" % (self.backgroundName)

    class Meta:
        verbose_name = "Antecedente"
        verbose_name_plural = "Antecedentes"


# Paths of Enlightment (it must include morality)
class Path(models.Model):
    idPath = models.AutoField(primary_key=True, verbose_name="ID da Trilha")
    # Longest path name is ??
    pathName = models.CharField(max_length=30, unique=True,
               verbose_name="nome")

    def __unicode__(self):
        return "%s" % (self.pathName)

    class Meta:
        verbose_name = "Trilha"
        verbose_name_plural = "Trilhas"


# Archetypes
class Archetype(models.Model):
    idArchetype = models.AutoField(primary_key=True,
             verbose_name="ID do Arquétipo")
    # Longest archetype name is ??
    archetypeName = models.CharField(max_length=20, unique=True,
                    verbose_name="nome")

    def __unicode__(self):
        return "%s" % (self.archetypeName)

    class Meta:
        verbose_name = "Arquétipo"
        verbose_name_plural = "Arquétipos"


# Merits
class Merit(models.Model):
    idMerit = models.AutoField(primary_key=True, verbose_name="ID da Qualidade")
    # Longest merit name is ??
    meritName = models.CharField(max_length=40, unique=True,
                verbose_name="nome")
    meritValue = models.IntegerField(verbose_name="Número de Pontos")

    def __unicode__(self):
        return "%s (%s)" % (self.meritName, self.meritValue)

    class Meta:
        verbose_name = "Qualidade"
        verbose_name_plural = "Qualidades"


# Flaws
class Flaw(models.Model):
    idFlaw = models.AutoField(primary_key=True, verbose_name="ID do Defeito")
    # Longest flaw name is ??
    flawName = models.CharField(max_length=40, unique=True,
               verbose_name="nome")
    flawValue = models.IntegerField(verbose_name="Número de Pontos")

    def __unicode__(self):
        return "%s (%s)" % (self.flawName, self.flawValue)

    class Meta:
        verbose_name = "Defeito"
        verbose_name_plural = "Defeitos"


# Generations
class Generation(models.Model):
    idGen = models.AutoField(primary_key=True, verbose_name="ID da Geração")
    gen = models.CharField(max_length=3, verbose_name="Geração")

    def __unicode__(self):
        return "%s" % (self.gen)

    class Meta:
        verbose_name = "Geração"
        verbose_name_plural = "Gerações"

PHY_CHOICES = (
    ("str", "Força"),
    ("dex", "Destreza"),
    ("sta", "Vigor"),
    )
SOC_CHOICES = (
    ("char", "Carisma"),
    ("man", "Manipulação"),
    ("appa", "Aparência"),
    )
MEN_CHOICES = (
    ("per", "Percepção"),
    ("int", "Inteligência"),
    ("wits", "Raciocínio"),
    )


# Character
class Character(models.Model):
    idChar = models.AutoField(primary_key=True, verbose_name="Personagem")
    # Character Information
    playerName = models.CharField(max_length=40, verbose_name="Nome do Jogador")
    charName = models.CharField(max_length=40,
                                verbose_name="Nome do Personagem")
    charGen = models.ForeignKey("Generation", verbose_name="Geração")
    charClan = models.ForeignKey("Clan", verbose_name="Clã")
    charArchetype = models.ForeignKey("Archetype", verbose_name="Arquétipo")
    charPath = models.ForeignKey("Path", verbose_name="Trilha")
    charSect = models.ForeignKey("Sect", verbose_name="Seita")
    charConcept = models.CharField(max_length=20, verbose_name="Conceito",
                                   blank=True)
    charWill = models.IntegerField(validators=[MinValueValidator(1),
                                   MaxValueValidator(6)],
                                   verbose_name="Força de Vontade")
    charMorality = models.IntegerField(validators=[MinValueValidator(1),
                                   MaxValueValidator(6)],
                                   verbose_name="Moralidade")
    # Attributes
    charPhysical = models.IntegerField(verbose_name="Físico")
    charSocial = models.IntegerField(verbose_name="Social")
    charMental = models.IntegerField(verbose_name="Mental")
    charPhyFocus = models.CharField("Foco Físico", max_length=255,
                                    choices=PHY_CHOICES)
    charSocFocus = models.CharField("Foco Social", max_length=255,
                                    choices=SOC_CHOICES)
    charMenFocus = models.CharField("Foco Mental", max_length=255,
                                    choices=MEN_CHOICES)

    # Skills
    academics = models.IntegerField(verbose_name="Acadêmicos", default="0")
    animalken = models.IntegerField(verbose_name="Empatia com Animais",
                                    default="0")
    athletics = models.IntegerField(verbose_name="Esportes", default="0")
    awareness = models.IntegerField(verbose_name="Prontidão", default="0")
    brawl = models.IntegerField(verbose_name="Briga", default="0")
    computer = models.IntegerField(verbose_name="Computador", default="0")
    crafts = models.IntegerField(verbose_name="Artes", default="0")
    dodge = models.IntegerField(verbose_name="Esquiva", default="0")
    drive = models.IntegerField(verbose_name="Condução", default="0")

    empathy = models.IntegerField(verbose_name="Empatia", default="0")
    firearms = models.IntegerField(verbose_name="Armas de Fogo", default="0")
    intimidation = models.IntegerField(verbose_name="Intimidação", default="0")
    investigation = models.IntegerField(verbose_name="Investigação",
                                        default="0")
    leadership = models.IntegerField(verbose_name="Liderança", default="0")
    linguistics = models.IntegerField(verbose_name="Linguística", default="0")
    lore = models.IntegerField(verbose_name="Lore", default="0")
    medicine = models.IntegerField(verbose_name="Medicina", default="0")
    melee = models.IntegerField(verbose_name="Armas Brancas", default="0")
    occult = models.IntegerField(verbose_name="Ocultismo", default="0")

    performance = models.IntegerField(verbose_name="Performance", default="0")
    science = models.IntegerField(verbose_name="Ciências", default="0")
    security = models.IntegerField(verbose_name="Segurança", default="0")
    stealth = models.IntegerField(verbose_name="Furtividade", default="0")
    streetwise = models.IntegerField(verbose_name="Manha", default="0")
    subterfuge = models.IntegerField(verbose_name="Lábia", default="0")
    survival = models.IntegerField(verbose_name="Sobrevivência", default="0")

    # Backgrounds
    aBackground = models.ForeignKey("Background", verbose_name="", blank=True,
                                    related_name='+', null=True)
    aBackgroundLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    bBackground = models.ForeignKey("Background", verbose_name="", blank=True,
                                    related_name='+', null=True)
    bBackgroundLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    cBackground = models.ForeignKey("Background", verbose_name="", blank=True,
                                    related_name='+', null=True)
    cBackgroundLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    dBackground = models.ForeignKey("Background", verbose_name="", blank=True,
                                    related_name='+', null=True)
    dBackgroundLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    eBackground = models.ForeignKey("Background", verbose_name="", blank=True,
                                    related_name='+', null=True)
    eBackgroundLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    # Merits
    aMerit = models.ForeignKey("Merit", verbose_name="", blank=True,
                                    related_name='+', null=True)
    bMerit = models.ForeignKey("Merit", verbose_name="", blank=True,
                                    related_name='+', null=True)
    cMerit = models.ForeignKey("Merit", verbose_name="", blank=True,
                                    related_name='+', null=True)
    dMerit = models.ForeignKey("Merit", verbose_name="", blank=True,
                                    related_name='+', null=True)
    eMerit = models.ForeignKey("Merit", verbose_name="", blank=True,
                                    related_name='+', null=True)

    # Flaws
    aFlaw = models.ForeignKey("Flaw", verbose_name="", blank=True,
                                    related_name='+', null=True)
    bFlaw = models.ForeignKey("Flaw", verbose_name="", blank=True,
                                    related_name='+', null=True)
    cFlaw = models.ForeignKey("Flaw", verbose_name="", blank=True,
                                    related_name='+', null=True)
    dFlaw = models.ForeignKey("Flaw", verbose_name="", blank=True,
                                    related_name='+', null=True)
    eFlaw = models.ForeignKey("Flaw", verbose_name="", blank=True,
                                    related_name='+', null=True)

    # Disciplines
    aDiscipline = models.ForeignKey("Discipline", verbose_name="", blank=True,
                                    related_name='+', null=True)
    aDisciplineLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    bDiscipline = models.ForeignKey("Discipline", verbose_name="", blank=True,
                                    related_name='+', null=True)
    bDisciplineLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    cDiscipline = models.ForeignKey("Discipline", verbose_name="", blank=True,
                                    related_name='+', null=True)
    cDisciplineLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    dDiscipline = models.ForeignKey("Discipline", verbose_name="", blank=True,
                                    related_name='+', null=True)
    dDisciplineLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    eDiscipline = models.ForeignKey("Discipline", verbose_name="", blank=True,
                                    related_name='+', null=True)
    eDisciplineLevel = models.IntegerField(verbose_name="Nível", default="",
                                           blank=True, null=True,
                                           validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])
    # Notes
    diablerie = models.BooleanField(default=False, verbose_name="Diablerrizado")
    destroyed = models.BooleanField(default=False, verbose_name="Destruído")
    introduced = models.BooleanField(default=False, verbose_name="Apresentado")
    vaulderie = models.BooleanField(default=False, verbose_name="Vaulderie")
    hunted = models.BooleanField(default=False, verbose_name="Caçado")
    notes = models.TextField(max_length=1024, verbose_name="Notas")

    def __unicode__(self):
        return "%s" % (self.charName)

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"
