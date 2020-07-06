<template>
<div>
  <el-form class="des-el-form" :model="ruleForm" :rules="rules" ref="ruleForm" :label-position="labelPosition" label-width="80px" >
    <el-form-item label="question description" prop="des">
      <el-input type="textarea" class="des-el-input1" v-model="ruleForm.des"></el-input>
    </el-form-item>
    <div>
      <h1 class="opt-a">A</h1>
      <el-form-item prop="opta">
        <el-input class="opt-a-input" v-model="ruleForm.opta"></el-input>
      </el-form-item>
      <h1 class="opt-b">B</h1>
      <el-form-item prop="optb">
        <el-input class="opt-b-input" v-model="ruleForm.optb"></el-input>
      </el-form-item>
      <h1 class="opt-c">C</h1>
      <el-form-item prop="optc">
        <el-input class="opt-c-input" v-model="ruleForm.optc"></el-input>
      </el-form-item>
      <h1 class="opt-d">D</h1>
      <el-form-item prop="optd">
        <el-input class="opt-d-input" v-model="ruleForm.optd"></el-input>
      </el-form-item>
        <el-form-item class="el-label-ans1" label="answer" prop="ans">
        <!-- <el-input class="ans-el-input" v-model="ruleForm.ans"></el-input> -->
          <el-select v-model="ruleForm.ans" class="ans-el-input" placeholder="choose answer">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
      </el-form-item>
      <el-form-item class="el-label-note1" label="note" prop="note">
        <el-input type="textarea" class="note-el-input" v-model="ruleForm.note"></el-input>
      </el-form-item>
    </div>
  </el-form>
</div>
</template>

<script>
import axios from "axios"
export default {
  name: "Mcqdescript",
  props: {
    active: String,

  },
  data () {
    return {
      labelPosition: 'top',
      ruleForm: {
        des: '',
        opta: '',
        optb: '',
        optc: '',
        optd: '',
        ans: '',
        note: ''
      },
      options: [{
        value: "A",
        label: "A"
      }, {
        value: "B",
        label: "B"
      }, {
        value: "C",
        label: "C"
      }, {
        value: "D",
        label: "D"
      },],
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
        var diffculty = this.$parent.diffculty;
        var grade = this.$parent.grade;
        var key_knowledge = this.$parent.kk;
        this.createXML (subject, type, diffculty, grade, key_knowledge);
        this.$emit ('activeChange')
      }
    },
    createXML (subject, type, diffculty, grade, key_knowledge) {
      // var xml = '<?xml version="1.0" encoding="utf-8"?>' + '\n' +
      //           '<question>' + '\n' +
      //               '     <question_info>' + '\n' +
      //               '         <subject>' + subject + '</subject>' + '\n' +
      //               '         <type>' + type + '</type>' + '\n' +
      //               '         <diffculty>' + diffculty + '</diffculty>' + '\n' +
      //               '         <grade>' + grade + '</grade>' + '\n' +
      //               '         <key_knowledge>' + key_knowledge + '</key_knowledge>' + '\n' +
      //               '     </question_info>' + '\n' +
      //               '     <question_content>' + '\n' +
      //               '         <question_title>' + this.ruleForm.des + '</question_title>' + '\n' +
      //               '         <option_a>' + this.ruleForm.opta + '</option_a>' + '\n' +
      //               '         <option_b>' + this.ruleForm.optb + '</option_b>' + '\n' +
      //               '         <option_c>' + this.ruleForm.optc + '</option_c>' + '\n' +
      //               '         <option_d>' + this.ruleForm.optd + '</option_d>' + '\n' +
      //               '     </question_content>' + '\n' +
      //               '     <correct_answer>' + this.ruleForm.ans + '</correct_answer>' + '\n' +
      //               '     <explanation>' + this.ruleForm.note + '</explanation>' + '\n' +
      //           '</question>';
      var xml = '<?xml version="1.0" encoding="utf-8"?>' + '<question>' + '<question_info>' + '<subject>' + subject + '</subject>' + '<type>' + type + '</type>' + '<diffculty>' + diffculty + '</diffculty>' + '<grade>' + grade + '</grade>' + '<key_knowledge>' + key_knowledge + '</key_knowledge>' + '</question_info>' + '<question_content>' + '<question_title>' + this.ruleForm.des + '</question_title>' + '<option_a>' + this.ruleForm.opta + '</option_a>' + '<option_b>' + this.ruleForm.optb + '</option_b>' + '<option_c>' + this.ruleForm.optc + '</option_c>' + '<option_d>' + this.ruleForm.optd + '</option_d>' + '</question_content>' + '<correct_answer>' + this.ruleForm.ans + '</correct_answer>' + '<explanation>' + this.ruleForm.note + '</explanation>' + '\n' + '</question>';
      console.log (xml);
      var post_url = "https://fangzx.pythonanywhere.com/api/uploadApi";
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
.des-el-input1 {
  width: 800px;
}
.ans-el-input {
  width: 200px;
  margin-right: 600px;
  top: 5px;
}
.el-textarea__inner {
  height: 60px;
}
.el-form-item__label {
  height: 30px;
  margin-right: 660px;
}

.opt-a {
  position: absolute;
  margin-bottom: 5px;
  left: 10px;
}
.opt-b {
  width: 50px;
  position: absolute;
  margin-top: 20px;
  top: 115px;
  left: 390px;
}
.opt-c {
  width: 50px;
  position: absolute;
  top: 175px;
}
.opt-d {
  width: 50px;
  position: absolute;
  top: 175px;
  left: 390px;
}
.opt-a-input {
  position: absolute;
  width: 300px;
  top: 20px;
  left: 50px;
}
.opt-b-input {
  position: absolute;
  width: 300px;
  top: 2px;
  left: 450px;
}
.opt-c-input {
  position: absolute;
  width: 300px;
  top: 45px;
  left: 50px;
}
.opt-d-input {
  position: absolute;
  width: 300px;
  top: 25px;
  left: 450px;
}

.el-label-ans1 .el-form-item__label {
  margin-top: 50px;
  height: 30px;
  margin-right: 750px;
}
.el-label-note1 .el-form-item__label {
  height: 30px;
  margin-right: 770px;
}
</style>