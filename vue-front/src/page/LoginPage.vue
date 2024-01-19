<template>
  <div class="item-div">
    <div class="login-form">
      <h1>{{ dynamicValidateForm.adminName }}</h1>
      <el-tabs
        v-model="dynamicValidateForm.activeName"
        class="demo-tabs"
        @tab-click="handleClick"
      >
        <el-tab-pane label="登录" name="first"> </el-tab-pane>
        <el-tab-pane label="注册" name="second"></el-tab-pane>
      </el-tabs>
      <el-form
        :label-position="'left'"
        :label-width="
          dynamicValidateForm.activeName === 'first' ? '40px' : '70px'
        "
        ref="formRef"
        class="demo-dynamic"
      >
        <el-form-item label="账号">
          <el-input v-model="dynamicValidateForm.userName" />
        </el-form-item>

        <el-form-item label="密码">
          <el-input v-model="dynamicValidateForm.password" type="password" />
        </el-form-item>
        <el-form-item
          label="密码确认"
          v-if="dynamicValidateForm.activeName === 'second'"
        >
          <el-input
            v-model="dynamicValidateForm.confirm_password"
            type="password"
          />
        </el-form-item>
      </el-form>
      <el-button
        type="primary"
        class="btn"
        @click="submitForm()"
        v-if="dynamicValidateForm.activeName === 'first'"
        >登录</el-button
      >
      <el-button
        type="primary"
        class="btn"
        @click="submitRegisterForm()"
        v-if="dynamicValidateForm.activeName === 'second'"
        >注册</el-button
      >
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue";
import { ElMessage } from "element-plus";
import { _login, _register } from "@/api/api.js";

import { useRouter } from "vue-router";
const router = useRouter();
const formRef = ref(null);
const dynamicValidateForm = ref({
  adminName: "账号登录",
  email: "",
  userName: "",
  password: "",
  confirm_password: "",
  activeName: "first",
});

function handleClick() {
  if (dynamicValidateForm.value.activeName === "first") {
    dynamicValidateForm.value.adminName = "账号注册";
  } else {
    dynamicValidateForm.value.adminName = "账号登录";
  }

  console.log(
    dynamicValidateForm.value.activeName,
    dynamicValidateForm.value.adminName
  );
  dynamicValidateForm.value.userName = "";
  dynamicValidateForm.value.password = "";
  dynamicValidateForm.value.confirm_password = "";
}

function valid() {
  if (!dynamicValidateForm.value.userName) {
    ElMessage.warning("账号不能为空");
    return false;
  }

  if (
    dynamicValidateForm.value.password !==
    dynamicValidateForm.value.confirm_password
  ) {
    ElMessage.warning("两次密码不一致");
    return false;
  }
  return true;
}

async function submitRegisterForm() {
  if (valid()) {
    const result = await _register({
      username: dynamicValidateForm.value.userName,
      confirm_password: dynamicValidateForm.value.confirm_password,
    });
    if (result) {
      ElMessage.success("注册成功");
      dynamicValidateForm.value.activeName = "first";
      dynamicValidateForm.value.adminName = "账号登录";
      dynamicValidateForm.value.userName = "";
      dynamicValidateForm.value.password = "";
      dynamicValidateForm.value.confirm_password = "";
    }
  }
}

async function submitForm() {
  console.log(
    "submit data is ",
    dynamicValidateForm.value.userName,
    dynamicValidateForm.value.password
  );
  const result = await _login({
    username: dynamicValidateForm.value.userName,
    password: dynamicValidateForm.value.password,
  });
  if (result) {
    ElMessage.success("登录成功");
    localStorage.setItem("token", result.token);
    router.push("/");
  }
}

onMounted(() => {
  console.log("mounted is -----------------------");
});
</script>

<style scoped>
.item-div {
  height: 100vh;

  /* 背景颜色 */
  background-image: url("./../assets/bg.png");

  background-image: linear-gradient(
      rgba(128, 128, 128, 0.6),
      rgba(128, 128, 128, 0.8)
    ),
    url("./../assets/bg.png");
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-form {
  width: 300px;
  padding: 50px;
  padding-left: 50px;
  padding-right: 50px;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.4);

  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1), 0 2px 2px rgba(0, 0, 0, 0.1),
    0 4px 4px rgba(0, 0, 0, 0.1);
}

.btn {
  width: 80%;
  font-size: 16px;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-left: 10px;
}
</style>
