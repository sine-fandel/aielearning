<template>
<div>
  <NavMenu></NavMenu>
  <div class="wrapper" style="margin-top: 60px;">
    <el-steps :active="active" align-center>
      <el-step title="Step 1" description="select subject"></el-step>
      <el-step title="Step 2" description="question information"></el-step>
      <el-step title="Step 3" description="question description"></el-step>
      <el-step title="Step 4" description="finished"></el-step>
    </el-steps>
    <div v-if="active == 1">
      <p class="title">Select subject</p>
      <el-select class="step-1" v-model="subject" clearable placeholder="Select subject">
        <el-option
          v-for="item in options_sub"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div v-if="active == 2">
      <p class="title">Question information</p>
      <el-select class="step-2" v-model="type" clearable placeholder="Select the question type">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-select class="step-2-1" v-model="diffculty" clearable placeholder="Select question diffculty">
        <el-option
          v-for="item in options_dif"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-select class="step-2-2" v-model="grade" clearable placeholder="Select grade">
        <el-option
          v-for="item in options_grade"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-select class="step-2-3" v-model="kk" multiple filterable allow-create default-first-option placeholder="Select key knowledge">
        <el-option
          v-for="item in key_knowledge"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div v-if="active == 3 && type == 'MCQ'">
      <p class="title">multiple choice question</p>
      <Fileupload class="upload-photo" msg="upload photo" tip="JPG/PNG only"></Fileupload>
      <Fileupload class="upload-word" msg="upload file" tip="WORD only"></Fileupload>
      <Mcqdescript ref="child" v-on:activeChange="activeChange ()" v-blind:active="active" class="upload-mcqquetion"></Mcqdescript>
    </div>
    <div v-if="active == 3 && type == 'problem solving'">
      <p class="title">problem solving</p>
      <input @change="uploadPhoto($event)" type="file" id="file" class="photo-file">
      <label for="file">Upload Photo</label>
      <input type="file" id="file" class="word-file">
      <label for="file">Upload WORD</label>
      <Psdescript ref="child" v-on:activeChange="activeChange ()" v-blind:active="active" class="upload-wquestion"></Psdescript>
    </div>
    <div v-if="active == 4">
      <p class="title">Finished</p>
    </div>
  </div>
  <div class="btn">
    <el-button class="btn-last" @click="step (0)" :disabled="active == 1" type="primary" icon="el-icon-arrow-left">last step</el-button>
    <el-button class="btn-next" @click="step (1)" :disabled="active == 4" type="primary">next step<i class="el-icon-arrow-right el-icon--right"></i></el-button>
  </div>
</div>
</template>

<script>
// import Footer from "../components/Footer"
import Fileupload from "../components/Fileupload"
import Psdescript from "../components/Psdescript"
import Mcqdescript from "../components/Mcqdescript"
import NavMenu from "../components/NavMenu"

export default {
  name: "Upload",
  data () {
    return {
      active : 1,
      options_dif: [{
        value: "easy",
        label: "easy"
      }, {
        value: "hard",
        label: "hard"
      }, {
        value: "normal",
        label: "normal"
      }],
      options_sub: [{
        value: "maths",
        label: 'maths'
      }, {
        value: "English",
        label: "English"
      }],
      options_grade: [{
          value: "first grade",
          label: "first grade"
        }, {
          value: "second grade",
          label: "second grade"
        }, {
          value: "third grade",
          label: "third grade"
      }],
      key_knowledge: [{
        value: "add and subtract",
        label: "add and subtract"
      }, {
        value: "multiply and divide",
        label: "multiply and divide"
      }],
      options: [{
        value: "MCQ",
        label: "multiple choice question"
      }, {
        value: "problem solving",
        label: "problem solving"
      }],
      type: '',
      subject: '',
      diffculty: '',
      grade: '',
      photolist: '',
      kk: [],
      wruleForm: {
        labelPosition: "top"
      }
    };
  },
  methods: {
    step (lon) {
      if (lon == 1) {
        if (this.active == 1) {
          if (this.subject == '') {
            this.$message ({
              type: 'error',
              message: 'Please select the subject'
            })
          }
          else {
            this.active ++;
          }
        }
        if (this.active == 2) {
          if (this.type == '') {
            this.$message ({
              type: 'error',
              message: 'Please select the question type'
            })
          }
          else {
            this.active ++;
          }
        }
        if (this.active == 3 && this.type == 'problem solving') {
          this.$refs.child.handleNextbtn ()
        }
        if (this.active == 3 && this.type == 'MCQ') {
          this.$refs.child.handleNextbtn ()
        }
      }
      else {
        if (this.active > 1) {
          this.active --;
        }
      }
    },
    uploadPhoto (e) {
        var file = e.target.files[0];
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function() {
          console.log (reader.result);
        }
    },
    activeChange () {
      this.active = 4;
    }
  },
  components : {
    // Footer,
    Fileupload,
    Psdescript,
    Mcqdescript,
    NavMenu
  }
}
</script>

<style lang="scss" scoped>
.title {
  position: absolute;
  left: 200px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 30px;
}
.input-photo, .input-file {
  width: 330px;
  margin-top: 80px;
}
.input-photo {
  margin-right: 150px;
}
.input-file {
  margin-left: 50px;
}
.input-des {
  width: 850px;
}
.el-form-item__label {
  text-align: right;
  height: 30px;
  margin-right: 720px;
}

.btn {
  display: block;
  width: 100%;
  margin-top: 580px;
}
.btn-next {
  margin-left: 400px;
}
.btn-last {
  margin-right: 400px;
}

.step-1 {
  position: absolute;
  width: 300px;
  top: 350px;
  left: 480px;
}
.step-2 {
  position: absolute;
  width: 300px;
  top: 320px;
  left: 480px;
}
.step-2-1 {
  position: absolute;
  width: 300px;
  top: 390px;
  left: 480px;
}
.step-2-2 {
  position: absolute;
  width: 300px;
  top: 460px;
  left: 480px;
}
.step-2-3 {
  position: absolute;
  width: 300px;
  top: 530px;
  left: 480px;
}

.upload-photo {
  position: absolute;
  left: 260px;
  top: 210px;
}
.upload-word {
  position: absolute;
  left: 760px;
  top: 210px;
}
.upload-wquestion, .upload-mcqquetion {
  position: absolute;
  margin-top: 50px;
  left: 260px;
  top: 260px;
}


// upload photo button
.photo-file {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}
.photo-file + label {
    position: absolute;
    left: 260px;
    top: 210px;
    border-radius:0.3em;
    font-size: 14px;
    width: 260px;
    height: 28px;
    border-color: #909399;
    color: #FFF;
    background-color:#909399;
    display: inline-block;
}
.photo-file:focus + label,
.photo-file + label:hover {
    background-color: #a6a9ad;
}
.photo-file + label {
  cursor: pointer; /* 小手光标*/
}

// upload word button
.word-file {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}
.word-file + label {
    position: absolute;
    left: 760px;
    top: 210px;
    border-radius:0.3em;
    font-size: 14px;
    width: 260px;
    height: 28px;
    border-color: #909399;
    color: #FFF;
    background-color:#909399;
    display: inline-block;
}
.word-file:focus + label,
.word-file + label:hover {
    background-color: #a6a9ad;
}
.word-file + label {
  cursor: pointer; /* 小手光标*/
}

</style>