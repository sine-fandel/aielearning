import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: localStorage.getItem ('islogin'),
    username: localStorage.getItem ('username'),
  },
  mutations: {
    LOGIN (state) {
      state.isLogin = localStorage.getItem ('islogin');
      state.username = localStorage.getItem ('username');
    },
    LOGOUT (state) {
      state.isLogin = localStorage.removeItem ('islogin');
      state.username = localStorage.removeItem ('username');
    }
  },
  actions: {
    login (context) {
      context.commit ('LOGIN');
    },
    logout (context) {
      context.commit ('LOGOUT');
    }
  },
  modules: {
  }
})
