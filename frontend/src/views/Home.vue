<template>
  <div class="home">
    <div>
      <el-button type="text" @click="to_upload()">upload</el-button>
      <el-button type="text" @click="to_login()">login</el-button>
      <el-button type="text" @click="to_exam()">exam</el-button>
    </div>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  methods: {
    to_upload () {
      this.$router.push ('/upload');
    },
    to_login () {
      this.$router.push ('/login');
    },
    to_exam () {
      this.$router.push ('/exam');
    }
  },
  components: {
    // HelloWorld
  }
}
</script>
