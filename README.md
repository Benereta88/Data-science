# Data-science
# För att pusha din kod till GitHub, följ dessa steg:

# Steg 1: Initiera ett Git-repository (om du inte redan har gjort det)
# Navigera till din projektkatalog och initiera ett Git-repository:

cd /Users/benereta/Data-science/inlupp/uppgift-2
git init

# Steg 2: Lägg till dina filer till staging-området
# Lägg till dina filer till staging-området:

git add uppgift-2.py

# Steg 3: Skapa en commit
# Skapa en commit med ett meddelande:

git commit -m "Uppdatera uppgiften"

# Steg 4: Lägg till din GitHub-fjärrrepository
# Lägg till din GitHub-fjärrrepository (ersätt URL_TO_YOUR_REPO med URL:en till din GitHub-repository):

git remote add origin main

# Steg 5: Pusha dina ändringar till GitHub
# Pusha dina ändringar till GitHub:

git push -u origin master
# Om du redan har en fjärrrepository och har gjort ändringar tidigare, kan du bara köra:

git push
# Detta kommer att pusha ändringar till GitHub-repository.

