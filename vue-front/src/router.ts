import { createRouter, createWebHashHistory } from "vue-router";
import * as VueRouter from "vue-router";

export const routess: VueRouter.RouteRecordRaw[] = [
  {
    path: "/",
    component: () => import("@/layout/MainContent.vue"),
    children: [
      {
        path: "/",
        component: () => import("@/components/HelloWorld.vue"),
      },
      {
        path: "/paddle-ocr",
        component: () => import("@/page/paddle/textOcrPage.vue"),
      },

      {
        path: "/html-editor",
        name: "HTML-EDITOR",
        component: () => import("@/page/editor/htmlEditor.vue"),
      },

      {
        path: "/ocr-records",
        name: "OCR_RECORDS",
        component: () => import("@/page/paddle/ocrRecord.vue"),
      },
    ],
  },
  {
    path: "/login",
    name: "LOHIN_PAGE",
    component: () => import("@/page/LoginPage.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes: routess,
});

export default router;
