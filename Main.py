#Pour lancer le code il faut remplir ces 5 lignes et lancer loop()

NOM_FICHIER = "Gouttes" #Le fichier exclusif
PATH = "C:/Users/me/AppData/Roaming/Mozilla/Firefox/Profiles/" #Absolute :)
LIEN = "https://www.lilo.org/fr/ensemble-agissons-pour-le-logement/" #Le lien web
TEMPS_ENTRE_REQ = 0.05 #EN SECONDES --> pas surcharger le serveur
CHEMIN_DOSSIER_EXPORT = "C:/Users/apzoeiruty/Desktop" #Le dossier de l'extenion --> ne pas changer son nom



#FIN INITIALISATION
NB_PROFILS = int(20/TEMPS_ENTRE_REQ + 1)
if PATH[-1] != "/" : #On patch PATH
    PATH += "/"
print("Avec ces paramètres ça donne " + str(3600 * 24 / (TEMPS_ENTRE_REQ * 1000)) + "€ par jour")

import urllib
import time
import random
import webbrowser 
from selenium import webdriver
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Lopo(unittest.TestCase):
    def setUp(self, profil, link):
        self.driver = webdriver.Firefox(profil)
        self.driver.implicitly_wait(30)
        self.driver.get(link)
        self.base_url = "https://www.lilo.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.test_lopo()
        self.test_lopo()
    
    def test_lopo(self):
        driver = self.driver
        driver.find_element_by_css_selector("input.shadow").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

def initialisationProfils(nb) :
    loc = PATH + NOM_FICHIER + "/"
    
    #Il faut notre plugin
    os.chdir(CHEMIN_DOSSIER_EXPORT + "/Export")
    l = os.listdir()
    
    os.chdir(PATH)
    if not (NOM_FICHIER in os.listdir()) :
        os.mkdir(loc)
    os.chdir(loc)
    deja = len(os.listdir())
    profils = []
    for i in range(deja, deja + nb) :
        if not str(i) in os.listdir() :
            shutil.copytree(CHEMIN_DOSSIER_EXPORT + "/Export", loc + str(i))
            print("Profil " + str(i) + " réalisé")
            profils.append(str(i))
    return profils

def recuperationProfils(profils) :
    browser = []
    loc = PATH + NOM_FICHIER + "/"
    for i in profils :
        fp = webdriver.FirefoxProfile(loc + i)
        b = webdriver.Firefox(fp)
        b.get("http://www.google.fr")
        browser.append(b)
        print("Profil " + i + " initialisé")
    return browser

def request(bliste) :
    for i in bliste :
        i.get("https://search.lilo.org/searchweb.php?q=bonjour")
        print("Requête avec " + str(i) + " effectuée")

def loop() :
    compteur = 0
    while True :
        compteur += 1
        #On creait les profils
        print("Initialisation")
        profils = initialisationProfils(NB_PROFILS)
        
        #On les index dans browser
        browser = recuperationProfils(profils)
        
        print("Debut du combat")
        #Et c'est pour 150 gouttes par profil
        for i in range(150) :
            for j in browser :
                j.get("https://search.lilo.org/searchweb.php?q=bonjour")
                time.sleep(TEMPS_ENTRE_REQ)
        
        print("Fin du combat, gouttes récoltées : " + str(NB_PROFILS * 150 * compteur))
        #On collecte les gouttes
        for k in profils :
            time.sleep(TEMPS_ENTRE_REQ)
            l = Lopo()
            l.setUp(k, LIEN) #Donne la moitié
            l.setUp(k, LIEN) #Donne l'autre moitié
