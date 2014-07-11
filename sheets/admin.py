# -*- coding: utf-8 -*-
from django.contrib import admin
from sheets.models import Clan, Sect, Discipline, Path, Archetype
from sheets.models import Merit, Flaw, Character, Generation, Background


# Register your models here.
class AdminClan(admin.ModelAdmin):
    fieldsets = [
            ('Informações do Clã', {'fields': ['clanName']})
            ]
    list_display = ['clanName']


class AdminSect(admin.ModelAdmin):
    fieldsets = [
            ('Informações da Seita', {'fields': ['sectName']})
            ]
    list_display = ['sectName']


class AdminDiscipline(admin.ModelAdmin):
    fieldsets = [
            ('Informações da Disciplina', {'fields': ['disciplineName']})
            ]
    list_display = ['disciplineName']


class AdminBackground(admin.ModelAdmin):
    fieldsets = [
            ('Informações do Antecedente', {'fields': ['backgroundName']})
            ]
    list_display = ['backgroundName']


class AdminPath(admin.ModelAdmin):
    fieldsets = [
            ('Informações da Trilha', {'fields': ['pathName']})
            ]
    list_display = ['pathName']


class AdminArchetype(admin.ModelAdmin):
    fieldsets = [
            ('Informações do Arquétipo', {'fields': ['archetypeName']})
            ]
    list_display = ['archetypeName']


class AdminMerit(admin.ModelAdmin):
    fieldsets = [
            ('Informações do Mérito', {'fields': ['meritName', 'meritValue']})
            ]
    list_display = ['meritName', 'meritValue']


class AdminFlaw(admin.ModelAdmin):
    fieldsets = [
            ('Informações do Defeito', {'fields': ['flawName', 'flawValue']})
            ]
    list_display = ['flawName', 'flawValue']


class AdminGeneration(admin.ModelAdmin):
    fieldsets = [
            ('Informações da Geração', {'fields': ['gen']})
            ]


class AdminChar(admin.ModelAdmin):
    fieldsets = [
        ('Dados gerais', {'fields': [['playerName', 'charName', 'charGen',
                                    'charArchetype'], ['charSect',
                                    'charClan', 'charConcept'], ['charWill',
                                    'charPath', 'charMorality']]}),
        ('Atributos', {'fields': [['charPhysical', 'charSocial', 'charMental'],
                                  ['charPhyFocus', 'charSocFocus',
                                  'charMenFocus']]}),
        ('Habilidades', {'fields': [['academics', 'empathy', 'performance'],
                                    ['animalken', 'firearms', 'science'],
                                    ['athletics', 'intimidation', 'security'],
                                    ['awareness', 'investigation', 'stealth'],
                                    ['brawl', 'leadership', 'streetwise'],
                                    ['computer', 'linguistics', 'subterfuge'],
                                    ['crafts', 'lore', 'survival'],
                                    ['dodge', 'melee', 'medicine'],
                                    ['drive', 'occult']]}),
        ('Disciplinas', {'fields': [['aDiscipline', 'aDisciplineLevel'],
                                    ['bDiscipline', 'bDisciplineLevel'],
                                    ['cDiscipline', 'cDisciplineLevel'],
                                    ['dDiscipline', 'dDisciplineLevel'],
                                    ['eDiscipline', 'eDisciplineLevel'],
                                    ]}),
        ('Antecedentes', {'fields': [['aBackground', 'aBackgroundLevel'],
                                    ['bBackground', 'bBackgroundLevel'],
                                    ['cBackground', 'cBackgroundLevel'],
                                    ['dBackground', 'dBackgroundLevel'],
                                    ['eBackground', 'eBackgroundLevel'],
                                    ]}),
        ('Qualidades', {'fields': [['aMerit'],
                                    ['bMerit'],
                                    ['cMerit'],
                                    ['dMerit'],
                                    ['eMerit'],
                                    ]}),
        ('Defeitos', {'fields': [['aFlaw'],
                                    ['bFlaw'],
                                    ['cFlaw'],
                                    ['dFlaw'],
                                    ['eFlaw'],
                                    ]}),
        ('Outros', {'fields': [['notes', 'diablerie', 'destroyed', 'vaulderie',
                               'introduced', 'hunted']]})
        ]
    list_display = ['playerName', 'charName', 'charClan', 'charSect',
                    'introduced', 'vaulderie']

admin.site.register(Clan, AdminClan)
admin.site.register(Sect, AdminSect)
admin.site.register(Discipline, AdminDiscipline)
admin.site.register(Background, AdminBackground)
admin.site.register(Path, AdminPath)
admin.site.register(Archetype, AdminArchetype)
admin.site.register(Merit, AdminMerit)
admin.site.register(Flaw, AdminFlaw)
admin.site.register(Generation, AdminGeneration)
admin.site.register(Character, AdminChar)
