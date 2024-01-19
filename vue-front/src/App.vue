<template>
  <router-view> </router-view>
</template>

<script setup>
import { Options, Vue } from "vue-class-component";
import { ref, watch, onMounted } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();

function judageRoute() {
  const currRouter = router.currentRoute.value.path;
  const token = localStorage.getItem("token");
  if (token) {
    return;
  } else if (currRouter !== "/login") {
    router.push("/login");
  }
}

onMounted(() => {
  judageRoute();
});

// 监听
watch(
  () => router.currentRoute.value.path,
  (n, o) => {
    judageRoute();
  }
);
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  margin: 0px;
}
</style>
