<template>
<div>
  <el-upload
    class=upload-photo
    action=""
    :on-preview="handlePreview"
    :on-remove="handleRemove"
    :before-remove="beforeRemove"
    multiple
    :limit='2'
    :on-exceed="handleExceed"
    :file-list="fileList">
    <el-button type="info">{{ msg }}</el-button>
    <div slot="tip" class="el-upload__tip">{{ tip }}</div>
  </el-upload>
</div>
</template>

<script>
export default {
  name: "Fileupload",
  props: {
    msg: String,
    tip: String
  },
  data () {
    return {
      fileList: []
    }
  },
  handlePreview (fileList) {
    console.log (fileList);
  }
}
</script>

<style lang="scss" scoped>
.el-button {
  width: 260px;
  height: 30px;
}
</style>
