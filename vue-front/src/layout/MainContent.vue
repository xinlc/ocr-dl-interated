<template>
  <div>
    <side-bar> </side-bar>
    <div class="site-content__wrapper">
      <div class="head-bar">
        <div
          class="logo"
          @mouseenter="handleMouseEnter"
          @mouseleave="handleMouseLeave"
        >
          <img src="../assets/user.png" />
          <div class="hover-logo" v-if="isShow">
            <a @click="logout" style="width: 100px"> 退出登录</a>
          </div>
        </div>
      </div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup>
import SideBar from "./SideBar.vue";
import { ref } from "vue";
import { ElMessageBox } from "element-plus";
import { useRouter } from "vue-router";
const router = useRouter();

const isShow = ref(false);

function logout() {
  ElMessageBox.confirm("确定要退出登录么?", "警告", {
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(() => {
      localStorage.clear();
      router.push("/login");
    })
    .catch(() => {});
  console.log("logout");
}

function handleMouseEnter() {
  console.log("in enter ----------");
  console.log(isShow.value);
  isShow.value = true;
}

function handleMouseLeave() {
  isShow.value = false;
}
</script>

<style scoped>
.site-content__wrapper {
  margin-left: 230px;
}

.head-bar {
  height: 50px;

  display: flex;
  justify-content: flex-end;
  align-items: center;
  box-shadow: 0 0px 3px rgba(0, 0, 0, 0.3);
}

.head-bar div {
}

.logo {
  position: relative;
  margin-right: 1.5rem;
  border-radius: 1.2rem;
}
.logo img {
  width: 30px;
  height: 30px;
  object-fit: cover;
}

.hover-logo {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  right: -10px;
  box-shadow: 1px;

  position: absolute;
  /* background-color: white;  */
  padding: 0.4rem;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1), 0 2px 2px rgba(0, 0, 0, 0.1),
    0 4px 4px rgba(0, 0, 0, 0.1), 0 8px 8px rgba(0, 0, 0, 0.1),
    0 16px 16px rgba(0, 0, 0, 0.1);
}

.hover-logo a:hover {
  color: red;
}

.hover-logo:hover {
  background-color: rgba(0, 0, 0, 0.1);
}
</style>
