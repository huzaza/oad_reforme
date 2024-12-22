<template>
  <div class="animal-profile">
    <header>
      <h1>Profil de l'animal</h1>
    </header>

    <!-- Conteneur pour le graphique radar -->
    <div class="chart-container">
      <canvas id="radarChart"></canvas>
    </div>

    <!-- Deux tableaux pour afficher les Top 10 CL Max et Min -->
    <div class="table-container">
      <div>
        <h3>Top 10 CL Max</h3>
        <table class="table">
          <thead>
            <tr>
              <th>Animal</th>
              <th>Index de lactation</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in top10Max" :key="index">
              <td>
                <a href="#" @click.prevent="fetchAnimalData(item.ID_ANIMAL)">
                  {{ item.ID_ANIMAL }}
                </a>
              </td>
              <td>{{ item.CL }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div>
        <h3>Top 10 CL Min</h3>
        <table class="table">
          <thead>
            <tr>
              <th>Animal</th>
              <th>Index de lactation</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in top10Min" :key="index">
              <td>
                <a href="#" @click.prevent="fetchAnimalData(item.ID_ANIMAL)">
                  {{ item.ID_ANIMAL }}
                </a>
              </td>
              <td>{{ item.CL }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

// Données réactives pour les tableaux et le graphique
const top10Max = ref([]);
const top10Min = ref([]);
const radarChart = ref<Chart | null>(null);

// Fonction pour récupérer les données Top 10 depuis l'API
async function fetchTop10Data() {
  try {
    const response = await fetch("/api/top10_cl");
    const data = await response.json();
    top10Max.value = data.top10Max;
    top10Min.value = data.top10Min;
  } catch (error) {
    console.error("Erreur lors du chargement des Top 10 :", error);
  }
}

// Fonction pour récupérer les données d'un animal et les afficher dans le graphique radar
async function fetchAnimalData(idAnimal: string) {
  try {
    const response = await fetch(`/api/animal_data/${idAnimal}`);
    const data = await response.json();

    // Ajouter les nouvelles données dans le graphique radar
    radarChart.value?.data.datasets.push({
      label: `Performances de l'animal ${idAnimal}`,
      data: data.animal_data,
      backgroundColor: "rgba(54, 162, 235, 0.2)",
      borderColor: "rgba(54, 162, 235, 1)",
      borderWidth: 2,
    });
    radarChart.value?.update();
  } catch (error) {
    console.error("Erreur lors du chargement des données de l'animal :", error);
  }
}

// Initialiser le graphique radar et charger les Top 10
onMounted(async () => {
  const ctx = document.getElementById("radarChart") as HTMLCanvasElement;
  radarChart.value = new Chart(ctx, {
    type: "radar",
    data: {
      labels: ["Quantité de lait", "Matières grasses", "Protéines", "Cellules somatiques"],
      datasets: [],
    },
    options: {
      responsive: true,
      scales: { r: { beginAtZero: true } },
    },
  });

  // Charger les données Top 10
  await fetchTop10Data();
});
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 500px;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.table-container {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-top: 20px;
}

.table {
  width: 48%;
  background-color: white;
  border-collapse: collapse;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.table th, .table td {
  padding: 15px;
  text-align: left;
}

.table th {
  background-color: #e53935;
  color: white;
}

.table tr:hover {
  background-color: #f1f1f1;
}

a {
  color: #007bff;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
  color: #0056b3;
}
</style>
