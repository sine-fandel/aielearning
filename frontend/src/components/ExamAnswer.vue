<template>
<div>
  <div id="clock">
    <div class="date">{{ date }}</div>
    <div class="time">{{ time }}</div>
  </div>
  <!-- <div>{{ left_time }} minutes left</div> -->
  <!-- <h4>the number of questions is {{ exam_content.length }}</h4> -->
  <span class="question-title">{{ current_question }}. {{ this.exam_content[current_question - 1].question_title }}</span>
  <el-input 
    v-if="this.question_len[current_question - 1].length === 3"
    type="textarea"
    class="ps-ans-input"
    v-model="ans_list[current_question - 1]">
  </el-input>
  <div v-if="this.question_len[current_question - 1].length === 7" class="mcq-ans-input">
    <el-radio v-model="ans_list[current_question - 1]" label="A" style="width: 800px; margin: 10px;" border>A.{{ this.exam_content[current_question - 1].option_a }}</el-radio>
    <el-radio v-model="ans_list[current_question - 1]" label="B" style="width: 800px; margin: 10px;" border>B.{{ this.exam_content[current_question - 1].option_b }}</el-radio>
    <el-radio v-model="ans_list[current_question - 1]" label="C" style="width: 800px; margin: 10px;" border>C.{{ this.exam_content[current_question - 1].option_c }}</el-radio>
    <el-radio v-model="ans_list[current_question - 1]" label="D" style="width: 800px; margin: 10px;" border>D.{{ this.exam_content[current_question - 1].option_d }}</el-radio>
  </div>
  <div class="ans-btn">
    <el-button type="info" icon="el-icon-arrow-left" @click="page_control (0)" :disabled="current_question == 1" style="margin-right: 950px;" circle plain></el-button>
    <el-button type="info" icon="el-icon-arrow-right" @click="page_control (1)" circle plain></el-button>
  </div>
  <el-button type="danger" class="submit-btn" @click="submit ()">Submit ({{ left_time }} minutes)</el-button>
  <el-button type="primary" class="info-btn" @click="show_info ()">Exam Infomation</el-button>
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
      current_question: 1,
      ans_list: [],
      cur_time: 0,
      time: '',
      date: '',
      left_time: 0,
      start_time: '',
      end_time: '',
    }
  },
  mounted () {
    setInterval (() => {
      var week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
      var cd = new Date();
      this.time = this.zeroPadding(cd.getHours(), 2) + ':' + this.zeroPadding(cd.getMinutes(), 2) + ':' + this.zeroPadding(cd.getSeconds(), 2);
      this.date = this.zeroPadding(cd.getFullYear(), 4) + '-' + this.zeroPadding(cd.getMonth()+1, 2) + '-' + this.zeroPadding(cd.getDate(), 2) + ' ' + week[cd.getDay()];
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
    zeroPadding(num, digit) {
      var zero = '';
      for(var i = 0; i < digit; i++) {
          zero += '0';
      }
      return (zero + num).slice(-digit);
    },
    page_control (c) {
      if (c == 0) {
        this.current_question = this.current_question - 1;
      }
      else if (c == 1) {
        if (this.current_question == this.exam_content.length) {
          alert ("This is the last question");
        }
        else {
          this.current_question = this.current_question + 1;
        }
      }
    },
    submit () {
      this.$confirm ("Are you sure to submit this exam ?", "NOTE", {
        confirmButtonText: 'Yes',
        cancelButtonText: 'cancel',
        type: 'warning'
      }).then (() => {
        this.$emit ("reset", "");
        let count_cor = 0;
        let wrong_list = [];
        for (let i = 0; i < this.exam_content.length; i++) {
          if (this.exam_content[i].correct_answer === this.ans_list[i]) {
            count_cor ++;
          }
          else {
            wrong_list.push (this.exam_content[i].question_title);
          }
        }
        this.$notify({
          title: 'Success',
          message: "Your score is " + count_cor + ' out of ' + this.exam_content.length,
          offset: 100,
          type: 'success'
        });
      }).catch (() => {
        this.$message({
          type: 'info',
          message: 'canceled the submit'
        });
      })
    },
    show_info () {
      let ps_num = 0;
      let mcq_num = 0;
      for (let i = 0; i < this.exam_content.length; i ++) {
        if (this.question_len[i].length == 3) {
          ps_num = ps_num + 1;
        }
        else {
          mcq_num = mcq_num + 1;
        }
      }
      this.$confirm ("<h3>The number of questions : " + this.exam_content.length + "</h3>" + "<h3>Includes problem solving : " + ps_num + "</h3>" + "<h3>Includes Multiply choice question : " + mcq_num + "</h3>", 'Exam information', {
          confirmButtonText: 'OK',
          cancelButtonText: 'cancel',
          type: 'info',
          center: true,
          dangerouslyUseHTMLString: true
        });
    },
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
    }
  }
}
</script>

<style lang="scss" scoped>
#clock {
  font-family: 'Share Tech Mono', monospace;
  // color: #ffffff;
  text-align: center;
  position: absolute;
  left: 50%;
  top: 150px;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  // color: #daf6ff;
  text-shadow: 0 0 20px #759daa, 0 0 20px rgba(10, 175, 230, 0);
}
#clock .time {
  letter-spacing: 0.05em;
  font-size: 20px;
  padding: 5px 0;
}


.question-title {
  position: absolute;
  width: 800px;
  top: 200px;
  left: 350px;
  font-size: 20px;
  text-align: left;
  color: black;
}
.ps-ans-input {
  position: absolute;
  width: 800px;
  top: 300px;
  left: 320px;
}
.mcq-ans-input {
  position: absolute;
  width: 60%;
  top: 300px;
  right: 280px;
}

.ans-btn {
  margin-top: 300px;
}

.submit-btn {
  position: absolute;
  width: 350px;
  top: 700px;
  left: 740px;
}
.info-btn {
  position: absolute;
  width: 350px;
  top: 700px;
  left: 350px;
}

</style>