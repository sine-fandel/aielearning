<template>
<div>
  <div class="wrapper">
    <div>
      <el-button type="text" @click="to_home ()">home</el-button>
    </div>
    <p class="title">Login</p>
    <!-- login form -->
    <el-form class="login-form" :model="ruleForm" :rules="rules" ref="ruleForm" :label-position="ruleForm.labelPosition" label-width="80px">
      <el-form-item class="el-label-name" label="email address" prop='name'>
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>
      <el-form-item class="el-label-pwd" label="password" prop="pwd">
        <el-input v-model="ruleForm.pwd" show-password></el-input>
      </el-form-item>
    <!-- button -->
      <el-form-item class="btn-login">
        <el-button class="login-btn" type="primary" @click="log_in (ruleForm)">login</el-button>
      </el-form-item>
      <label id="note">———-— do not have an account ？————-</label>
      <el-form-item class="btn-signup">
        <el-button class="signup-btn" type="danger" @click="to_signup">sign up</el-button>
      </el-form-item>
    </el-form>
    <el-row>
      <p style="display: inline;margin-right:20px;">or login through:</p>
      <el-button class="wechat-btn" circle></el-button>
      <el-button class="qq-btn" circle></el-button>
    </el-row>
  </div>
  <router-view/>
  <!-- <Footer msg="COPYRIGHT©️2020"></Footer> -->
</div>
</template>

<script>
// import Footer from '../components/Footer.vue'
import axios from "axios"

export default {
  name: "Login",
  data () {
    return {
      ruleForm: {
        labelPosition: 'top',
        name: '',
        pwd: ''
      },
      rules: {
        name: [
          { required: true, message: "email cannot be empty", trigger: "blur" },
          { type: 'email', message: 'please input a real email', trigger: ['blur', 'change'] }
        ],
        pwd: [
          { required: true, message: "password cannot be empty", trigger: "blur" },
        ],
      }
    }
  },  
  methods: {
    log_in (formName) {
      if (formName.name == '' || formName.pwd == '') {
        this.$message ({
          message: "email and password can not be empty",
          type: "error"
        })
      }
      else {
        if (formName.name == '358746595@qq.com' && formName.pwd == 'hedyfattoo') {
          this.$router.push ('/upload')
        }
        else {
          this.$message ({
            message: "wrong email or password",
            type: "error"
          })
        }
      }
    },
    to_home () {
      this.$router.push ('/')
    },
    to_signup () {
      this.$router.push ('/signup')
    },
    test () {
      var config = {  headers: {'Content-Type': 'application/json'} };
      let url = "https://fangzx.pythonanywhere.com/api/login";
      let json_data = {
        email: this.ruleForm.name,
        password: this.ruleForm.password
      }
      axios.post (url, json_data, config).then (response => {
        if (response.data.msg == "success") {
          this.$msgbox ({
            title: 'success',
            message: "sign up successfully"
          })
          this.$router.push ('/login')
        }
        else {
          this.$msgbox ({
            title: 'wrong',
            message: response.data.msg
          })
        }
      }).catch (error => {
        console.log (error);
        alert (error);
      })
    }
    },
  components: {
    // Footer,
  }
}
</script>

<style lang="scss">
.title {
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 40px;
}

.el-input {
  width: 330px;
}
.el-form-item {
  margin-bottom: 10px;
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
.el-form-item__error {
  margin-left: 550px;
}

#note {
  margin-bottom: 5px;
  width: 14%;
  padding-left: 34.6%;
  display: block;
  font-size: 0.9em;
  color: #606266;
  width: 50%;
  margin-top: 8px;
  padding-left: 25%;
}

// button css
.signup-btn, .login-btn {
  margin-top: 10px;
  width: 335px;
  height: 35px;
}
.signup-btn {
  background-color: #B92B24;
}
.wechat-btn {
  width: 40px;
  height: 40px;
  background-image: url('http://bpic.588ku.com/element_pic/00/74/74/7356e003cb881b0.jpg') ;
  background-size:67px 67px;
  background-repeat: no-repeat;
  background-position: 50% 50%;
}
.qq-btn {
  width: 40px;
  height: 40px;
  background-image: url('http://www.free-icons-download.net/images/tencent-qq-icon-95736.png');
  background-size:74px 74px;
  background-repeat: no-repeat;
  background-position: 50% 50%;
}

.Footer {
  margin-top: 500px;
}
</style>