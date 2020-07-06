<template>
<div>
  <el-header>
    <ExamMenu v-bind:which_to_show="which_to_show" v-on:changeMenu="change ($event)" v-on:to_answer="answer ($event)" v-on:get_exam_json="get_exam_json ($event)"></ExamMenu>
  </el-header>

  <component :is="which_to_show" v-bind:which_to_show="which_to_show" v-on:reset="resetM ($event)"></component>

</div>
</template>

<script>
import ExamMenu from "../components/ExamMenu"
import ExamGenerate from "../components/ExamGenerate"
import ExamAnswer from "../components/ExamAnswer"

export default {
  name: "Exam",
  data () {
    return {
      which_to_show: "",
      exam_json: '',
    }
  },
  methods: {
    change (msg) {
      this.which_to_show = msg;
    },
    resetM (msg) {
      this.which_to_show = msg;
    },
    answer (msg) {
      this.which_to_show = msg;
    },
    get_exam_json (msg) {
      this.exam_json = msg;
      console.log (this.exam_json); 
    }
  },
  components: {
    ExamMenu,
    ExamGenerate,
    ExamAnswer,
  }
}
</script>