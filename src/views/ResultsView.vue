<template>
  <div class="results-view">
    <header>
      <h1>Résultats de l'analyse personnalisée</h1>
    </header>
    <div class="results-container">
      <div v-for="(item, index) in results" :key="index" class="result-table">
        <h3>{{ item.category }}</h3>
        <table>
          <thead>
            <tr>
              <th>ID Animal</th>
              <th v-for="col in item.columns" :key="col">{{ col }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in item.data" :key="row.ID_ANIMAL">
              <td>{{ row.ID_ANIMAL }}</td>
              <td v-for="col in item.columns" :key="col">{{ row[col] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const results = ref<any[]>([]);

// Récupération des données depuis l'état transmis ou via l'API
onMounted(async () => {
  const state = router.options.history.state;
  if (state && state.results) {
    results.value = state.results;
  } else {
    try {
      const response = await fetch("/api/results_analysis");
      if (response.ok) {
        results.value = await response.json();
      } else {
        console.error("Erreur lors de la récupération des résultats.");
      }
    } catch (error) {
      console.error("Erreur :", error);
    }
  }
});
</script>

<style scoped>
header {
  background-color: #e53935;
  color: white;
  text-align: center;
  padding: 20px;
}

.results-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 20px;
}

.result-table {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #e53935;
  color: white;
}

tr:hover {
  background-color: #f5f5f5;
}
</style>
