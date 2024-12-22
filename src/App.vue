<script setup lang="ts">
// Importer RouterView pour afficher les composants enfants selon les routes
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <!-- Structure principale de l'application -->
  <div id="app">
    <!-- Header global -->
    <header>
     
      <nav>
        <RouterLink to="/" class="nav-link">Accueil</RouterLink>
        <RouterLink to="/about" class="nav-link">À propos</RouterLink>
        <RouterLink to="/dashboard" class="nav-link">Tableau de bord</RouterLink>
        <RouterLink to="/alerts" class="nav-link">Alertes</RouterLink>
        <RouterLink to="/personnalisation" class="nav-link">Personnaliser</RouterLink>
      </nav>
    </header>

    <!-- Contenu principal : affichage des routes -->
    <main>
      <RouterView />
    </main>

    <!-- Footer global -->
    <footer>
      <p>&copy; 2024 WALLeSmart. Tous droits réservés.</p>
    </footer>
  </div>
</template>

<style scoped>
/* Styles globaux pour l'application */
#app {
  font-family: "Roboto", Arial, sans-serif;
  color: #333;
  text-align: center;
}

header {
  background-color: #e74c3c;
  color: white;
  padding: 20px 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

header .logo {
  display: block;
  margin: 0 auto 10px;
}

nav {
  margin-top: 15px;
}

nav .nav-link {
  margin: 0 15px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  transition: color 0.3s;
}

nav .nav-link:hover {
  color: #ffc107;
}

main {
  margin: 20px auto;
  max-width: 1200px;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

footer {
  margin-top: 20px;
  padding: 15px 0;
  background-color: #333;
  color: white;
  font-size: 0.9em;
  text-align: center;
}
</style>
