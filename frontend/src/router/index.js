import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    meta: {
      requireLogin: true      // needed login
    },
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    meta: {
      requireLogin: false      // needed login
    },
    component: () => import ('../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'Signup',
    meta: {
      requireLogin: false      // needed login
    },
    component: () => import ('../views/Signup.vue')
  },
  {
    path: '/upload',
    name: 'Upload',
    meta: {
      requireLogin: true      // needed login
    },
    component: () => import ('../views/Upload.vue')
  },
  {
    path: '/exam',
    name: 'Exam',
    meta: {
      requireLogin: true      // needed login
    },
    component: () => import ('../views/Exam.vue')
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
