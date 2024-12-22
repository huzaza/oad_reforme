<template>
  <div class="customization-view">
    <header>
      <h1>Personnalisation de l'analyse</h1>
    </header>
    <form @submit.prevent="submitCustomization">
      <div class="form-group" v-for="(parameter, index) in parameters" :key="index">
        <input type="checkbox" v-model="selectedParameters" :value="parameter.value" />
        <label>{{ parameter.label }}</label>
      </div>
      <button type="submit">Analyser</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// Liste des paramètres disponibles
const parameters = [
  { label: "Propriétés pour la fabrication du fromage", value: "cheese_making" },
  { label: "Minéraux", value: "minerals" },
  { label: "Bilan énergétique", value: "energy_balance" },
  { label: "Infections", value: "infections" },
  { label: "Production de méthane", value: "methane_production" },
];

const selectedParameters = ref<string[]>([]);

// Fonction pour envoyer les paramètres sélectionnés à l'API
async function submitCustomization() {
  try {
    const response = await fetch("/api/customize_analysis", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ parameters: selectedParameters.value }),
    });

    if (response.ok) {
      const data = await response.json();
      router.push({ name: "Results", state: { results: data } });
    } else {
      console.error("Erreur lors de l'analyse personnalisée.");
    }
  } catch (error) {
    console.error("Erreur :", error);
  }
}
</script>

<style scoped>
header {
  background-color: #e53935;
  color: white;
  text-align: center;
  padding: 20px;
}

form {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 500px;
  margin: 20px auto;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

input[type="checkbox"] {
  margin-right: 10px;
}

button {
  background-color: #e53935;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

button:hover {
  background-color: #b71c1c;
}
</style>
