<template>
  <div class="ocr-records">
    <el-table :data="table.data" style="width: 100%">
      <el-table-column prop="image" label="图片" align="center">
        <template #default="scope">
          <img
            class="table-class"
            :src="'data:image/png;base64,' + scope.row.image"
          />
        </template>
      </el-table-column>
      <el-table-column prop="text" label="文本" align="center">
        <template #default="scope">
          <div class="truncate">
            {{ scope.row.text }}
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="create_at" label="生成时间" align="center">
        <template #default="scope">
          {{ scope.row.create_at.replace("T", " ").replace("+08:00", "") }}
        </template>
      </el-table-column>
      <el-table-column prop="is_sen" label="是否含有敏感词" align="center">
        <template #default="scope">
          {{ scope.row.is_sen === "是" ? "是" : "否" }}
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template #default="scope">
          <a @click="viewItem(scope.row)" style="color: blue; cursor: pointer">
            查看</a
          >
          <a
            @click="deleteItem(scope.row.id)"
            style="color: blue; cursor: pointer; margin-left: 8x"
          >
            删除</a
          >
        </template>
      </el-table-column>
    </el-table>
    <div style="margin-top: 10px">
      <el-pagination
        v-model:current-page="table.pagination.page"
        v-model:page-size="table.pagination.pageSize"
        :page-sizes="[10, 20, 30, 40]"
        :small="false"
        :background="false"
        layout="total, sizes, prev, pager, next, jumper"
        :total="table.pagination.total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </div>
    <el-dialog
      v-model="table.form.visible"
      title="详情"
      width="60%"
      @close="closeData"
    >
      <div class="diag-con">
        <img :src="'data:image/png;base64,' + table.form.data.image" />

        <div>
          <span class="title">识别时间:</span>
          <span>{{ table.form.data.create_at }}</span>
        </div>

        <div>
          <span class="title">识别文本:</span>
          <span>{{ table.form.data.text }}</span>
        </div>

        <div>
          <span class="title">是否含有敏感词:</span>
          <span style="color: red; font-weight: bold; font-size: 18px">{{
            table.form.data.is_sen
          }}</span>
        </div>

        <div>
          <span class="title">处理后文本:</span>
          <span>{{ table.form.data.after_txt }}</span>
        </div>

        <div>
          <span class="title">敏感词汇:</span>
          <span style="color: red; font-size: 18px">{{
            table.form.data.sen_txt
          }}</span>
        </div>
      </div>
    </el-dialog>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue";
import { _queryOcrs, _deleteOcrRecord } from "@/api/api.js";
import { ElMessageBox } from "element-plus";
import { ElMessage } from "element-plus";

const table = ref({
  data: [],
  columns: [],
  pagination: {
    page: 1,
    limit: 5,
    totalPage: 0,
  },
  form: {
    data: {
      image: "",
      text: "",
      create_at: "",
      // 是否敏感词
      is_sen: "",
      // 敏感词
      sen_text: "",
      after_txt: "",
    },
    id: "",
    visible: false,
  },
});

async function queryList() {
  const result = await _queryOcrs({
    limit: table.value.pagination.limit,
    page: table.value.pagination.page,
  });
  if (result) {
    console.log("result is", result);
    table.value.pagination.total = result.totalPage;
    table.value.data = result.data;
  }
}

async function deleteItem(id) {
  ElMessageBox.confirm("确定要删除该记录么?", "警告", {
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(async () => {
      const result = await _deleteOcrRecord({ id: id });
      if (result) {
        ElMessage.success("删除成功");
        queryList();
      }
    })
    .catch(() => {
      ElMessage.success("删除失败");
    });
  console.log("delete");
}

function closeData() {
  table.value.form.data = {};
  table.value.form.id = "";
}

function handleSizeChange(number) {
  table.value.pagination.pageSize = number;
  queryList();
}

function handleCurrentChange(number) {
  table.value.pagination.page = number;
  queryList();
}

function viewItem(item) {
  table.value.form.data.is_sen = item.is_sen;
  table.value.form.data.sen_txt = item.sen_txt;
  table.value.form.data.after_txt = item.after_txt;
  table.value.form.data.create_at = item.create_at;
  table.value.form.data.image = item.image;
  table.value.form.data.id = item.id;
  table.value.form.data.text = item.text;
  console.log("form data is ", table.value.form.data);
  table.value.form.visible = true;
}

onMounted(() => {
  queryList();
});
</script>
<style scoped>
.table-class {
  width: 10em;
  border-radius: 0.5rem;
  height: auto;
  object-fit: cover;
}

.ocr-records {
  padding: 2rem;
}

.diag-con {
  border-top: 1px solid gray;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: auto;
  text-align: left;
  padding: 20px;
  padding-top: 10px;
}

.diag-con .title {
  font-weight: bold;
  font-size: 18px;
  margin-right: 40px;
}

.diag-con span {
  line-height: 25px;
}

.diag-con img {
  height: auto;
  width: 350px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 10px;
}

.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 200px; /* 假设容器宽度为 200px */
}

::ng-deep .el-overlay .el-overlay-dialog .el-dialog .el-dialog__body {
  padding-top: 0px;
}
</style>
