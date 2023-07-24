fur=input('Fur: ')
for line in open('species.csv'):
  line=line.strip()
  b=line.split(',')
  if fur=='y':
    eggs=input('Eggs: ')
    if eggs=='y':
      print(f'Common name: {b[1]}\nScientific name: Tachyglossus aculeatus\nTaxonomic class: Mammalia\nDiet: carnivorous\nHabitat: bush\nIdentified by: fur, eggs') 
      break
    elif eggs=='n':
      neck=input('Long neck: ')
      if neck=='y':
        tongue=input('Barbed Tongue: ')
        if tongue=='y':
          print('Common name: northern giraffe\nScientific name: Giraffa camelopardalis\nTaxonomic class: Mammalia\nDiet: herbivorous\nHabitat: savannah\nIdentified by: fur, barbed tongue, long neck, no eggs')
          break
        elif tongue=='n':
          print('Common name: one-humped camel\nScientific name: Camelus dromedarius\nTaxonomic class: Mammalia\nDiet: herbivorous\nHabitat: arid\nIdentified by: fur, no eggs, long neck, no barbed tongue')
          break
      elif neck=='n':
        print('Common name: domestic cat\nScientifc name: Felis catus\nTaxonomic class: Mammalia\nDiet: carnivorous\nHabitat: urban\nIdentified by: fur, no eggs, no long neck')
        break
  elif fur=='n':
    trunk=input('Trunk: ')
    if trunk=='y':
      print('Common name: African bush elephant\nScientific name: Loxodonta africana\nTaxonomic class: Mammalia\nDiet: herbivorous\nHabitat: arid\nIdentified by: no fur, trunk')
      break
    elif trunk=='n':
      eggs=input('Eggs: ')
      if eggs=='n':
        print('Common name: sheep\nScientific name: Ovis aries\nTaxonomic class: Mammalia\nDiet: herbivorous\nHabitat: farmland\nIdentified by: no fur, no trunk, no eggs')
        break
      elif eggs=='y':
        claws=input('Claws: ')
        if claws=='y':
          print('Common name: Eastern blue tongue\nScientific name: Tiliqua scincoides\nTaxonomic class: Reptilia\nDiet: omnivorous\nHabitat: bush\nIdentified by: no fur, no trunk, eggs, claws')
          break
        elif claws=='n':
          print('Common name: Australian green tree frog\nScientific name: Litoria caerulea\nTaxonomic class: Amphibia\nDiet: carnivorous\nHabitat: rainforest\nIdentified by: no fur, no trunk, eggs, no claws')
          break
    