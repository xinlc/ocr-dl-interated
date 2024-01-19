import axios from "axios";
import { ElMessage } from "element-plus";

import router from "@/router";
import { ElLoading } from "element-plus";

export async function fetch(options) {
  console.log("optionsi ", options);
  const loading = ElLoading.service({
    lock: true,
    text: "加载中",
    background: "rgba(0, 0, 0, 0.3)",
  });

  const instance = await axios.create({
    timeout: 1000 * 60, // 超时  (设定请求时长 60s)
    headers: {
      token: localStorage.getItem("token"),
    },
  });
  try {
    const result = await instance(options);
    console.log("result is", result);
    loading.close();
    if (result.status === 200) {
      return result.data || {};
    }
    return null;
  } catch (error) {
    const { response } = error;
    loading.close();
    console.log("result is", response);
    if (response.status === 401 && router.currentRoute !== "/login") {
      ElMessage.error(response.data.message);
      localStorage.clear();
      router.push("/login");
      return;
    }

    if (response.status === 401 && router.currentRoute === "/login") {
      localStorage.clear();
      return;
    }

    if (response.data.message) {
      ElMessage.error(response.data.message);
      return null;
    }
    if (response.data.statusText) {
      ElMessage.error(response.data.statusText);
      return null;
    }
    if (response.data) {
      if (response.data.includes("Proxy error: Could not proxy request")) {
        ElMessage.error("服务异常，请重新尝试");
        return null;
      }
      ElMessage.error(response.data);
      return null;
    }
    return null;
  }
}
