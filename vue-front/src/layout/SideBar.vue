<template>
  <aside class="site-sidebar">
    <div class="site-sidebar__inner">
      <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"
        default-active="1"
        text-color="#fff"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-menu-item index="1" @click="$router.push({ path: '/' })">
          <el-icon><location /></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-sub-menu index="2">
          <template #title>
            <el-icon><icon-menu /></el-icon>
            <span>DL模型</span>
          </template>
          <el-menu-item
            index="2-1"
            @click="$router.push({ path: '/paddle-ocr' })"
          >
            <span>OCR 识别</span>
          </el-menu-item>
          <el-menu-item
            index="2-1"
            @click="$router.push({ path: '/ocr-records' })"
          >
            <span>识别记录</span>
          </el-menu-item>
        </el-sub-menu>
      </el-menu>
    </div>
  </aside>
</template>
<script lang="ts" setup>
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from "@element-plus/icons-vue";
const handleOpen = (key: string, keyPath: string[]) => {};
const handleClose = (key: string, keyPath: string[]) => {};
</script>

<style scoped>
.site-sidebar {
  position: fixed;
  top: 0px;
  left: 0;
  bottom: 0;
  z-index: 1020;
  width: 230px;
  overflow: hidden;
  background-color: #545c64;
}
.site-sidebar__inner {
  height: 100%;
  padding-bottom: 15px;
  overflow-y: scroll;
}
</style>
