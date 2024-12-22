<template>
  <div class="home">
    <header>
      <h1>WALLeSmart</h1>
      <nav>
        <RouterLink to="/">Accueil</RouterLink>
        <RouterLink to="/about">À propos de l'application</RouterLink>
        <RouterLink to="/app">Logiciel</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
      </nav>
    </header>

    <div class="content">
      <h2>Bienvenue sur notre outil d'aide à la réforme Win Lose !</h2>
      <p>
        Notre application est conçue pour vous fournir un outil d'aide à la réforme,
        vous permettant de classer les vaches de votre troupeau.
      </p>
      <img
        src="@/assets/search_icon.png"
        alt="Icône de recherche"
        class="search-icon"
        @click="openApp"
      />
    </div>

    <footer>
      <div class="logo">
        <img src="@/assets/logo1.png" alt="Wallonie recherche CRA-W" />
        <img src="@/assets/logo2.png" alt="éleveo" />
        <img src="@/assets/logo3.png" alt="Université de Liège" />
        <img src="@/assets/logo4.png" alt="UMONS Université de Mons" />
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
const openApp = () => {
  window.location.href = "/app";
};
</script>

<style scoped>
header {
  background-color: #e74c3c;
  padding: 20px;
  text-align: center;
  color: white;
}

nav a {
  margin: 0 15px;
  text-decoration: none;
  color: white;
}

.content {
  text-align: center;
  background-color: #fff;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin: 20px auto;
  max-width: 800px;
}

.search-icon {
  width: 60px;
  cursor: pointer;
  margin-top: 20px;
  transition: transform 0.3s;
}

.search-icon:hover {
  transform: scale(1.1);
}
</style>
