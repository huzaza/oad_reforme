<template>
  <div class="alerts">
    <header>
      <h1>Alertes pour votre ferme</h1>
    </header>

    <table class="alert-table">
      <thead>
        <tr>
          <th>Forte probabilité de rester dans le groupe élevé</th>
          <th>Forte probabilité d'aller dans le groupe élevé</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(alert, index) in alerts" :key="index">
          <td>{{ alert.stay }}</td>
          <td>{{ alert.move }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const alerts = ref([
  { stay: "ID_13522582", move: "ID_13611350" },
  { stay: "ID_13633199", move: "ID_13801550" },
]);
</script>

<style scoped>
header {
  background-color: #e74c3c;
  padding: 20px;
  text-align: center;
  color: white;
}

.alert-table {
  width: 80%;
  margin: 0 auto;
  border-collapse: collapse;
}

.alert-table th,
.alert-table td {
  padding: 15px;
  text-align: center;
  border: 1px solid #ddd;
}

.alert-table th {
  background-color: #4caf50;
  color: white;
}
</style>
