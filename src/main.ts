import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // Importation du routeur

// Création de l'application Vue avec le routeur
createApp(App).use(router).mount("#app");
