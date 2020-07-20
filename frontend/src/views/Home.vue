<template>
  <div class="home">
    <NavMenu></NavMenu>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import NavMenu from '../components/NavMenu'

export default {
  name: 'Home',
  data () {
    return {
      count: 0
    }
  },
  components: {
    NavMenu
  }
}
</script>
