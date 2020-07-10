import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import x2js from 'x2js'
// import axios from "axios"
import Vuex from 'vuex'

Vue.use(Vuex);


// Vue.prototype.$axios = axios;
Vue.prototype.$x2js = new x2js()

Vue.config.productionTip = false

new Vue({
  router,
  store: store,
  // axios,
  render: h => h(App)
}).$mount('#app')
