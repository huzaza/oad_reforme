<!-- src/views/Home.vue -->
<template>
  <div>
    <!-- Header -->
    <header>
      <h1>WALLeSmart</h1>
      <nav>
        <a href="/">Accueil</a>
        <a href="#about">À propos de l'application</a>
        <a href="#software">Logiciel</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>

    <!-- Contenu principal -->
    <div class="content">
      <h2>Bienvenue sur notre outil d'aide à la réforme Win Lose !</h2>
      <p>
        Notre application est conçue pour vous fournir un outil d'aide à la réforme, vous permettant de classer les vaches de votre troupeau.
        Basée sur des informations détaillées relatives à la production, à la santé, et bien plus encore, nous vous aidons à prendre des décisions
        éclairées pour optimiser la gestion de votre troupeau.
        Découvrez comment notre outil peut transformer la gestion de votre troupeau en fournissant des analyses précises et des recommandations
        personnalisées pour chaque animal.
      </p>
      <img
        src="@/assets/search_icon.png"
        alt="Icône de recherche"
        class="search-icon"
        @click="openApp"
      />
    </div>

    <!-- Footer -->
    <footer>
      <div class="logo">
        <img src="@/assets/logo1.png" alt="Wallonie recherche CRA-W" />
        <img src="@/assets/logo2.png" alt="éleveo" />
        <img src="@/assets/logo3.png" alt="Université de Liège Gembloux Agro-Bio Tec" />
        <img src="@/assets/logo4.png" alt="UMONS Université de Mons" />
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  methods: {
    openApp() {
      // Navigation vers une autre page, à adapter selon votre routeur Vue.js
      this.$router.push("/dashboard");
    },
  },
};
</script>

<style scoped>
body {
  font-family: "Roboto", Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f3f4f6;
  color: #333;
}

header {
  background-color: #e74c3c;
  padding: 20px;
  text-align: center;
  border-bottom: 3px solid #c0392b;
  color: white;
}

nav {
  margin: 20px 0;
}

nav a {
  margin: 0 15px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  transition: color 0.3s;
}

nav a:hover {
  color: #ffc107;
}

.content {
  text-align: center;
  padding: 40px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin: 20px auto;
  max-width: 800px;
}

.search-icon {
  width: 60px;
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s;
  margin-top: 20px;
}

.search-icon:hover {
  transform: scale(1.1);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

footer {
  background-color: #f8f8f8;
  padding: 20px;
  text-align: center;
  border-top: 2px solid #e7e7e7;
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.logo img {
  width: 130px;
  height: 80px;
  object-fit: contain;
  margin: 0 15px;
  transition: transform 0.3s, opacity 0.3s;
}

.logo img:hover {
  transform: scale(1.1);
  opacity: 0.9;
}

h2 {
  color: #444;
  font-size: 1.8em;
  margin-bottom: 15px;
}

.content p {
  font-size: 1.2em;
  line-height: 1.6;
  text-align: justify;
  color: #555;
}
</style>
