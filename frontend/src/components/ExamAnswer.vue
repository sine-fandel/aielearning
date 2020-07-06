<template>
<div>
  <div>current time is : {{ cur_time }}</div>
  <div>{{ left_time }} minutes left</div>
  <span class="question-title">{{ this.exam_content[current_page - 1].question_title }}</span>
  <el-input 
    v-if="this.question_len[current_page - 1].length === 1"
    type="textarea"
    class="ps-ans-input"
    v-model="ans_list[current_page - 1]">
  </el-input>
  <div v-if="this.question_len[current_page - 1].length === 5" class="mcq-ans-input">
    <el-radio v-model="ans_list[current_page - 1]" label="A" border>A.{{ this.exam_content[current_page - 1].option_a }}</el-radio>
    <el-radio v-model="ans_list[current_page - 1]" label="B" border>B.{{ this.exam_content[current_page - 1].option_b }}</el-radio>
    <el-radio v-model="ans_list[current_page - 1]" label="C" border>C.{{ this.exam_content[current_page - 1].option_c }}</el-radio>
    <el-radio v-model="ans_list[current_page - 1]" label="D" border>D.{{ this.exam_content[current_page - 1].option_d }}</el-radio>
  </div>
  <el-button v-if="current_page === this.exam_content.length" class="submit-btn" type="success" @click="submit ()">submit</el-button>
  <el-pagination
    background
    layout="prev, pager, next"
    @current-change="handleCurrentChange"
    :current-page="current_page"
    :page-size=1
    :total=exam_content.length
    class="pagination">
  </el-pagination>
</div>
</template>

<script>

export default {
  name: "ExamAnswer",
  props: ['which_to_show'],
  data () {
    return {
      exam_content: [{"question_title": "1+1="}, {"question_title": "2+2="}],
      question_len: [["question_title"]],
      current_page: 1,
      ans_list: [],
      cur_time: 0,
      left_time: 0,
      start_time: '',
      end_time: '',
    }
  },
  mounted () {
    setInterval (() => {
      this.cur_time = new Date ();
      let end = new Date (this.end_time) / 1000;
      // console.log (end);
      let left_second = parseInt (end) - parseInt (this.cur_time.getTime () / 1000);
      this.left_time = parseInt (left_second / 60);
      if (parseInt (end) <= parseInt (this.cur_time.getTime () / 1000)) {
        this.submit ();
      }
    });
    this.xml_to_json ();

  },
  methods: {
    handleCurrentChange (val) {
      this.current_page = val;
    },
    // submit () {
    //   this.$confirm ("Are you sure to submit this exam ?", "NOTE", {
    //     confirmButtonText: 'Yes',
    //     cancelButtonText: 'cancel',
    //     type: 'warning'
    //   }).then (() => {
    //     this.$emit ("reset", "");
    //     console.log (this.ans_list);
    //     this.$message ({
    //       type: 'success',
    //       message: 'submit successfully !'
    //     });
    //   }).catch (() => {
    //     this.$message({
    //       type: 'info',
    //       message: 'canceled the submit'
    //     });
    //   })
    // },
    xml_to_json () {
      // let xml = '<?xml version="1.0" encoding="utf-8"?><exam><start_time>2020-07-04T16:00:00.000Z</start_time><end_time>2020-07-04T18:00:00.000Z</end_time><exam_questions><question_content><question_title>22+2=</question_title></question_content><question_content><question_title>I have ten apple and you have six apple. What\'s the mount of the apple of us?</question_title></question_content><question_content><question_title>33 + 22=</question_title></question_content><question_content><question_title>22 * 3</question_title></question_content><question_content><question_title>2*2=</question_title><option_a>4</option_a><option_b>1</option_b><option_c>3</option_c><option_d>2</option_d></question_content><question_content><question_title>two plus four equal to ?</question_title><option_a>3</option_a><option_b>4</option_b><option_c>5</option_c><option_d>6</option_d></question_content><question_content><question_title>6*6=</question_title><option_a>22</option_a><option_b>36</option_b><option_c>12</option_c><option_d>34</option_d></question_content><question_content><question_title>1+1=</question_title><option_a>2</option_a><option_b>3</option_b><option_c>33</option_c><option_d>4</option_d></question_content></exam_question></exam>';
      let json = this.$parent.exam_json;
      // let json = this.$x2js.xml2js (xml);
      let exam = json['exam'];
      this.start_time = exam['start_time'];
      this.end_time = exam['end_time'];
      console
      for (let i = 0; i < exam['exam_questions']['question_content'].length; i ++) {
        this.exam_content[i] = exam['exam_questions']['question_content'][i];
        this.question_len[i] = Object.keys (this.exam_content[i]);
      }
      // console.log (this.exam_content);
    }
  }
}
</script>

<style lang="scss" scoped>
.question-title {
  position: absolute;
  width: 400px;
  top: 200px;
  left: 250px;
  font-size: 20px;
}
.ps-ans-input {
  position: absolute;
  width: 800px;
  top: 300px;
  left: 320px;
}
.mcq-ans-input {
  position: absolute;
  top: 300px;
  left: 320px;
}
.submit-btn {
  position: absolute;
  left: 1300px;
}

</style>