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

router.beforeEach ((to, from, next) => {
  if (to.meta.requireLogin) {
    if (localStorage.getItem ('islogin')) {
      next ();
    }
    else {
      next ({
        path: '/login',
        query: {redirect: to.fullPath},
      });
    }
  }
  else {
    next ();
  }
})

new Vue({
  router: router,
  store: store,
  // axios,
  render: h => h(App)
}).$mount('#app')
