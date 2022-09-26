km_per_dag = int(input('Geef km per dag :'))
km_totaal = int(input('Geef km totaal'))
aantaldagen = km_totaal//km_per_dag
vandaag = 1
dagaankomst = vandaag + aantaldagen
print(dagaankomst)