<template>
  <div
    v-loading="loading"
    :element-loading-text="loadingText"
    element-loading-background="rgba(122, 122, 122, 0.8)"
  >
    <div class="h-class">
      <h1>OCR 识别敏感词检测</h1>
    </div>
    <div class="display-class">
      <div class="upload-img advance">
        <h2>上传图片</h2>
        <el-upload
          class="avatar-uploader"
          action="/api/paddleApp/upload-image"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" />
          <el-icon v-else class="avatar-uploader-icon"><Plus></Plus></el-icon>
        </el-upload>
      </div>
      <div class="upload-img" style="margin-left: 3rem; width: 50%">
        <h2>识别结果</h2>
        <span style="color: red; font-size: 0.8rem; margin-left: 1rem"
          >(敏感词由 * 代替)</span
        >

        <div class="text-direct">
          <div class="result-item">
            <span class="title"> 识别结果: </span>
            <span>
              {{ form.txt }}
            </span>
          </div>

          <div class="result-item">
            <span class="title"> 处理后结果: </span>
            <span>
              {{ form.after_txt }}
            </span>
          </div>
          <div class="result-item">
            <span class="title"> 是否含有敏感词: </span>
            <span style="font-weight: bold; color: red">
              {{ form.is_sen }}
            </span>
          </div>

          <div class="result-item">
            <span class="title"> 敏感词内容: </span>
            <span style="color: red">
              {{ form.sen_txt }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import type { UploadProps } from "element-plus";

const imageUrl = ref("");
const resultText = ref("");
const form = ref({
  is_sen: "",
  sen_txt: "",
  after_txt: "",
  txt: "",
});
const loading = ref(false);
const loadingText = ref("识别中，请耐心等待");

const handleAvatarSuccess: UploadProps["onSuccess"] = (
  response,
  uploadFile
) => {
  const resultData = response.data;
  resultText.value = resultData.result[0];
  form.value.after_txt = resultData.after_txt;
  form.value.is_sen = resultData.is_sen;
  form.value.sen_txt = resultData.sen_txt;
  form.value.txt = resultData.txt;

  imageUrl.value = URL.createObjectURL(uploadFile.raw!);
  loading.value = false;
};
const beforeAvatarUpload: UploadProps["beforeUpload"] = (rawFile) => {
  if (!(rawFile.type === "image/jpeg" || rawFile.type === "image/png")) {
    ElMessage.error("Avatar picture must be JPG format!");
    return false;
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error("Avatar picture size can not exceed 2MB!");
    return false;
  }
  loading.value = true;
  return true;
};
</script>

<style scoped>
.avatar-uploader {
  text-align: center;
  margin-top: 100px;
}
.avatar-uploader .avatar {
  width: 90%;
  height: auto;
  object-fit: cover;
  border-radius: 1rem;
}
</style>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}

.el-card {
  margin-top: 50px;
  height: 100%;
}

.el-card__header {
  font-weight: 600;
  font-size: 30px;
}
.img {
  width: 400px;
}

.h-class {
  text-align: left;
  margin: 1rem;
}
.h-class {
  margin-left: 2rem;
  padding-left: 1.5rem;
  font-size: 0.8rem;
  border-left: 5px solid red;
}

.display-class {
  margin-top: 4rem;
  align-items: start;
  padding-right: 2rem;
  display: flex;
}

.upload-img {
  margin-left: 1rem;
  border: 1px dashed gray;
  width: 40%;
  padding: 1rem;
  text-align: left;
  height: 500px;
  border-radius: 10px;
}

.advance {
  height: auto;
}

.upload-img h2 {
  border-left: 4px solid blue;
  padding-left: 2rem;
  margin-bottom: 1rem;
}

.result-item {
  text-align: left;
  padding-left: 1rem;
  padding-right: 1rem;
  margin-top: 0.4rem;
}

.result-item .title {
  font-weight: bold;
  margin-right: 20px;
}

.text-direct {
  height: 80%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
</style>
