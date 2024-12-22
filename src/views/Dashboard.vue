<template>
  <div class="dashboard">
    <!-- En-tête -->
    <header>
      <h1>Tableau de bord de votre ferme</h1>
      <nav>
        <RouterLink to="/">Accueil</RouterLink>
        <RouterLink to="/alerts">Voir les alertes</RouterLink>
        <RouterLink to="/personnalisation">Personnaliser l'analyse</RouterLink>
      </nav>
    </header>

    <!-- Barre de recherche -->
    <div class="search-bar">
      <input
        type="text"
        v-model="farmId"
        placeholder="Entrez l'ID de votre ferme"
      />
      <button @click="searchFarm">Rechercher</button>
    </div>

    <!-- Contenu du tableau de bord -->
    <div v-if="loading" class="loading">Chargement...</div>
    <div v-else class="dashboard-content" v-if="farmData">
      <!-- Section Win/Lose -->
      <div class="chart">
        <h3>Win/Lose</h3>
        <canvas id="winLoseChart"></canvas>
      </div>

      <!-- Section Évolution de la lactation -->
      <div class="chart">
        <h3>Évolution de la lactation</h3>
        <canvas id="lactationChart"></canvas>
      </div>
    </div>

    <div v-else class="no-data">Aucune donnée trouvée pour cette ferme.</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const farmId = ref<string>(""); // ID de la ferme saisi par l'utilisateur
const farmData = ref<any>(null); // Données récupérées depuis l'API
const loading = ref<boolean>(false);
let winLoseChart: Chart | null = null;
let lactationChart: Chart | null = null;

// Fonction pour rechercher les données de la ferme
const searchFarm = async () => {
  if (!farmId.value) {
    alert("Veuillez entrer un ID de ferme valide.");
    return;
  }

  loading.value = true;
  farmData.value = null;

  try {
    const response = await fetch(`/api/dashboard/${farmId.value}`);
    if (response.ok) {
      farmData.value = await response.json();
      renderCharts();
    } else {
      console.error("Erreur lors de la récupération des données.");
    }
  } catch (error) {
    console.error("Erreur de recherche :", error);
  } finally {
    loading.value = false;
  }
};

// Fonction pour rendre les graphiques
const renderCharts = () => {
  const winLoseCtx = document.getElementById(
    "winLoseChart"
  ) as HTMLCanvasElement;
  const lactationCtx = document.getElementById(
    "lactationChart"
  ) as HTMLCanvasElement;

  // Détruire les graphiques existants pour éviter les duplications
  if (winLoseChart) winLoseChart.destroy();
  if (lactationChart) lactationChart.destroy();

  // Win/Lose Chart
  winLoseChart = new Chart(winLoseCtx, {
    type: "pie",
    data: {
      labels: ["Win", "Lose"],
      datasets: [
        {
          data: farmData.value.winLose,
          backgroundColor: ["#4CAF50", "#E53935"],
          borderColor: ["#388E3C", "#C62828"],
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: "top" },
        title: { display: true, text: "Répartition Win/Lose" },
      },
    },
  });

  // Lactation Evolution Chart
  lactationChart = new Chart(lactationCtx, {
    type: "line",
    data: {
      labels: farmData.value.lactation.dates,
      datasets: [
        {
          label: "Évolution de la lactation",
          data: farmData.value.lactation.values,
          backgroundColor: "rgba(54, 162, 235, 0.2)",
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        title: { display: true, text: "Évolution de la lactation" },
      },
    },
  });
};
</script>

<style scoped>
/* En-tête */
header {
  background-color: #e74c3c;
  padding: 20px;
  text-align: center;
  color: white;
}

nav a {
  margin-right: 15px;
  color: white;
  text-decoration: none;
}

.search-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin: 20px;
}

input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

button {
  padding: 10px 15px;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #c0392b;
}

.dashboard-content {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.chart {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 45%;
}

.loading,
.no-data {
  text-align: center;
  font-size: 1.2em;
  margin: 20px;
  color: #666;
}
</style>
