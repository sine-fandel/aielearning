<template>
<div>
  <div class="wrapper">
    <div>
      <el-button type="text" @click="to_home ()">home</el-button>
    </div>
    <p class="title">Sign up</p>
    <!-- sinup form -->
    <el-form class="login-form" :model="ruleForm" :rules="rules" ref="ruleForm" :label-position="ruleForm.labelPosition" label-width="80px">
      <el-form-item class="el-label-name" label="email address" prop="name">
        <el-input v-model="ruleForm.name" clearable></el-input>
      </el-form-item>
      <el-form-item class="el-label-pwd" label="password" prop="pwd">
        <el-input v-model="ruleForm.pwd" show-password></el-input>
        <el-progress :percentage="passwordPercent" :format="passwordPercentFormat"></el-progress>
      </el-form-item>
      <el-form-item class="el-label-cpwd" label="comfrim password" prop="cpwd">
        <el-input v-model="ruleForm.cpwd" show-password></el-input>
      </el-form-item>
      <el-form-item class="el-label-username" label="username" prop="username">
        <el-input v-model="ruleForm.username" clearable></el-input>
      </el-form-item>
      <el-form-item class="el-label-date" label="birthday" prop="date">
        <el-date-picker
          v-model="ruleForm.date"
          type="date"
          placeholder="choose date">
        </el-date-picker>
      </el-form-item>
      <el-form-item class="el-label-identity" label="identity" prop="identity">
        <el-select v-model="ruleForm.identity" placeholder="select">
        <el-option
          v-for="item in ruleForm.options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option> 
      </el-select>
      </el-form-item>
      <!-- button -->
      <el-form-item class="btn-login">
        <el-button type="success" @click="log_in ()">Sign up</el-button>
      </el-form-item>
    </el-form>
    <label id="note">Already have an account ? <el-link type="primary" href="/login">login</el-link></label>
  </div>
  
  <router-views/>
</div>
</template>

<script>
// import Footer from '../components/Footer.vue'

export default {
  name: "Signup",
  data () {
    // validate the password
    var validatePassword = (rule, value, callback) => {
      var ls = 0;
      if (this.ruleForm.pwd !== '') {
        if (this.ruleForm.pwd.match (/([a-z])+/)) {
          ls ++;
        }
        if (this.ruleForm.pwd.match (/([0-9])+/)) {
          ls ++;
        }
        if (this.ruleForm.pwd.match (/([A-Z])+/)) {
          ls ++;
        }
        if (this.ruleForm.pwd.length > 8) {
          ls ++;
        }
      }
      switch (ls) {
        case 0: this.passwordPercent = 0; callback (); break;
        case 1: this.passwordPercent = 33; callback (); break;
        case 2: this.passwordPercent = 66; callback (); break;
        case 4: this.passwordPercent = 100; callback (); break;
      }
    };
    // check the password
    var checkPassword = (rule, value, callback) => {
      if (value != this.ruleForm.pwd) {
        callback (new Error ("The password is not the same as the first time input"))
      }
    };
    return {
      passwordPercent: 0,
      ruleForm: {
        labelPosition: 'top',
        name: '',
        pwd: '',
        cpwd: '',
        username: '',
        options: [{
          value: "op1",
          label: "Teacher"
        }, {
          value: "op2",
          label: "Student"
        }, {
          value: "op3",
          label: "Parent"
        }],
        identity: '',
        date: ''
      },
        rules: {
          name: [
            { required: true, message: "email cannot be empty", trigger: "blur" },
            { type: 'email', message: 'please input a real email', trigger: ['blur', 'change'] }
          ],
          pwd: [
            { required: true, message: "password cannot be empty", trigger: "blur" },
            { validator: validatePassword, trigger: ['blur', 'change'] }
          ],
          cpwd: [
            { required: true, message: "please confirm the password", trigger: "blur" },
            { validator: checkPassword, trigger: "blur" }
          ],
          username: [
            { required: true, message: "username cannot be empty", trigger: "blur" }
          ],
          date: [
            { required: true, message: "birthday cannot be empty", trigger: "blur" }
          ],
          identity: [
            { required: true, message: "please choose your identity", trigger: "blur" }
          ]
        }

    }
  }, 
  methods: {
    passwordPercentFormat (passwordPercent) {
      if (passwordPercent == 0) {
        return ''
      }
      else if (passwordPercent <= 33) {
        return 'weak'
      } 
      else if (passwordPercent == 66) {
        return 'security'
      }
      return 'strong'
    },
    to_home () {
      this.$router.push ('/')
    },
  },
  components: {
    // Footer
  }
}
</script>

<style lang="scss">
.wrapper {
  padding-bottom: 50px;
}
.title {
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 40px;
}

.el-input, .el-input__inner{
  width: 330px;
}
.el-date-editor--date {
  margin-right: 110px;
}
.el-form-item {
  margin-bottom: 3px;
}
.el-form-item__label {
  text-align: left;
  height: 30px;
}
.el-label-name .el-form-item__label {
  margin-right: 220px;;
}
.el-label-pwd .el-form-item__label {
  margin-right: 250px;;
}
.el-label-cpwd .el-form-item__label {
  margin-right: 200px;;
}
.el-label-username .el-form-item__label {
  margin-right: 250px;;
}
.el-label-identity .el-form-item__label {
  margin-right: 260px;;
}
.el-form-item__error {
  margin-left: 550px;
}
.el-progress-bar {
  text-align: center;
  width: 330px;
}
.el-form-item__label {
  margin-right: 260px
}

.el-button {
  margin-top: 30px;
  width: 335px;
  height: 35px;
}

#note {
  width: 14%;
  padding-left: 34.6%;
  display: block;
  font-size: 0.9em;
  color: rgb(87, 87, 95);
  font-size: 1em;
  width: 50%;
  margin-top: 8px;
  padding-left: 25%;
}


</style>