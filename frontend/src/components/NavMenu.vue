<template>
<div>
  <div class="menu-wrapper">
    <img class="logo" src="../assets/logo.png">
    <el-breadcrumb class="nav-menu" separator=" ">
      <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/exam' }">Exam</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/upload' }">Upload</el-breadcrumb-item>
      <el-breadcrumb-item></el-breadcrumb-item>
    </el-breadcrumb>
    <el-breadcrumb class="nav-user">
      <el-breadcrumb-item v-if="!this.$store.state.isLogin" :to="{ path: '/login' }">Login</el-breadcrumb-item>
      <el-breadcrumb-item v-else>
        <el-dropdown @click="handleClick" @command="handleCommand">
          <span class="el-dropdown-link">
            {{ this.$store.state.username }}
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="logout">Logout</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-breadcrumb-item>
    </el-breadcrumb>
      
  </div>
  <router-view/>
</div>
</template>

<script>
export default {
  name: "NavMenu",
  methods: {
    logout () {
      this.$store.dispatch ('logout');
    },
    handleCommand (command) {
      if (command == "logout") {
        this.$store.dispatch ('logout');
      }
    }
  }
}
</script>

<style scoped>
.menu-wrapper {
  position: absolute;
  top:0%;
  width: 100%;
  height: 40px;
  border-bottom: 1px solid #bcbec0;
  background-color: rgb(250, 250, 250);
  box-shadow: 0px 0px  0.2px 0.3px rgb(243, 243, 243);
}

.logo {
  width: 100px;
  position: absolute;
  top: 5px;
  left: 30px;
}
.nav-menu {
  font-size: 14px;
  position: absolute;
  top: 14px;
  left: 150px;
}
.nav-user {
  font-size: 14px;
  position: absolute;
  top: 14px;
  right: 50px;
}
</style>