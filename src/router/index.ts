import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import DashboardView from "@/views/Dashboard.vue";
import AlertsView from "@/views/Alerts.vue";
import CustomizationView from "@/views/Customization.vue";
import AnimalProfileView from "@/views/AnimalProfile.vue";
import ResultsView from "@/views/ResultsView.vue";
import Home from "@/views/Home.vue";


const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "About",
    component: AboutView,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: DashboardView,
  },
  {
    path: "/alerts",
    name: "Alerts",
    component: AlertsView,
  },
  {
    path: "/personnalisation",
    name: "Customization",
    component: CustomizationView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
