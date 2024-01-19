<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="desc">{{ info }}</div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
const msg = ref("OCR 敏感词检测系统");
const info = ref(
  "系统专注于图片OCR 文本识别和敏感词检测。我们的系统采用领先的技术，能够快速、准确地识别图片中的文本，并对其进行高效的敏感词检测，以保护用户的合法权益。"
);
</script>

<style scoped>
.hello {
  padding: 10%;
  height: 500px;
  background-image: url("./../assets/bg.png");

  background-image: linear-gradient(
      rgba(255, 255, 255, 0.7),
      rgba(255, 255, 255, 0.3)
    ),
    url("./../assets/bg.png");
}

.desc {
  line-height: 30px;
  padding: 120px;
  padding-top: 20px;
}
</style>
