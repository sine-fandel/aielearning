<template>
  <div class="home">
    <div>
      <el-button type="text" @click="to_upload()">upload</el-button>
      <el-button type="text" @click="to_login()">login</el-button>
      <el-button type="text" @click="to_exam()">exam</el-button>
    </div>
    <router-view/>
    <div v-if="!this.$store.state.isLogin">Please Login</div>
    <div v-else>Welcome {{ this.$store.state.username }}</div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data () {
    return {
      count: 0
    }
  },
  mounted () {
    this.increment ()
  },
  methods: {
    to_upload () {
      this.$router.push ('/upload');
    },
    to_login () {
      this.$router.push ('/login');
    },
    to_exam () {
      this.$router.push ('/exam');
    },
    increment () {
      // this.$store.commit ('increment');
      // this.count = this.$store.state.count;
    }
  },
  components: {
    // HelloWorld
  }
}
</script>
