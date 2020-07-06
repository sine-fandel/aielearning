<template>
<div>
  <el-select class="opt-grade" v-model="grade" clearable placeholder="Select grade">
    <el-option
      v-for="item in options_grade"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  <el-select class="opt-diff" v-model="difficulty" clearable placeholder="Select difficulty">
    <el-option
      v-for="item in options_diff"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  <el-select class="opt-kk" v-model="kk" clearable multiple placeholder="Select key knowledge">
    <el-option
      v-for="item in options_kk"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  <div class="date-time">
    <el-date-picker
      v-model="date"
      type="datetimerange"
      start-placeholder="start time"
      end-placeholder="end time">
    </el-date-picker>
  </div>
  <el-button type="success" class="submit-btn" @click="generate ()">submit</el-button>
  <!-- <label class="num-questions" for="num">number of questions</label> -->
  <!-- <el-input-number v-model="num" :step="1" size="medium" class="input-num"></el-input-number> -->
  <div  class="type-input" v-for="(type, index) in types" :key="index">
      <el-select class="opt-types" v-model="types[index]" clearable placeholder="Select question types">
        <el-option
          v-for="item in options_types"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-input-number style="width:100px" v-model="types_num[index]" :step="1" size="mini"></el-input-number>
  </div>
  <el-button type="primary" class="add-btn" icon="el-icon-plus" @click="add_type" circle></el-button>
  <el-button type="danger" class="del-btn" icon="el-icon-minus" @click="del_type (index)" circle></el-button>
</div>
</template>

<script>
import axios from "axios"

export default {
  name: "ExamGenerate",
  props: ['which_to_change'],
  data () {
    return {
      options_grade: [{
        value: 'first grade',
        label: 'first grade'
      }, {
        value: 'second grade',
        label: 'second grade'
      },],
      options_diff: [{
        value: 'easy',
        label: 'easy'
      }, {
        value: 'normal',
        label: 'normal'
      }, {
        value: 'hard',
        label: 'hard'
      }],
      options_types: [{
        value: 'problem solving',
        label: 'problem solving'
      }, {
        value: 'MCQ',
        label: 'multiple choice question'
      }, {
        value: 'calculation',
        label: 'calculation'
      }],
      options_kk: [{
        value: "Four Arithmetic Operations",
        label: "Four Arithmetic Operations"
      }, {
        value: "problem of geometry",
        label: "problem of geometry"
      }],
      grade: '',
      difficulty: '',
      types: [''],
      types_num: [],
      kk: [],
      date: '',
      num: 1,
    }
  },
  methods: {
    add_type () {
      this.types.push ('');
    },
    del_type () {
      if (this.types.length == 1) {
        alert ("cannot be remove anymore")
      }
      else  {
        this.types.pop ();
      }
    },
    generate () {
      // var xml = '<?xml version="1.0" encoding="utf-8"?>' + '\n' +
      //           '<exam_info>' + '\n' +
      //           '   <grade>' + this.grade + '</grade>' + '\n' +
      //           '   <diffculty>' + this.diffculty + '</diffculty>' + '\n' +
      //           '   <key_knowledge>' + this.kk + '</key_knowledge>' + '\n' +
      //           '   <date>' + this.date + "</date>" + '\n' +
      //           '   <types>' + this.types + '</types>' + '\n' +
      //           '   <types_num>' + this.types_num + "</types_num>" + '\n' +
      //           '</exam_info>';

      // console.log (xml);

      let json_str = {
        grade: this.grade,
        difficulty: this.difficulty,
        key_knowledge: this.kk,
        date: this.date,
        types: this.types,
        types_num: this.types_num
      }
      console.log (json_str);

      var config = {  headers: {'Content-Type': 'application/json'} };
      var upload_url = "http://fangzx.pythonanywhere.com/api/gen_examapi";
      axios.post (upload_url, json_str, config).then (response => {
        if (response.data.msg == "success") {
          this.$msgbox ({
            title: 'success',
            message: "The exam code you generated is " + response.data.code
          })
          this.$emit ("reset", "");
        }
      }).catch (error => {
        console.log (error);
        alert ("Wrong");
      })
    }
  },

}
</script>

<style lang="scss" scoped>
.title {
  position: absolute;
  left: 200px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 30px;
}

.opt-grade {
  position: absolute;
  width: 400px;
  top: 140px;
  left: 450px;
}
.opt-diff {
  position: absolute;
  width: 400px;
  top: 200px;
  left: 450px;
}
.opt-kk {
  position: absolute;
  width: 400px;
  top: 270px;
  left: 450px;
}
.date-time {
  position: absolute;
  width: 330px;
  top: 340px;
  left: 450px;
}
.num-questions {
  position: absolute;
  width: 400px;
  top: 400px;
  left: 360px;
}
.input-num {
  position: absolute;
  width: 330px;
  top: 420px;
  left: 480px;
}
.type-input {
  position: relative;
  width: 400px;
  top: 340px;
  left: 400px;
}

.add-btn {
  position: absolute;
  top: 430px;
  left: 800px;
}
.del-btn {
  position: absolute;
  top: 430px;
  left: 850px;
}
.submit-btn {
  position: absolute;
  left: 1200px;
}

</style>