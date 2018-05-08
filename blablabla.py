#!/usr/bin/env python3
# Script for generating impressive but meaningless text in the Dutch language.
# Inspired by: http://bullshit.takovermeulen.eu and http://www.jurgensland.nl/download/adviesmatrix.pdf
# Copyleft 2018, Jan Kroon (Hogeschool Rotterdam)

import random
from argparse import ArgumentParser

def main():
   def generate_random_government_sentence():
      # Declare partial sentences
      public_sector_words = []
      public_sector_words.append(["Het proces", "Het format", "Het management", "De communicatie", "De nieuwe organisatie", "Het ontwikkelpad", "De organisatieontwikkeling", "De missie", "Kennismanagement", "De eerste aanzet"])
      public_sector_words.append(["moet meerwaarde leveren bij", "stelt eisen aan", "dient te faciliteren bij", "is uitgangspunt bij", "is onlosmakelijk verbonden met", "schept voorwaarden voor", "dient te focussen op", "stuurt", "hangt nauw samen met", "moet een opstap bieden voor"])
      public_sector_words.append(["de implementatie van", "de terugkoppeling van", "het aftimmeren van", "het aansturen van", "de ontwikkeling van", "de flexibilisering van", "de integratie van", "de inventarisatie van", "de definitie van", "de insteek van"])
      public_sector_words.append(["complexe", "optimale", "met elkaar samenhangende", "eenduidige", "onderling afhankelijke", "structurele", "probleemoplossende", "resultaatgerichte", "efficiënte", "consistente"])
      public_sector_words.append(["beslissingen", "besluitvorming", "oplossingen", "belangen", "teams", "organisatieonderdelen", "oplossingsrichtingen", "uitgangspunten", "protocollen", "memo's"])
      public_sector_words.append(["waarbij het belang van", "waarbij de feedback van", "waarbij het kader voor", "waarbij de afstemming met", "waarbij de structuur van", "waarbij de samenhang met", "waarbij de uitkomst van", "waarbij input van", "waarbij commitment van", "waarbij klankborden met"])
      public_sector_words.append(["strategisch beleid", "de stuurgroep", "de communicatie", "de werkgroepen", "het ministerie", "de buitenwacht", "de markt", "de stakeholders", "de directie", "het beleid"])
      public_sector_words.append(["moet uitkristalliseren.", "voorop staat.", "wordt aangestuurd.", "afgestemd moet worden.", "toegevoegde waarde levert.", "oplossingsgericht is.", "moet worden besloten.", "voldoende draagvlak heeft.", "doorslaggevend is.", "cruciaal is." ])

      sentence = ""
      for i in range(0, len(public_sector_words)):
         sentence = sentence + public_sector_words[i][random.randint(0,9)] + " "
      return(sentence)   

   def generate_random_business_sentence():
      private_sector_words = []
      private_sector_words.append(["Het proces", "De factor mens", "Het management", "De communicatie", "De kerncompetentie", "Human capital",
       "De organisatieontwikkeling", "De missie", "Kennismanagement", "De eerste aanzet"])
      private_sector_words.append(["moet meerwaarde leveren bij", "stelt eisen aan", "dient te faciliteren bij", "is uitgangspunt bij",
       "is onlosmakelijk verbonden met", "schept voorwaarden voor", "dient te focussen op", "stuurt", "hangt nauw samen met",
       "moet een opstap bieden voor"])
      private_sector_words.append(["de implementatie van", "de terugkoppeling van", "het aftimmeren van", "het aansturen van",
       "de ontwikkeling van", "de flexibilisering van", "de integratie van", "de inventarisatie van", "de definitie van", "de insteek van"])
      private_sector_words.append(["complexe", "optimale", "in elkaar grijpende", "eenduidige", "onderling afhankelijke", "structurele",
       "pro-actieve", "resultaatgerichte", "efficiënte", "consistente"])
      private_sector_words.append(["supply chain processen", "business architecture", "mijlpalen", "targets", "business units",
       "organisatie-onderdelen", "scenario's", "best practices", "business models", "conceptplannen"])
      private_sector_words.append(["waarbij het belang van", "waarbij de feedback van", "waarbij het kader voor", "waarbij de afstemming met",
       "waarbij de structuur van", "waarbij de synergie met", "waarbij de interface met", "waarbij input van", "waarbij commitment van",
       "waarbij klankborden met"])
      private_sector_words.append(["strategisch beleid", "de taskforce", "de communicatie", "de werkgroepen", "new business development",
       "de systeemintegratie", "de markt", "de stakeholders", "het management", "de projectorganisatie"])
      private_sector_words.append(["moet uitkristalliseren.", "voorop staat.", "wordt aangestuurd.", "leading is.",
       "toegevoegde waarde levert.", "win-win situaties creërt..", "moet worden gemanaged.", "voldoende draagvlak heeft.", "doorslaggevend is.",
       "cruciaal is."])

      sentence = ""
      for i in range(0, len(private_sector_words)):
         sentence = sentence + private_sector_words[i][random.randint(0,9)] + " "
      return(sentence)

   # Parse command line arguments
   ap = ArgumentParser()
   ap.add_argument('sector', nargs='?')
   ap.add_argument('-n', '--number', type=int, default=1, help="Het aantal zinnen gegenereerde tekst")

   args = ap.parse_args()
   sector = args.sector
   n = args.number

   #print("Bla, Bla, Bla!")

   report = ""
   if (sector == "public"):
      for i in range(0, n):
         report = report + generate_random_government_sentence()
   elif (sector == "private"):
      for i in range(0, n):
         report = report + generate_random_business_sentence()

   print(report)

main()
