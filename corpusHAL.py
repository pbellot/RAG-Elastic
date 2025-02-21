import requests
import json

def download_pdf(hal_id, save_path):
    url = f"https://hal.archives-ouvertes.fr/{hal_id}/document"

    try:
        reponse = requests.get(url)
    except requests.ReadTimeout:
        print ("temps limite atteint")
        
    if reponse.status_code==200:
        with open(save_path+"/"+hal_id+".pdf", "wb") as pdf_file:
            pdf_file.write(reponse.content)
        print(f"Le fichier PDF {hal_id} a été téléchargé avec succès et enregistré sous {save_path}")
    else:
        print(f"Erreur lors du téléchargement du PDF {hal_id} : Statut {reponse.status_code}")


keywords = "(quantum OR qubit OR qbit OR NISQ OR entaglement OR superposition OR decoherence)"
query = "q=title_t:"+keywords+"&q=abstract_t:"+keywords
anneeDebut = 2021
anneeFin = 2021
recherche = query+"&fq=producedDateY_i:["+str(anneeDebut)+" TO "+str(anneeFin)+"]&fl=halId_s,authFullName_s,title_s&rows=10&wt=json"

#interrogation de l'API :
try:
    requete = "https://api.archives-ouvertes.fr/search/?"+recherche
    print("Requête posée sur HAL : "+requete)
    reponses = requests.get(requete, timeout=(300,300))
except requests.ReadTimeout:
    print ("temps limite atteint")

#Récupération des PDF pour les documents trouvés    
j = json.loads(reponses.text) #transformation de la chaîne JSON envoyée par l'API en objet Python
print(json.dumps(j, indent=3)) #affichage du JSON complet
documents=j['response']['docs'] #liste des documents trouvés
print(documents[0]) #affichage du premier document trouvé
for doc in documents: #pour chaque document dans la liste
    print(doc['halId_s']) #affiche de l'Id du document dans HAL
    download_pdf(doc['halId_s'],"data/PDF")
    