<template>
<div>
  <el-menu :default-active="activeIndex" class="menu-top" mode="horizontal">
    <el-menu-item index="1" v-on:click="change (1)">
      <el-input class="search-exam-input" v-model="exam_code" placeholder="Input a exam code here" maxLength="6"></el-input>
      <el-button class="search-exam-btn"  @click="search ()"></el-button>
    </el-menu-item>
    <el-menu-item index="2" v-on:click="change (2)">generate exam</el-menu-item>
  </el-menu>
</div>
</template>

<script>
import axios from "axios"

export default {
  name: "ExamMenu",
  props: ['which_to_show'],
  data () {
    return {
      activeIndex: 1,
      exam_code: null,
    }
  },
  methods: {
    change (which) {
      if (which == 1) {
        this.$emit ("changeMenu", "");
      }
      else {
        this.$emit ("changeMenu", "ExamGenerate");
      }
    },
    search () {
      var post_url = "http://fangzx.pythonanywhere.com/api/search_examapi";
      var config = {  headers: {'Content-Type': 'text/xml'} };

      axios.post (post_url, this.exam_code, config).then (response => {
        if (response.data.msg == "success") {
          
          let exam_json = this.$x2js.xml2js (response.data.exam_content);
          let start = new Date (exam_json['exam']['start_time']);
          let end = new Date (exam_json['exam']['end_time']);
          let cur = new Date ();
          if (end < cur) {
            alert ("The exam is over");
          }
          else if (start > cur) {
            alert ("The exam is not begin");
          }
          // let content_xml = response.data.exam_content;
          else {
            this.$emit ("to_answer", "ExamAnswer");
            this.$emit ("get_exam_json", exam_json);
          }
          
        }
        else {
          alert (response.data.msg);
        }
      }).catch (error => {
        console.log (error);
        alert (error);
      })

    }
  }
}
</script>

<style lang="scss">
.search-exam-input {
  width: 200px;
}
.search-exam-btn {
  margin-top: 1px;
  height: 39px;
  width: 30px;
  background-image: url("http://www.shejiye.com/uploadfile/icon/2017/0203/shejiyeiconkn52tp3dxt1.png");
  background-size: 30px 30px;
  background-repeat: no-repeat;
  background-position: 50% 50%;
}

</style>