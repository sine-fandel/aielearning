<template>
<div>
  <el-form class="des-el-form" :model="ruleForm" :rules="rules" ref="ruleForm" :label-position="labelPosition" label-width="80px" >
    <el-form-item label="question description" prop="des">
      <el-input type="textarea" class="des-el-input" v-model="ruleForm.des"></el-input>
    </el-form-item>
    <el-form-item class="el-label-ans" label="answer" prop="ans">
      <el-input type="textarea" class="des-el-input" v-model="ruleForm.ans"></el-input>
    </el-form-item>
    <el-form-item class="el-label-note" label="note" prop="note">
      <el-input type="textarea" class="des-el-input" v-model="ruleForm.note"></el-input>
    </el-form-item>
  </el-form>
</div>
</template>

<script>
import axios from "axios"

export default {

  name: "Psdescript",
  props: {
    active: String,
  },
  data () {
    return {
      labelPosition: 'top',
      ruleForm: {
        des: '',
        ans: '',
        note: ''
      },
      rules: {
        des: [
          { required: true, message: 'question description cannot be empty', trigger: 'blur' }
        ],
        ans: [
          { required: true, message: 'answer cannot be empty', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleNextbtn () {// eslint-disable-line no-unused-vars
      if (this.ruleForm.des == '' || this.ruleForm.ans == '') {
        this.$message ({
          type: 'error',
          message: 'question description and answer cannot be empty'
        })
      }
      else {
        var subject = this.$parent.subject;
        var type = this.$parent.type;
        // var photo = this.$parent.;
        // console.log (photo);
        var diffculty = this.$parent.diffculty;
        var grade = this.$parent.grade;
        var key_knowledge = this.$parent.kk;
        this.postXML (subject, type, diffculty, grade, key_knowledge);
        this.$emit ('activeChange');
      }
    },
    postXML (subject, type, diffculty, grade, key_knowledge) {
      var xml = '<?xml version="1.0" encoding="utf-8"?>' + '<question>' + '<question_info>' + '<subject>' + subject + '</subject>' + '<type>' + type + '</type>' + '<diffculty>' + diffculty + '</diffculty>' + '<grade>' + grade + '</grade>' + '<key_knowledge>' + key_knowledge + '</key_knowledge>' + '</question_info>' + '<question_content>' + '<question_title>' + this.ruleForm.des + '</question_title>'  + '<correct_answer>' + this.ruleForm.ans + '</correct_answer>' + '<explanation>' + this.ruleForm.note + '</explanation>' + '</question_content>' + '</question>';

      console.log (xml);
      var post_url = "https://fangzx.pythonanywhere.com/api/uploadApi";
      // var post_url = "http://localhost:8000/api/uploadApi";
      var config = {  headers: {'Content-Type': 'text/xml'} };
      axios.post (post_url, xml, config).then (response => {
          console.log (response);
        }).catch (error => {
          console.log (error);
          alert (error);
        });
    }
  }
}
</script>

<style lang="scss">
.des-el-input {
  width: 800px;
}
.el-textarea__inner {
  height: 80px;
}
.el-form-item__label {
  height: 30px;
  margin-right: 660px;
}
.el-label-ans .el-form-item__label {
  height: 30px;
  margin-right: 750px;
}
.el-label-note .el-form-item__label {
  height: 30px;
  margin-right: 770px;
}
</style>